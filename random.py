
# Imports
import asyncio
import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

# 
class MyClient(discord.Client):

    #
    async def on_message(self, message):
        if message.author == self.author:
            return
        await message.channel.send('Message Received!')
    #
    async def on_raw_reaction_add(self, payload):


    #
    

client = MyClient()
client.run(config.token)