from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial
import youtube_dl
from youtube_dl import YoutubeDL
import os 

async def load_extensions(bot):
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            await bot.load_extension(f"modules.{folder}.cog")

def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    intents.message_content = True
    intents.typing = True
    bot = commands.Bot(command_prefix='=', intents=intents)

    load_dotenv()
    token = os.getenv('TOKEN')

    asyncio.run(load_extensions(bot))

    bot.run(token)

if __name__=="__main__":
    main()
