import discord
from discord.utils import get
from discord.ext.commands import Bot
from config import BOT_TOKEN, ROLE_NAME, OWNER_ID
import asyncio

bot = Bot("vr.")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the Ship Shop"))
    bot.owner_id=OWNER_ID


@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    if not get(guild.roles, name=ROLE_NAME):
        await guild.create_role(name=ROLE_NAME)
    if not before.channel and after.channel:
        role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
        await member.add_roles(role)
    elif before.channel and not after.channel:
        role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
        await member.remove_roles(role)


@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong! {0}ms'.format(round(bot.latency, 4)*1000))


@bot.command()
async def pong(ctx):
    await ctx.send("🏓 You're doing this wrong!")


bot.run(BOT_TOKEN)

# does not appear to actually log out
print("Exiting process")
asyncio.run(bot.logout())
