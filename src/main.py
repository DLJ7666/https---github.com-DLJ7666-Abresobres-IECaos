import os
import discord
from discord.ext import commands
import random
from discord.ext import tasks
from src.keep_alive import live 
from data.cartas import lista_completa_cartas
from src.panini import *
my_secret = os.environ['Tokensita AbreSobres']

client = commands.Bot(command_prefix='=',intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Bot encendido')


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def abrirsobre(ctx):
    await ctx.send(f'{generar_sobre(1, lista_completa_cartas)}')
    await ctx.send(f'{generar_sobre(1, lista_completa_cartas)}')
    await ctx.send(f'{generar_sobre(1, lista_completa_cartas)}')

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def info(ctx):
      await ctx.send(
        '''Bot del servidor Inazuma Eleven Caos
        https://discord.gg/UPKf2UqCCp
      Hecho por jard2334, admin de:
      MULTIVERSO F1
        https://discord.gg/MBVDVNZFB4 
      Copa Pistón
        https://discord.gg/e8F9ZYRDCD '''
        )
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx):
      await ctx.send("pong!")
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def Mehr(ctx):
      await ctx.send(r"Mehr😍 https://t.ly/orn- ")
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def porno_gay(ctx):
      await ctx.send("bro? 🧐📸")
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def seducir(ctx):
      await ctx.send(" https://media.tenor.com/UQMFZNqpzgUAAAAd/la-seduce.gif ")
live()

client.run(my_secret)

#try:
    #client.run(os.getenv('TOKEN'))
#except discord.errors.HTTPException:
    #print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    #system("python restarter.py")
    #system('kill 1')
try:
    client.start(my_secret)
except:
    os.system("kill 1")