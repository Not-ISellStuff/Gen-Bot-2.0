import json, discord, os
from discord.ext import commands
from discord import Intents

def cls():
    os.system('cls')
cls()

with open('token.json', 'r') as file:
    data = json.load(file)
    token = data['token']
    channel = data['gen_channel_id']


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix=',')
client.remove_command('help')

#########################
# Developer: ISellStuff #
#########################

#########################
######  Commands  ####### 
#########################

@client.command()
async def help(ctx):
    embed = discord.Embed(
    title="Commands",color=discord.Color.blue())
    
    embed.add_field(name=",stock", value="Shows all available accounts")
    embed.add_field(name=",gen <account>", value="Sends an account to your dms")
    embed.add_field(name=",info", value="Shows info about the bot")

    await ctx.send(embed=embed)

@client.command()
async def stock(ctx):
    embed = discord.Embed(
    title="Stock",color=discord.Color.blue())

    for filename in os.listdir("Stock"):
        file_path = os.path.join("Stock", filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                accounts = file.readlines()
                lines = len(accounts)
                name, _ = os.path.splitext(filename)
                embed.add_field(name=f"**{name}**", value=lines)

    await ctx.send(embed=embed)

@client.command()
async def gen(ctx, acc):
    if int(ctx.channel.id) == int(channel):
        
        try:
            with open(f"Stock/{acc}.txt", "r") as f:
                pass
            ##########################
            try:

                with open(f"Stock/{acc}.txt", "r") as f:
                    account = f.readline()
                
                if account == "":
                    embed = discord.Embed(
                    title="Error",description=f"We are out of {acc} accounts.",color=discord.Color.red())
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                    title=f"Here is your {acc} account.",color=discord.Color.blue())
                    embed.add_field(name="Account", value=f"{account}")
                    
                    await ctx.author.send(embed=embed)
                    ###############################
                    av = ctx.author.avatar
                    embed = discord.Embed(
                        title="Sent Account To Your Dms.",
                        description=f"Generated by {ctx.author.mention}",
                        color=discord.Color.blue(),
                    )
                    embed.set_thumbnail(url=av)
                    await ctx.send(embed=embed)

                    with open(f"Stock/{acc}.txt", "r+") as f:
                        lines = f.readlines()
                        f.seek(0)  
                        f.writelines(lines[1:]) 
                        f.truncate()

            except:
                embed = discord.Embed(
                title=f"Error.",color=discord.Color.red(), description="Your Dms Are Off")
                await ctx.send(embed=embed)
    
            ##########################
        except:
            embed = discord.Embed(
            title="Error",description=f"There are no {acc} accounts.",color=discord.Color.red())
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
        title="Error",description=f"This command only works in <#{channel}> only.",color=discord.Color.red())
        await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(
    title="Info",description=("""
** Developer: ISellStuff **

** This bot is for storing rewards like accounts, gift cards, and other stuff**\n**people can use the gen command to get an item/reward from stock**\n\n**In token.json you can add your token and the channel id you want the bot to work in only**                       
"""),color=discord.Color.blue())

    await ctx.send(embed=embed)


#########################
client.run(token)
