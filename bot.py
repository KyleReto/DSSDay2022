import os
import re
import discord
from dotenv import load_dotenv
from pathlib import Path
import glob
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} connected successfully')

@bot.slash_command(description='test command')
async def ping(ctx):
    return await ctx.respond("pong")

bot.run(TOKEN)