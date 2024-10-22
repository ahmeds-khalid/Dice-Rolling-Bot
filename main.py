import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os
import random
import webserver

client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("Dice Roller is ready to use!!")

@client.slash_command(name="roll", description="Roll a standard six-sided die", guild_ids=[1173218609682731038])
async def roll(interaction: Interaction):
    embed = nextcord.Embed(title='Dice Roll Results', color=0xffffff)
    rand = random.randint(1, 6)
    if rand == 1:
        url="https://i.postimg.cc/TYyFymxQ/dice1.png"
    elif rand == 2:
        url="https://i.postimg.cc/52QXkPVv/dice2.png"
    elif rand == 3:
        url="https://i.postimg.cc/QMLFLp8z/dice3.png"
    elif rand == 4:
        url="https://i.postimg.cc/B64tb41c/dice4.png"
    elif rand == 5:
        url="https://i.postimg.cc/769hTd3v/dice5.png"
    elif rand == 6:
        url="https://i.postimg.cc/0jHNVSXc/dice6.png"

    embed.set_image(url)
    embed.add_field(name='Result:', value=rand, inline=False)
    embed.add_field(name='User:', value=interaction.user.mention, inline=False)

    await interaction.response.send_message(embed=embed)

@client.slash_command(name="flip", description="Flip a coin", guild_ids=[1173218609682731038])
async def flip(interaction: Interaction):
    embed = nextcord.Embed(title='Coin Flip Results', color=0xffffff)
    result = ""
    rand = random.randint(1, 2)
    if rand == 1:
        url="https://i.postimg.cc/63XkhLr1/heads.png"
        result = "Heads"
    elif rand == 2:
        url="https://i.postimg.cc/sD0DJXnC/tails.png"
        result = "Tails"

    embed.set_image(url)
    embed.add_field(name='Result:', value=result, inline=False)
    embed.add_field(name='User:', value=interaction.user.mention, inline=False)

    await interaction.response.send_message(embed=embed)

@client.slash_command(name="custom_roll", description="Roll custom dice", guild_ids=[1173218609682731038])
async def custom_roll(
    interaction: Interaction,
    sides: int = nextcord.SlashOption(description="Number of sides on the die", min_value=2, max_value=100),
    number: int = nextcord.SlashOption(description="Number of dice to roll", min_value=1, max_value=10)
):
    results = [random.randint(1, sides) for _ in range(number)]
    total = sum(results)
    
    embed = nextcord.Embed(title='Custom Dice Roll Results', color=0xffffff)
    embed.add_field(name='Dice:', value=f"{number}d{sides}", inline=False)
    embed.add_field(name='Results:', value=', '.join(map(str, results)), inline=False)
    embed.add_field(name='Total:', value=total, inline=False)
    embed.add_field(name='User:', value=interaction.user.mention, inline=False)

    await interaction.response.send_message(embed=embed)

# webserver.keep_alive()
client.run(Token)
