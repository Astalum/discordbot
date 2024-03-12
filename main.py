import discord
import config

intents = discord.Intents.all()
client=discord.Client(intents=intents)

# bot起動時に発火
@client.Event
async def on_ready():
    print("Ready!")

# メッセージの検知
@client.event
async def on_message(message):
    # 自身が送信したメッセージには反応しない
    if message.author == client.user:
        return

    # ユーザーからのメンションを受け取った場合、あらかじめ用意された配列からランダムに返信を返す
    if client.user in message.mentions:

        answer = "Hello World!"
        print(answer)
        await message.channel.send(answer)

# Bot起動
client.run(config.DISCORD_TOKEN)