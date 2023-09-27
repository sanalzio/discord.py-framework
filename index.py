# Imports
import sys
import os
import discord
import modules.PyDB as PyDB
# Vars
## Bot Vars
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
## Config Vars
config = PyDB.pydb("database/config")
prefixes = config.prefixs.split("-")
# Functions
def cls():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def restartBot():
    cls()
    os.system('python '+os.path.basename(sys.argv[0]))
# Index
## On Ready Function
@client.event
async def on_ready():
    activity = discord.Activity(name = config.status, type = eval("discord.ActivityType."+config.ActivityType))
    await client.change_presence(status = discord.Status.online, activity = activity)
    print("I'm Ready")
## On Message Function
@client.event
async def on_message(message):
    prefix = prefixes[0]
    for p in prefixes:
        if message.content.lower().startswith(p):
            prefix = p
    args = message.content.split(' ')
    async def replytxt(msg):
        await message.reply(msg, mention_author = True)
    if message.author.id == client.user.id:
        return
    direc = config.CommandFolder
    dire = os.listdir(os.getcwd()+f"\\{direc}")
    for f in set(dire):
        if ".py" in f:
            filel = f.replace(".py", "")
            m = __import__(direc+"."+filel, fromlist=[''])
            for i in m.cmd:
                if message.content.lower().startswith(prefix+i):
                    await m.run(client, message, args)
# Run Bot
client.run(config.token)