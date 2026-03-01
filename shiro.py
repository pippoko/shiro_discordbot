import discord
import os
from keep import keep_alive


class Shiro(discord.Client):

    async def on_ready(self):
        print(f"ログインしました：{self.user}")

    async def on_message(self, message):
        print(f"メッセージを受信：{message.content} (送信者: {message.author})")
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('こんにちは！')

    async def setup_hook(self):
        await self.load_extension("word_button")


intents = discord.Intents.default()
intents.message_content = True

client = Shiro(intents=intents)

keep_alive()
try:
    client.run(os.environ['DISCORD_BOT_TOKEN'])
except:
    os.system("kill")


async def setup_hook(self):
    await self.load_extension("word_button")
