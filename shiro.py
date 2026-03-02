import discord
from discord.ext import commands
import os
import asyncio
import datetime

class Shiro(commands.Bot):
    async def on_ready(self):
        print(f"ログインしました：{self.user}")

    async def on_message(self, message):
        print(f"メッセージを受信：{message.content} (送信者: {message.author})")
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('こんにちは！')

        await self.process_commands(message)

    async def setup_hook(self):
        await self.load_extension("word_button")
        self.loop.create_task(sleep_cheacker(self))


intents = discord.Intents.default()
intents.message_content = True

async def sleep_cheacker(bot):
    await bot.wait_until_ready()
    while not bot.is_closed():
        now = datetime.datetime.now().time()

        if datetime.time(1, 0) <= now <= datetime.time(9, 0):
            print("深夜・早朝帯のためBotを停止します")
            await bot.close()
            break

        await asyncio.sleep(60)

client = Shiro(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN is None:
    print("✖ トークンが読み込めませんでした。RailwayのVariablesを確認してください。")
else:
    client.run(TOKEN)




