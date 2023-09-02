cmd=["ping"]
info="Pong! olarak yanıtlaar işte."
usage="ping"
import discord
async def run(client, message, args):
    await message.reply("Pong!", mention_author = True)