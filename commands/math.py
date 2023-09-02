cmd=['math', 'matematik', 'işlem']
info="Math command."
usage="math <1.float> <operator +,-,/,*> <2.float>"
async def run(client, message, args):
    try:
        async def math(message, args):
            if args[2] == '+':
                return float(args[1]) + float(args[3])
            elif args[2] == '-':
                return float(args[1]) - float(args[3])
            elif args[2] == '/':
                return float(args[1]) / float(args[3])
            elif args[2] == '%':
                return float(args[1]) % float(args[3])
            elif args[2] == '*':
                return float(args[1]) * float(args[3])
            elif args[2] == '//':
                return float(args[1]) // float(args[3])
            elif args[2] == '**':
                return float(args[1]) ** float(args[3])
        await message.reply(f"**Cevap ;** `{float(await math(message, args))}`", mention_author=True)
    except ZeroDivisionError:
        await message.reply("Bir Sayıyı 0'a Bölemezsin!", mention_author=True)
    except ValueError:
        await message.reply("Sayı Yerine Yazı Yazamazsın!", mention_author=True)
    except TypeError:
        await message.reply("`+`**/**`-`**/**`/`**/**`%`**/**`*`**/**`//`**/**`**` Karakterlerinden Birini Kullanmalısınız", mention_author=True)
    except IndexError:
        await message.reply('Birşeyler Eksik!', mention_author=True)
    except:
        await message.reply('Hata Oluştu!', mention_author=True)
