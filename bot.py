import discord
import aiohttp
from random import randint
import io

TOKEN = 'token' #Place your bot token here!

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        msg = message.content
        if 'cat' in msg.lower():
            x = str(randint(200,600)) #Both x and y are cat image width and height sizes and generated randomly
            y = str(randint(200,600)) # between 200px and 600px. You can change if you want!
            url = f"http://placekitten.com/{x}/{y}"
            async with aiohttp.ClientSession() as session: 
                async with session.get(url) as resp: 
                    img = await resp.read() 
                    with io.BytesIO(img) as file: 
                        await message.channel.send(file=discord.File(file, "testimage.png"))

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN) 

