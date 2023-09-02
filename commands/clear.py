cmd=["clear","temizle"]
info="Clear Command."
usage="clear <integer>"
async def run(client, message, args):
    if message.author.guild_permissions.administrator:
        try:
            if int(args[1]) > 100 or int(args[1]) < 2:
                await message.reply('**2** İle **100** Arasında Bir Değer Girmelisiniz!', mention_author=True)
            else:
                await message.channel.purge(limit=int(args[1])+1)
        except:
            await message.reply('Belirttiğin Yada **Belirtmediğin** Şeyin **Sayı** Olduğundan Emin Misin?', mention_author=True)
    else:
        await message.reply('Sen Bir Admin Değilsin!', mention_author=True)
