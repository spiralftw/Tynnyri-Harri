import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents = intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "homo" in message.content:
        await message.channel.send("ite oot homo")

client.run(token)