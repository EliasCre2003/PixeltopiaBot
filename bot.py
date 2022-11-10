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
async def whitelist(ctx, arg=None, name=None):
    if arg is None:
        return
    if arg == "add":
        if name is None:
            return
        # Add user to whitelist
        await ctx.send(f'Added {name} to the whitelist')
    if arg == "remove":
        # Remove user from whitelist
        await ctx.send(f'Removed {name} from the whitelist')
    if arg == "list":
        # List all users in whitelist
        await ctx.send(f'Whitelist: {name}')


@bot.command()
async def stop(ctx):
    await ctx.send('Stopping server...')


@bot.command()
async def restart(ctx):
    await ctx.send('Restarting server...')


@bot.command()
async def gamerule(ctx, rule=None, value=None):
    if rule is None:
        return
    if value is None:
        return
    # Set gamerule
    await ctx.send(f'Set gamerule {rule} to {value}')


@bot.command()
async def ban(ctx, name=None):
    if name is None:
        return
    # Ban user
    await ctx.send(f'Banned {name}')


@bot.command()
async def banip(ctx, name=None):
    if name is None:
        return
    # Ban IP
    await ctx.send(f'IP Banned {name}')


bot.run(TOKEN)
