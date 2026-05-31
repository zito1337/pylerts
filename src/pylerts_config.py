import os
import sys
from dataclasses import dataclass, field

import tomllib

from src.pylerts_logger import log


@dataclass
class DonationRule:
    min_amount: float
    role_ids: list[int]
    currency: str | None = None
    exclude_role_ids: list[int] = field(default_factory=list)


@dataclass
class Config:
    discord_token: str
    guild_id: int
    da_widget_token: str
    rules: list[DonationRule] = field(default_factory=list)

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

            raw_rules = data.get("rules", [])
            rules = []
            for r in raw_rules:
                # Чтение ролей для выдачи
                role_ids = r.get("role_ids", [])
                if isinstance(role_ids, int):
                    role_ids = [role_ids]
                elif not isinstance(role_ids, list):
                    role_ids = []

                # Чтение ролей для удаления
                exclude_role_ids = r.get("exclude_role_ids", [])
                if isinstance(exclude_role_ids, int):
                    exclude_role_ids = [exclude_role_ids]
                elif not isinstance(exclude_role_ids, list):
                    exclude_role_ids = []

                rules.append(
                    DonationRule(
                        min_amount=float(r.get("min_amount", 0.0)),
                        role_ids=[int(rid) for rid in role_ids],
                        currency=r.get("currency"),
                        exclude_role_ids=[int(erid) for erid in exclude_role_ids],
                    )
                )

            return cls(
                discord_token=data["discord"]["bot_token"],
                guild_id=int(data["discord"]["guild_id"]),
                da_widget_token=data["donationalerts"]["widget_token"],
                rules=rules,
            )
        except Exception as e:
            log("pylerts", f"error reading .config: {e}")
            sys.exit(1)
