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

        month_to_season = {
            12: "winter", 1:"winter", 2:"winter",
            3: "spring", 4:"spring", 5:"spring",
            6:"summer", 7:"summer", 8:"summer",
            9:"autumn", 10:"autumn", 11:"autumn"
        }

        season_words = {
            "winter": ["餅", "墨汁", "雪", "オーロラ"],
            "spring": ["卒業", "桜", "チューリップ"],
            "summer": ["アジサイ", "傘", "波"],
            "autumn": ["紅葉"]
        }

        now_month = datetime.datetime.now().month
        current_season = month_to_season[now_month]

        words = fixed_words.copy()
        words.extend(season_words.get(current_season, []))

        chosen = random.choice(words)

        await interaction.response.send_message(
            f"{interaction.user.mention} あなたへのお題は **『 {chosen} 』** です！\n"
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
