import discord
import os
from dotenv import load_dotenv
load_dotenv()

class Shiro(discord.Client):
    async def on_ready(self):
        print(f"ログインしました：{self.user}")

    async def on_message(self, message):
        print(f"メッセージを受信：{message.content} (送信者: {message.author})")
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('こんにちは！')

intents = discord.Intents.default()
intents.message_content = True

client = Shiro(intents=intents)
client.run(os.getenv('DISCORD_BOT_TOKEN'))