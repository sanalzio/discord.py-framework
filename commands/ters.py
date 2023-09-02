cmd=['tersyaz',"ters"]
info="Belirttiğiniz yazıyı tersine çevirir"
usage="tersyaz <yazı>"
async def run(client, message, args):
    try:
        if str(" ".join(args[1:])).find('enoyreve@') != -1 or str(" ".join(args[1:])).find('ereh@') != -1:
            await message.reply('Herkezi Etiketlemem İçin Herhangi Bir Sebep Yok!', mention_author=True)
        else:
            string=" ".join(args[1:])
            await message.reply(string[::-1], mention_author=True)
    except IndexError:
        await message.reply('Birşeyler Eksik!', mention_author=True)
    except:
        await message.reply('Hata Oluştu!', mention_author=True)
