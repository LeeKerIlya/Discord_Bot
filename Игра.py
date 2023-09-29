import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('Угадать число'):
            await message.channel.send('Угадай число от 1 до 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Извини, время вышло, ответ - {answer}.')

            if int(guess.content) == answer:
                await message.channel.send('Ты полностью прав!')
            else:
                await message.channel.send(f'Ой, ой ответ - {answer}.')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1MjYwMTI2MTk2Nzk0MTc3NA.GpgLhq.BrKtNGI0EEG4GCCh9JUBN-QBSzS9l5fO7g-4Do')