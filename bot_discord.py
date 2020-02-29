import discord
from discord.ext import commands
from time import *
from token import Part_bilet


bot = commands.Bot(command_prefix = '!')


emojis = {
'wtf' : '<:emoji_9:681485164609929218>',
'fuck_you' : '<:emoji_8:681481825272725562>',
'no_fuck_you' : '<:emoji_7:681476030258741289>',
'mmm' : '<:emoji_6:675406943103483904>',
'mmm_full' : '<:emoji_5:675388729661325332>',
'peka' : '<:peka:681832106489675823>',
'pled' : '<:Pled:674196648519532574>',
'cool_peka' : '<:Pled:674196648519532574>',
'peka_chudo' : '<:peka_chudo:674205087337414676>'
}


@bot.command(pass_context=True) #разрешаем передавать агрументы
async def emoji(ctx, arg):
    await ctx.send(emojis[arg])

@bot.command(pass_context=True) #разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент
    print(arg)

bot.run(Part_bilet)
