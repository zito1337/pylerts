import json

import socketio

from src.pylerts_logger import log


class DonationAlertsClient:
    def __init__(self, token: str, on_donation_callback):
        self.token = token
        self.on_donation_callback = on_donation_callback
        self.processed_ids = set()

        self.sio = socketio.AsyncClient(
            reconnection=True,
            reconnection_attempts=0,
            reconnection_delay=3,
            reconnection_delay_max=15,
            logger=False,
            engineio_logger=False,
        )
        self._register_events()

    def _register_events(self):
        @self.sio.on("connect")
        async def on_connect():
            log("da", "connected to DA")
            await self.sio.emit(
                "add-user", {"token": self.token, "type": "alert_widget"}
            )

        @self.sio.on("disconnect")
        async def on_disconnect():
            log("da", "disconnected from DA")

        @self.sio.on("donation")
        async def on_donation(data):
            try:
                if isinstance(data, str):
                    event = json.loads(data)
                elif isinstance(data, dict):
                    event = data
                else:
                    return

                await self._process_donation(event)
            except Exception as e:
                pass  # ignore empty packets from DA

    async def _process_donation(self, event: dict):
        donation_id = int(event.get("id", 0))

        # protection against duplicates
        if donation_id != 0:
            if donation_id in self.processed_ids:
                return
            self.processed_ids.add(donation_id)
            if len(self.processed_ids) > 1000:
                self.processed_ids.clear()

        name = event.get("username", "Anonymous")
        amount = event.get("amount", "0")
        currency = event.get("currency", "RUB")

        log("da", f"{name} donated {amount} {currency}")

        # pass donation data to discord bot
        await self.on_donation_callback(name, amount, currency)

    async def start(self):
        if not self.sio.connected:
            try:
                await self.sio.connect(
                    "wss://socket.donationalerts.ru:443", transports=["websocket"]
                )
            except Exception as e:
                log("da", f"Socket connection error: {e}")
