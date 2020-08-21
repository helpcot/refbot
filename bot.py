import os
import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
import random as r
import random
import json
import requests

prefix = "/"
client = commands.Bot(command_prefix=prefix)



@client.event
async def on_ready(*args):
    print ( 'Бот Подключён!Можно работать.' )

@client.command()
async def av(ctx, member : discord.Member = None):
    
	user = ctx.message.author if (member == None) else member

	embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x00FF00)

	embed.set_image(url=user.avatar_url)

	await ctx.channel.purge( limit = 1 )
	await ctx.send(embed=embed)



@client.command()
@commands.has_permissions( administrator = True)
async def ban(ctx, member : discord.Member=None, *, reason=None):
	await ctx.channel.purge( limit = 1 )

	if ctx.author.top_role.position <= member.top_role.position:
			return await ctx.author.send(embed = discord.Embed(description = f'**:shield: Я не буду банить человека который выше тебя по должности!**', color=0x0c0c0c)) 


	elif member is None:
			await ctx.author.send(embed = discord.Embed(description = f'**:shield: Введите пользователя**', color=0x0c0c0c)) 

	elif reason is None:
			await ctx.author.send(embed = discord.Embed(description = f'**:shield: Введите причину**', color=0x0c0c0c)) 

	else:
			emb = discord.Embed(
				title='✅ Кик', 
				description= f'**Кикнут участник: {member.mention} \n По причине {reason}**',
				colour=0xf20a0a
			)
			emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')

			await member.ban(reason=reason)
			await ctx.send(embed=emb)




@client.command()
@commands.has_permissions( administrator = True)
async def kick(ctx, member : discord.Member=None, *, reason=None):
   
   await ctx.channel.purge( limit = 1 )
        
   
   if ctx.author.top_role.position <= member.top_role.position:
       
       return await ctx.author.send(embed = discord.Embed(description = f'**:shield: Я не буду кикать человека который выше тебя по должности!**', color=0x0c0c0c)) 


   
   elif member is None:
       
       await ctx.author.send(embed = discord.Embed(description = f'**:shield: Введите пользователя**', color=0x0c0c0c)) 

   
   elif reason is None:
       
       await ctx.author.send(embed = discord.Embed(description = f'**:shield: Введите причину**', color=0x0c0c0c)) 

   
   else:
       
       emb = discord.Embed(
           
           title='✅ Кик', 
           
           description= f'**Кикнут участник: {member.mention} \n По причине {reason}**',
           
           colour=0xf20a0a
       
       )
       
       emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')

       
       await member.kick(reason=reason)
       
       await ctx.send(embed=emb)


@client.command( pass_context = True, aliases=[ "Мут", "мут", "мьют", "Мьют", "mute" ] )
@commands.has_permissions( administrator = True)
async def tempmute(ctx, member : discord.Member, time:int, arg:str, *, reason=None):

	Переменная_размут = f'**Вы были размучены на сервере {ctx.guild.name}**'
	Переменная_мут = f'**Вы были замучены на сервере {ctx.guild.name} на {time}{arg} по причине: {reason}**'
	mute_role = discord.utils.get( ctx.message.guild.roles, id = 742408970483925102 )

	await member.add_roles(mute_role, reason=None, atomic=True)

	emb = discord.Embed(
		title='✅ Мут', 
		description= f'**Замучен участник: {member.mention} \n По причине {reason} \n На время {time}{arg}**',
		colour=0xf20a0a,
		timestamp=ctx.message.created_at
	)
	emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/689879530542071952/711588305506140241/verdict.png?width=407&height=407')
	await ctx.send(embed=emb)
	await member.send(embed = discord.Embed(description = f'{Переменная_мут}', color=0x0c0c0c))

	if arg == "s":
		await asyncio.sleep(time)          
	elif arg == "m":
		await asyncio.sleep(time * 60)
	elif arg == "h":
		await asyncio.sleep(time * 60 * 60)
	elif arg == "d":
		await asyncio.sleep(time * 60 * 60 * 24)
	elif arg == "y":
		await asyncio.sleep(time * 60 * 60 * 24 * 365)
	elif arg == "v":
		await asyncio.sleep(time * 60 * 60 * 24 * 365 * 100)


	await member.remove_roles( mute_role )
	await member.send(embed = discord.Embed(description = f'{Переменная_размут}', color=0x800080))




@client.command()
async def server(ctx):
	r = requests.get(f'https://mcapi.us/server/status?ip=95.217.92.207&port=25626')
	data = r.json()['players']['now']
	datas = r.json()['players']['max']
	datasa = r.json()['motd']
	datasaa = r.json()['online']
	datasaaa = r.json()['server']['name']
	embed=discord.Embed(title="Статистика о серверах", color=0x00FF00)
	embed.set_thumbnail(url="https://media.discordapp.net/attachments/742105991243628594/744952187280425080/ReflectionCrat.png")
	embed.add_field(name=f"Статистика", value=f"Онлайн: {data}/{datas}", inline=False)
	embed.set_footer(text=f"{datasa}\nОнлайн :{datasaa}")
	await ctx.send(embed=embed)
    
    
token = os.environ.get('BOT_TOKEN') # Получаем токен с heroku который ты указывал в настройках
client.run(str(token)) # запускаем бота