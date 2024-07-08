import discord
from discord.ext import commands
from discord import ButtonStyle
from discord.ui import Modal, Button, View, TextInput
import config
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

@bot.hybrid_command(name='help_pp', description='ขอความช่วยเหลือ.')
async def help(ctx):  # Use Context type
    button = Button(style=discord.ButtonStyle.link,
                    label='ขอความช่วยเหลือ',
                    url='https://discord.gg/yNKGyDumje')

    # Create a View to contain the Button
    view = View()
    view.add_item(button)

    # Send a message with the Button to the chat
    await ctx.send('สวัสดี! คุณต้องการความช่วยเหลือในสิ่งใด?', view=view)


@bot.hybrid_command(name='ping', description='ค่าปิงของบอท.')
async def ping(ctx):  # Use Context type
    latency = bot.latency
    # แปลงค่า latency จากวินาทีเป็นมิลลิวินาที
    latency_ms = latency * 1000
    await ctx.send(f'บอทมีค่า ping เท่ากับ {latency_ms:.2f} มิลลิวินาที')


bot.run(TOKEN)
