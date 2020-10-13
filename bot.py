# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

from screenshot import (
    save_outofcontext_screenshot,
    InvalidLobbyException,
    PageNotFoundException,
    PageDesignChangedException,
)

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
async def send_screenshot(ctx, lobby: str, channel: discord.TextChannel = None):
    channel = channel or ctx
    try:
        working_message = await ctx.send("Started working on it ...")
        filename = save_outofcontext_screenshot(lobby)
    except (
        InvalidLobbyException,
        PageNotFoundException,
        PageDesignChangedException,
    ) as error:
        await channel.send(str(error))
    except Exception as error:
        await channel.send(repr(error))
        raise error
    else:
        await channel.send(file=discord.File(filename))
        os.remove(filename)
        await working_message.edit(content="Started working on it ... Done")
    finally:
        await working_message.edit(delete_after=10)


@send_screenshot.error
async def send_screenshot_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        if error.param.name == "lobby":
            await ctx.send("You need to supply a lobby id.")
        else:
            await ctx.send(str(error))
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.send(str(error))
    else:
        await ctx.send(repr(error))
        raise error


bot.run(TOKEN)
