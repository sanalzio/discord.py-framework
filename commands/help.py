cmd=['help', '?']
info=""
usage=""
import discord
import os
import database.config as config
async def run(client, message, args):
    CommandFolder = config.CommandFolder
    dp = config.con['prefixs'][0]
    msg = ""
    direc = CommandFolder
    dire = os.listdir(os.getcwd()+f"\\{direc}")
    dirl = set(dire)
    for f in dirl:
        if "help" in f: continue
        if ".py" in f:
            filel = f.replace(".py", "")
            m = __import__(direc+"."+filel, fromlist=[''])
            msg+="**"+dp+m.cmd[0]+"**:   "+m.info+"   Usage: "+dp+m.usage+"\n\n"
    """msg='```\n%help\n\n%clear <sayı>\n\n%math <işlem>\n\n%resim <isim> <limit>\n\n%say <mesaj>\n\n%botasor <soru>\n\n%tersyaz <yazı>\n```'"""
    e=discord.Embed(title=config.con["botname"]+" Commands :", description=msg, colour=config.con["color"])
    await message.channel.send(embed=e)