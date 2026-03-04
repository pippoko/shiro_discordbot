import discord
from discord.ext import commands
import random
import datetime

class WordButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="単語を表示", style=discord.ButtonStyle.primary, custom_id="word_button")
    async def send_word(self, interaction: discord.Interaction, button: discord.ui.Button):

        fixed_categories = {
            #素材や質感表現
            "texture": [
                "サテン生地", "レザー生地", "木目", "石", "金属", "シルク生地", "ダイヤモンド", "オパール", "パール", "ガラス", "ネオンライト", "木漏れ日"
            ]
            #単数や複数でのポーズ
            "pose": [
                "見上げる", "見下ろす", "走る", "転ぶ", "しゃがむ", "ジャンプ", "上に手が届かない…", "椅子に座る", "地面に座る",
                "背中", "横顔",  "振り向く", "伸び", "ウォーミングアップ",
                "髪を耳にかける", "ギャルピース", "髪を縛る", "足を見せる", "裾を持つ"
                "銃を構える", "ペンを持つ", "メガネｸｲｯ", "タイピング", "スマホを使う", "スマホでもしもし？", "古の電話でもしもし？", "傘を差す", "剣を構える",
                "ハグ",  "目隠し", "あーん", "腕を絡める", "手をつなぐ", "恋人繋ぎ", "指切りげんまん"
            ]
            "background": [
                "街角", "港", "夜景", "路地裏", "図書館", "学校", "駅", "噴水", "公園", "リビング", "電車の車内", "カフェの窓際", "映画館", "廃墟", "温室", "屋上", "海辺", "森の中"
            ]
            "item":[
                "バラ", "棒キャンディ", "傘", "本", "スマホ", "イヤホン", "花束", "マグカップ", "リボン"
            ]
            #雰囲気や演出
            "mood":[
                "逆光", "虹", "朝焼け", "夕暮れ", "オーロラ"
            ]
            #シチュエーション
            "situation": [
                "雨宿り", "相合傘", "徹夜中", "散歩", "1日だけの休み", "料理中", "読書中"
            ]
            "fashion": [
                "パーカー", "ロングスカート", "ホットパンツ", "キャミソール", "ジーンズ",
                "セーラー服", "浴衣", "着物", "ウェディングドレス", "タキシード", "ダンスドレス", "レオタード", "バニー服"
                "ストッキング", "ニット帽", "ブーツ", "ハイヒール", "マフラー", "手袋", "ピアス"
            ]
            #イラスト全体におけるスタイルとか
            "style":[
                "デフォルメ", "ヴィネットイラスト", "フカン", "アオリ"
            ]
        }


        # 季節ごと
        season_words = {
            "winter": ["餅", "墨汁", "雪", "オーロラ"],
            "spring": ["卒業", "桜", "チューリップ"],
            "summer": ["アジサイ", "傘", "波"],
            "autumn": ["紅葉"]
        }
        
        month_to_season = {
            12: "winter", 1:"winter", 2:"winter",
            3: "spring", 4:"spring", 5:"spring",
            6:"summer", 7:"summer", 8:"summer",
            9:"autumn", 10:"autumn", 11:"autumn"
        }

        now_month = datetime.datetime.now().month
        current_season = month_to_season[now_month]

        fixed_words = []
        for category_list in fixed_categories.values():
            fixed_words.extend(category_list)

        word = fixed_words + season_words.get(current_season, [])

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
