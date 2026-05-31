import os
import sys
from dataclasses import dataclass

import tomllib

from src.pylerts_logger import log


@dataclass
class Config:
    discord_token: str
    guild_id: int
    role_id: int
    da_widget_token: str

    @classmethod
    def load(cls) -> "Config":
        # search for .config in root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "pylerts.config")

        if not os.path.exists(config_path):
            config_path = "pylerts.config"  # fallback

        try:
            with open(config_path, "rb") as f:
                data = tomllib.load(f)

            return cls(
                discord_token=data["discord"]["bot_token"],
                guild_id=data["discord"]["guild_id"],
                role_id=data["discord"]["role_id"],
                da_widget_token=data["donationalerts"]["widget_token"],
            )
        except Exception as e:
            log("pylerts", f"error reading .config: {e}")
            sys.exit(1)
