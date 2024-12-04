#imported libraries
import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents = intents)
token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

# this function prints out a message if a certain word is sent into the chat
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "on" in message.content:
        await message.channel.send("ON!")

client.run(token)
