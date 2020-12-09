
# Imports
import discord
import config
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

emoji_to_role = {
    u"\U0001F44D" : config.react_role_1_id,
    u"\U0001F44E" : config.react_role_2_id
}

# 
class MyClient(discord.Client):

    #
    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send('Message Received!')

    #
    async def on_raw_reaction_add(self, payload):
        if payload.message_id != config.react_msg_id:
            return 

        try:
            role_id = emoji_to_role[payload.emoji.name]
        except KeyError:
            return

        server = self.get_guild(payload.guild_id)
        role = server.get_role(role_id)

        try:
            await payload.member.add_roles(role)
        except discord.HTTPException:
            pass

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != config.react_msg_id:
            return

        try:
            role_id = emoji_to_role[payload.emoji.name]
        except KeyError:
            return

        server = self.get_guild(payload.guild_id)
        role = server.get_role(role_id)

        try:
            await server.get_member(payload.user_id).remove_roles(role)
        except discord.HTTPException:
            pass

    #

# Setup
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run(config.token)