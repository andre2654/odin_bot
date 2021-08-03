import discord
from discord.ext.commands import Bot
from discord import DMChannel
from cryptography.fernet import Fernet
import time
import datetime

now = datetime.datetime.now()
hour = now.hour

key = b'5g_hGQP7Nw8aujB9uBk30mBtBrTXdi4JMKfuulxsoZE='
f = Fernet(key)
token = b'gAAAAABhCa-OXCPq7smOUuCLj6jPrXRLprdi0OItvYVw4MaonsEHteH28vqDhaYPxxd8D_SWCPba9z8Jk4nkxZzkOMSgoYmaXnOJmSwxUS0RvhvWOOBzYsHf2R6L2OLQap1l9eWq2EZm1VAZVFg30cNLEl6rp8dWQQ=='

TOKEN = f.decrypt(token).decode('UTF-8')
GUILD = '854698270148132864'
ANDRE_ID = 397006147263135744
FABIO_ID = 273615496933277696

bot = Bot(command_prefix='$')
#bot = discord.Client()


@bot.command()
async def helpfabio(ctx):

    if hour <= 7 and 'urgente' not in ctx.message.content:
        replyMsg = await ctx.reply('Meu filho, até os deuses precisam dormir um pouco, se quer estudar agora, vá sozinho!!!', mention_author=True)
        time.sleep(20)
        await replyMsg.delete()
        await ctx.message.delete()

    else:
        replyMsg = await ctx.reply('The calculator is comming...', mention_author=True)

        time.sleep(10)
        await replyMsg.delete()
        await ctx.message.delete()

        fabio = await bot.fetch_user(FABIO_ID)
        await DMChannel.send(fabio, f"My son, <@{ctx.author.id}> summoned you at {ctx.message.created_at} <#{ctx.channel.id}>")

        andre = await bot.fetch_user(ANDRE_ID)
        await DMChannel.send(andre, f"My son, <@{ctx.author.id}> summoned you at {ctx.message.created_at} <#{ctx.channel.id}>")

bot.run(TOKEN)
