import openai
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())

openai.api_key = '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'
model_engine = "davinci"

@client.event
async def on_ready():
  print('Puta Madre, опять за работу')

@client.command()
async def chat(ctx, *, message):
  response = openai.Completion.create(
    prompt=message,
    model=model_engine,
    temperature=0.9,
    max_tokens=100,
    n=1,
    stop=None,
    )
  
  bot_reply = response.choices[0].text
  await ctx.send(bot_reply)

client.run('MTE1MjYwMTI2MTk2Nzk0MTc3NA.GYz5Zg.MP4kE26iTGtQpROpzq7xysJpFK8PwSYxN_EiWc')