# Imports
import sys
import os
import discord
import database.config as config
# Vars
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
defprefix = config.con['prefixs'][0]
prefixes = config.con['prefixs']
CommandFolder = config.CommandFolder
# Functions
def cls():
    '''#### Konsol Ekranını Temizler.'''
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def restartBot():
    '''#### Bota 'Restart' Atar.'''
    cls()
    os.system('python '+os.path.basename(sys.argv[0]))
def unite(list, op):
    '''#### `join()` Fonksiyonun Daha Basitleştirilmiş Halidir.'''
    text = op.join(list)
    return text
# Index
@client.event
async def on_ready():
    activity = discord.Activity(name = config.con["status"], type = config.con["statusgame"])
    await client.change_presence(status = discord.Status.online, activity = activity)
    print("I'm Ready")
@client.event
async def on_message(message):
    prefix = defprefix
    for p in prefixes:
        if message.content.lower().startswith(p):
            prefix = p
    args = message.content.split(' ')
    async def replytxt(msg):
        '''#### Mesajı Yazı Olarak Yanıtlar.'''
        await message.reply(msg, mention_author = True)
    if message.author.id == client.user.id:
        return
    direc = CommandFolder
    dire = os.listdir(os.getcwd()+f"\\{direc}")
    for f in set(dire):
        if ".py" in f:
            filel = f.replace(".py", "")
            m = __import__(direc+"."+filel, fromlist=[''])
            for i in m.cmd:
                if message.content.lower().startswith(prefix+i):
                    await m.run(client, message, args)
client.run(config.con['token'])
