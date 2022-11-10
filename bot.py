import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents(messages=True, message_content=True, guilds=True, members=True)
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='mc ', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@bot.command()
async def whitelist(ctx, arg=None, name=''):
    if arg == None:
        return
    if arg == "add":
        # Add user to whitelist
        await ctx.send(f'Added {name} to the whitelist')
    if arg == "remove":
        # Remove user from whitelist
        await ctx.send(f'Removed {name} from the whitelist')
    if arg == "list":
        # List all users in whitelist
        await ctx.send(f'Whitelist: {name}')

bot.run(TOKEN)
