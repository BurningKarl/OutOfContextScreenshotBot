# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in client.guilds:
            print(f'{self.user} is connected to {guild.name} (id: {guild.id})')
            print(f'  Its members are:', [member.name for member in guild.members])

    async def on_message(self, message):
        if message.author == client.user:
            return
        print(message)
        
        if message.content == '!scribble_screenshot':
            await message.channel.send('Hi! I registered your request.')


client = BotClient()
client.run(TOKEN)


