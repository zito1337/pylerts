import asyncio

from src.pylerts_bot import PylertsBot
from src.pylerts_config import Config
from src.pylerts_da import DonationAlertsClient
from src.pylerts_logger import log


async def main():
    log("init", "please wait for da & pylerts to init")

    config = Config.load()
    # initialize discord bot
    bot = PylertsBot(config)
    # initialize da client
    da_client = DonationAlertsClient(
        token=config.da_widget_token, on_donation_callback=bot.grant_role
    )

    # for Socket.IO to work with the bot, create a background task to run it
    async def start_services():
        async with bot:
            # run the DA client in the background
            asyncio.create_task(da_client.start())
            # run the Discord bot (this is a blocking call)
            await bot.start(config.discord_token)

    await start_services()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log("pylerts", "shutdown")
