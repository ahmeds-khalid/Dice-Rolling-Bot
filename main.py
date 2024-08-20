import nextcord
from nextcord.ext import commands
from nextcord.ui import view
from nextcord import Interaction
import os
import random
import webserver

client = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("Dice Roller is ready to use!!")

@client.slash_command(name="roll", description="Roll a standard six-sided die", guild_ids=[1173218609682731038])
async def test(interaction: Interaction):
    embed = nextcord.Embed(title='Dice Roll Results', color=0xffffff)  # You can customize the color
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

    # Add information to the embed
    embed.set_image(url)
    embed.add_field(name='Result:', value= rand, inline=False)
    embed.add_field(name='User:', value=interaction.user.mention, inline=False)

    # Send the embed as a message
    await interaction.response.send_message(embed=embed)

#UI

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.danger)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Confirming", ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Cancelling", ephemeral=True)
        self.value = False
        self.stop()

@client.command()
async def ask(ctx):
    view = Confirm()
    await ctx.send("Do you want to confirm somthing.", view=view)

    await view.wait()

    if not view.value == None:
        print("Timed Out")
    if view.value == True:
        print("Confirmed")
    if view.value == False:
        print("Cancelled")

webserver.keep_alive()
client.run("MTE4NzA2OTY5Mjc4Mzg5ODc4Ng.GXsjMo.6psVZpCk1HJo_XImhjoNsiRQ-vcLXY2ddZ0BAM")
