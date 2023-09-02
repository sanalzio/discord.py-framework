cmd=['say', 'söyle']
info="Belirttiğiniz mesajı iletir."
usage="say <mesaj>"
async def run(client, message, args):
    if message.author.guild_permissions.administrator:
        try:
            string=" ".join(args[1:])
            await message.delete()
            await message.channel.send(string)
        except IndexError:
            await message.reply('Birşeyler Eksik!', mention_author=True)
        except:
            await message.reply('Hata Oluştu!', mention_author=True)
    else:
        await message.reply('Sen Bir Admin Değilsin!', mention_author=True)