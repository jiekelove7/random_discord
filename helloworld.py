import discord
import config

class MyClient(discord.Client):
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        await message.channel.send('Hello World!')

        # Prints message it sees
        # Success!
        # print('{0.author}: {0.content}'.format(message))

client = MyClient()
client.run(config.token)