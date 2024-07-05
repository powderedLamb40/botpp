import discord
from discord.ext import commands
from config import TOKEN_BOT

TOKEN = config.TOKEN

class Bot(commands.Bot):

    def __init__(self, intents: discord.Intents, **kwargs):
        super().__init__(
            command_prefix="!",  # Set command prefix
            intents=intents,
            case_insensitive=True)  # Make commands case-insensitive

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        await self.tree.sync()
        activity = discord.Activity(type=discord.ActivityType.streaming,
                                    name="/help_pp | PP",
                                    url="https://www.twitch.tv/powderedlamb40")
        await self.change_presence(activity=activity)



bot.run(TOKEN)
