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
            log("pylerts", f"sever with id {self.cfg.guild_id} not found")
            return

        role = guild.get_role(self.cfg.role_id)
        if not role:
            log("pylerts", f"role {self.cfg.role_id} not found on server")
            return

        search_name = str(name).lower()
        target_member = None

        # search for member
        for member in guild.members:
            member_names = [str(member.name).lower(), str(member.display_name).lower()]
            if hasattr(member, "global_name") and member.global_name:
                member_names.append(str(member.global_name).lower())

            if search_name in member_names:
                target_member = member
                break

        if target_member:
            if role in target_member.roles:
                log("pylerts", f"{name} already has a role")
                return

            try:
                await target_member.add_roles(role)
                log("pylerts", f"given role to {name}")
            except Exception as e:
                log("pylerts", f"error giving role to {name}: {e}")
        else:
            log("pylerts", f"user {name} not found on server")
