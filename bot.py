# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

from screenshot import save_outofcontext_screenshot

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
async def send_screenshot(ctx, lobby: str):
    waiting_message = await ctx.send("Wait a moment")
    filename = save_outofcontext_screenshot(lobby)
    await ctx.send(file=discord.File(filename))
    os.remove(filename)
    await waiting_message.delete()
    await ctx.message.delete()


@send_screenshot.error
async def send_screenshot_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("You need to supply a lobby id.")
    else:
        raise error


bot.run(TOKEN)
