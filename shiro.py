import discord
from discord.ext import commands
import os
import asyncio
import datetime

class Shiro(commands.Bot):
    async def on_ready(self):
        print(f"ログインしました：{self.user}")

        channel_id = 1477907626342875298
        channel = self.get_channel(channel_id)

        if channel:
            view = WordButtonView()
            msg = await channel.send("ボタンを押して単語を表示してください！", view=view)

            with open("button_message.txt", "w") as f:
                f.write(str(msg.id))

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
        now_utc = datetime.datetime.utcnow().time()

        if datetime.time(17, 0) <= now_utc or now_utc < datetime.time(0, 0):
            print("深夜・早朝帯のためBotを停止します")
            try:
                with open("button_message.txt", "r") as f:
                    msg_id = int(f.read().strip())
                channel = bot.get_channel(1477907626342875298)
                msg = await channel.fetch_message(meg_id)
                await msg.delete()
            except Exception as e:
                print("削除に失敗：", e)
            
            await bot.close()
            break

        await asyncio.sleep(60)

client = Shiro(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN is None:
    print("✖ トークンが読み込めませんでした。RailwayのVariablesを確認してください。")
else:
    client.run(TOKEN)






