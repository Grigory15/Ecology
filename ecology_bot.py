import discord
from discord.ext import commands
import random
import asyncio

fact = ['Около 12% поверхности нашей планеты имеют заповедный статус.','В Тихом океане есть мусорное пятно,'
         'площадь которого достигает 1,5 млн км², что больше площади большинства стран мира.'
         'Течения сносят сюда миллионы тонн мусора ежегодно, и он превратился в подобие мусорного континента.','Более 50% мирового урожая'
         'зерна идёт на корм скоту и на производство биотоплива.','Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок']
command_bot = ['/glass','/facts', '/ecology','/info','/plastic', '/paper','/ecology_problems']
command_description = ['через сколько лет разлагается стекло','интересные факты о экологии','что такое экология',
                       'информация о боте','время разложения пластика','разложение бумаги','экологические проблемы(временно не работает)']
bot = commands.Bot(intents=discord.Intents.all(), command_prefix= "/")

@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send("я бот и помогу тебе узнать о экологии")

@bot.command('помощь')
async def command_help(ctx:commands.Context):
    for i in range(7):
        await ctx.send(i+1)
        await ctx.send(command_bot[i])
        await ctx.send(command_description[i])
        asyncio.sleep(1)

@bot.command('glass')
async def command_info(ctx:commands.Context):
    await ctx.send("стекло разлагается более 1000 лет, поэтому лучше его переробатывать")

@bot.command('facts')
async def command_info(ctx:commands.Context):
    random_fact = random.choice(fact)
    await ctx.send(random_fact)

@bot.command('пластик')
async def command_info(ctx:commands.Context):
    await ctx.send('пластиковые бутылки разлагаются больше 100 лет, а поэлителен 200 лет')

@bot.command('plastic')
async def command_info(ctx:commands.Context):
    await ctx.send('бумага разлагается 2 года')

@bot.command('ecology')
async def command_info(ctx:commands.Context):
    await ctx.send('Эколо́гия (от др.-греч. οἶκος — жилище (дом), местопребывание и λόγος — учение) — естественная наука (раздел биологии)'
                    'о взаимодействиях живых организмов между собой и с их средой обитания, об организации и функционировании биосистем '
                    'различных уровней (популяции, сообщества, экосистемы).')
                    


        


bot.run('')
