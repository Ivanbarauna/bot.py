import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from Controller.modulo import create_embed, gallery_embed
from configparser import ConfigParser
# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
#puxar os links do .env
LINK_GOD = os.getenv("LINK_GOD")
LINK_FIFA = os.getenv("LINK_FIFA")
LINK_Forza = os.getenv("LINK_Forza")
LINK_Farming_simulator25 = os.getenv("LINK_Farming_simulator25")
LINK_TEKKEN8 = os.getenv("LINK_TEKKEN8")
LINK_SPARKING = os.getenv("LINK_SPARKING")
LINK_XENOVERSE = os.getenv("LINK_XENOVERSE")

# Carregar o token do arquivo .env
token = os.getenv("DISCORD_TOKEN")
prefix = os.getenv("DISCORD_PREFIX")
welcome_chanel_id = int(os.getenv("WELCOME"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Bot conectado como {bot.user}') 
    
    # Comando de barra para enviar link do god of war
@bot.tree.command()
async def god(interaction: discord.Interaction):
    embed, file = create_embed(
        "God of War",
        "Link para baixar o jogo God of War",
        "01",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_GOD, style=discord.ButtonStyle.primary))
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command()
async def fifa23(interaction: discord.Interaction):
    embed, file = create_embed(
        "FIFA 23",
        "Link para baixar o jogo FIFA 23",
        "02",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_FIFA, style=discord.ButtonStyle.primary))
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command()
async def forza(interaction: discord.Interaction):
    embed, file = create_embed(
        "Forza Horizon 5",
        "Link para baixar o jogo Forza Horizon 5",
        "03",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_Forza , style=discord.ButtonStyle.primary))
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command()
async def farming25(interaction: discord.Interaction):
    embed, file = create_embed(
        "Farming Simulator 25",
        "Link para baixar o jogo Farming Simulator 25",
        "04",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_Farming_simulator25, style=discord.ButtonStyle.primary))
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command()    
async def tekken8(interaction: discord.Interaction):
    embed, file = create_embed(
        "Tekken 8",
        "Link para baixar o jogo Tekken 8",
        "05",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_TEKKEN8, style=discord.ButtonStyle.primary))  
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command()
async def xenoverse2(interaction: discord.Interaction):
    embed, file = create_embed(
        "Dragon Ball Xenoverse 2",
        "Link para baixar o jogo Dragon Ball Xenoverse 2",
        "06",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_XENOVERSE, style=discord.ButtonStyle.primary))
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


@bot.tree.command()
async def sparking0(interaction: discord.Interaction):
    embed, file = create_embed(
        "Dragon Ball Sparking ZERO",
        "Link para baixar o jogo Dragon Ball Sparking ZERO",
        "07",
        discord.Color.blue()
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Download", url=LINK_SPARKING, style=discord.ButtonStyle.primary))
    if file:
        await interaction.response.send_message(embed=embed, file=file, view=view, ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


# iniciar o bor
bot.run(token)