import discord
import asyncio
from discord.ext import commands

token = "ODI3NTYwOTE1MDM3MTkyMjUz.YGc0KQ.Yo5gJrMGckTHn0bB_R1a6T7v8go"
app = discord.Client()
from discord.utils import get
ch = app.get_channel(837232418515320862)
app = commands.Bot(command_prefix='PTOX')

@app.command(name="밴", pass_context=True)
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+"을(를) 영원히 매장시켰습니다.")

@app.event
async def on_ready():
    print("봇이 실행되었습니다!")
    print(app.user)
    print("저는 레이첼님이 탄생시키신 SERVER.BOT 입니다!")
    game = discord.Game("!help")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.content == "!help":
        await message.channel.send("해당 봇은 레이첼님이 만드신 봇입니다. 욕설시 경고가 부여되니 욕설은 되도록 하지 않는게 좋겠죠?")
    if message.content == "!YT":
        embed = discord.Embed(title="https://www.youtube.com/channel/UCzjiNd25WE9gU-AqDAdc2pQ 애크님이 운영하시는 유튜브 입니다. 한번씩 들어오셔서 구독, 좋아요 눌러주세요.", description="구독한걸 인증하면 애크님 서버에서 하군단 역할이!?!?", color=0x00ff00)
        embed.set_footer(text="와! 이건 눌러야 겠는걸?")
        await message.channel.send(embed=embed)
    if message.content == "!AEKEU":
        await message.channel.send("해당 봇 제작 의뢰하신 분")
    if message.content == "!레이첼":
        await message.channel.send("이 봇을 만드신 세상에서 제일 가는 봇 제작자")
    if message.content == "!뉴트로":
        await message.channel.send("고 덴버서버 아틀란티스 총리이자 마지막 총리")
    if message.content == "!쿠키":
        await message.channel.send("파라다이스를 만드려 했던 바보")
    if message.content == "!수헌":
        await message.channel.send("아틀란티스 봇 만드시는 레이첼의 봇 제작자 팀원?")
    if message.content == "!파란종이":
        await message.channel.send("아틀란티스 봇 만드시는 레이첼의 봇 제작자 팀원?")
    if message.content == "!곰":
        await message.channel.send("이 봇의 제작자가 개인적으로 싫어하는 동물")
    if message.content == "!라면":
        await message.channel.send("세상에서 제일 맛있는 음식")
    if message.content == "!태아틀 연방당":
        await message.channel.send(f"{message.author.mention}님 가입이 완료되었습니다")
    if message.content == "!AP 당":
        await message.channel.send(f"{message.author.mention}님 가입이 완료되었습니다")
    if message.content == "!오션하트 당":
        await message.channel.send(f"{message.author.mention}님 가입이 완료되었습니다")
    if message.content.startswith(" 당"):
        embed = discord.Embed(title="사용자 님이 치신 당은 현재 존재하지 않습니다.   현재 당 리스트입니다", description="태아틀 연방당 , 오션하트 당 , AP 당", color=0x00ff00)
        embed.set_footer(text="해당 당들에 들어오고 싶으시다면 !태아틀 연방당 , !오션하트 당 , !AP 당    이렇게 입력하시면 됩니다.")
        await message.channel.send(embed=embed)
    if message.content == "아틀봇":
        await message.channel.send("넹?")
    if message.content == "아틀 봇":
        await message.channel.send("넹?")
    if message.content == ("안녕"):
        await message.channel.send("안녕하세요!")
    if message.content == "아틀봇?":
        await message.channel.send("넹?")
    if message.content == "아틀 봇?":
        await message.channel.send("넹?")
    if message.content == "바보":
        await message.channel.send("실망했어요!")
    if message.content.startswith("ㅅㅂ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 ㅅㅂ욕설은 금지입니다")
    if message.content.startswith("ㅂㅅ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 ㅂㅅ욕설은 금지입니다")
    if message.content.startswith("ㅄ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 ㅄ욕설은 금지입니다")
    if message.content.startswith("병신"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 병신욕설은 금지입니다")
    if message.content.startswith("시발"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 시발욕설은 금지입니다")
    if message.content.startswith("씨발"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 씨발욕설은 금지입니다")
    if message.content.startswith("ㅆㅂ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 ㅆㅂ욕설은 금지입니다")
    if message.content.startswith("tq"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 tq욕설은 금지입니다")
    if message.content.startswith("TQ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 TQ욕설은 금지입니다")
    if message.content.startswith("QT"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 QT욕설은 금지입니다")
    if message.content.startswith("TQ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 TQ욕설은 금지입니다")
    if message.content.startswith("ㅅㅂㄴ"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 ㅅㅂㄴ욕설은 금지입니다")
    if message.content.startswith("시발년"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 시발년욕설은 금지입니다")
    if message.content.startswith("씨발년"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 씨발련욕설은 금지입니다")
    if message.content.startswith("tqs"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 tqs욕설은 금지입니다")
    if message.content.startswith("TQS"):
        ch = app.get_channel(837232418515320862)
        await ch.send (f"{message.author.mention}님 TQS욕설은 금지입니다")
    if message.content.startswith("!Twitch"):
        embed = discord.Embed(title="https://www.twitch.tv/aekeu_apple     애크님이 운영하시는 트위치 채널입니다. 한번씩 들어오셔서 팔로워 눌러주세요.", description="와! 정말 유익한걸?", color=0x00ff00)
        embed.set_footer(text="와! 이건 눌러야 겠는걸?")
        await message.channel.send(embed=embed)
    
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
    
    if message.content.startswith("!clear"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)

    if message.content.startswith("!투표"):
        await message.delete()
        vote = message.content[4:].split("/")
        await message.channel.send("투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('✔')
    
    if message.content.startswith("!vote"):
        await message.delete()
        vote = message.content[4:].split("/")
        await message.channel.send("vote - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('✔')

@app.command(name="추방", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다.")

@app.command()
async def 들어와(ctx):
    global vc
    vc = await ctx.message.author.voice.channel.connect()

app.run(token)