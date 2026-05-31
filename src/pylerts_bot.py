import discord
from discord.ext import commands

from src.pylerts_config import Config
from src.pylerts_logger import log


class PylertsBot(commands.Bot):
    def __init__(self, config: Config):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)
        self.cfg = config

    async def on_ready(self):
        log("pylerts", "discord bot init")

    async def grant_role(self, name: str, amount: str, currency: str):
        guild = self.get_guild(self.cfg.guild_id)
        if not guild:
            log("pylerts", f"server with id {self.cfg.guild_id} not found")
            return

        try:
            donation_amount = float(amount)
        except ValueError:
            log("pylerts", f"invalid donation amount format: {amount}")
            return

        donation_currency = str(currency).upper()

        roles_to_add = set()
        roles_to_remove = set()

        # Gather targets from matching rules
        for rule in self.cfg.rules:
            if rule.currency and rule.currency.upper() != donation_currency:
                continue

            if donation_amount >= rule.min_amount:
                for role_id in rule.role_ids:
                    roles_to_add.add(role_id)
                for role_id in rule.exclude_role_ids:
                    roles_to_remove.add(role_id)

        # Exclusion takes priority
        roles_to_add = roles_to_add - roles_to_remove

        if not roles_to_add and not roles_to_remove:
            log(
                "pylerts",
                f"{name} donated {amount} {currency}, but no matching actions found",
            )
            return

        search_name = str(name).lower()
        target_member = None

        # search for member
        for member in guild.members:
            member_names = [
                str(member.name).lower(),
                str(member.display_name).lower(),
            ]
            if hasattr(member, "global_name") and member.global_name:
                member_names.append(str(member.global_name).lower())

            if search_name in member_names:
                target_member = member
                break

        if not target_member:
            log("pylerts", f"user {name} not found on server")
            return

        # 1. Grant roles
        for role_id in roles_to_add:
            role = guild.get_role(role_id)
            if not role:
                log("pylerts", f"role {role_id} not found on server")
                continue

            if role in target_member.roles:
                log("pylerts", f"{name} already has role {role.name} ({role_id})")
                continue

            try:
                await target_member.add_roles(role)
                log("pylerts", f"given role {role.name} ({role_id}) to {name}")
            except Exception as e:
                log("pylerts", f"error giving role {role_id} to {name}: {e}")

        # 2. Remove excluded roles
        for role_id in roles_to_remove:
            role = guild.get_role(role_id)
            if not role:
                continue

            if role in target_member.roles:
                try:
                    await target_member.remove_roles(role)
                    log("pylerts", f"removed role {role.name} ({role_id}) from {name}")
                except Exception as e:
                    log("pylerts", f"error removing role {role_id} from {name}: {e}")
