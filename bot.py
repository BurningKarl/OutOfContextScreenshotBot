# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="ooc_")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    for guild in bot.guilds:
        print(f"{bot.user} is connected to {guild.name} (id: {guild.id})")
        print(f"  Its members are:", [member.name for member in guild.members])


@bot.command(
    name="screenshot",
    help="Responds with a screenshot of your Out of Context lobby",
)
async def on_message(ctx, lobby: str):
    await ctx.send("Hi! I registered your request.")


bot.run(TOKEN)
