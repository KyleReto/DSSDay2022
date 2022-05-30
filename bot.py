# Set up libraries
import os
import discord
from dotenv import load_dotenv

# Set up boilerplate
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')
bot = discord.Bot()

# Set up file imports
from user import User
import database
import combat

@bot.event
async def on_ready():
    print(f'{bot.user} connected successfully')

@bot.slash_command(description='test command')
async def ping(ctx):
    test = User('test')
    test.xp = 200
    return await ctx.respond(test.get_level())

@bot.slash_command(description="test")
async def test(ctx):
    return await ctx.respond("this is a button", view=combat.CombatView())

bot.run(TOKEN)