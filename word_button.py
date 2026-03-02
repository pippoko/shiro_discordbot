import discord
from discord.ext import commands
import random
import datetime

class WordButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="単語を表示", style=discord.ButtonStyle.primary, custom_id="word_button")
    async def send_word(self, interaction: discord.Interaction, button: discord.ui.Button):

        fixed_words = [
            "ヴィネットイラスト", "デフォルメ", "サテン生地", "フリル", "アオリ", "フカン",
            "レザー", "水面", "日差し", "レンガ", "街角", "鏡", "バラ", "着物",
            "背中", "横顔", "ハグ", "髪を耳にかける", "ストッキング", "プリーツスカート"
        ]

        limited_words = {
            1: ["餅", "墨汁"],
            2: ["バレンタイン"],
            3: ["卒業"],
            4: ["桜"],
            5: ["こいのぼり"],
            6: ["アジサイ", "傘"],
            7: ["日差し"],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        }

        now_month = datetime.datetime.now().month

        words = fixed_words.copy()
        if now_month in limited_words:
            words.extend(limited_words[now_month])

        chosen = random.choice(words)

        await interaction.response.send_message(
            f"{interaction.user.mention} あなたへのお題は **{chosen}** です！\n"
            "資料をたっぷり見て描いて、できたら https://discord.com/channels/1292757949608886353/1293199504459436134 にあげてみてね！",
            ephemeral=True
        )


class WordButtonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="wordbutton")
    async def word_button_command(self, ctx):
        view = WordButtonView()
        await ctx.send("ボタンを押して単語を表示してください！", view=view)


async def setup(bot):
    await bot.add_cog(WordButtonCog(bot))
