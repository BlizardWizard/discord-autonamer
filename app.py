
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio


Client = discord.Client()
bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("discord-autoname Bot is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="changing nick\'s"))


@bot.event
async def on_member_join(member):
    num = int(open('count.txt', 'r').readline().replace('\\n', ''))
    name = "foreskin" + str(num)
    await bot.change_nickname(member, name)
    num += 1
    open('count.txt', 'w').write(str(num))




token_file = open('token.txt', 'r')
token = token_file.readline().replace('\n', '')
token_file.close()
bot.run(token)
