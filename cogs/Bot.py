from discord.ext import commands, tasks, menus
import discord, random , time, asyncio, difflib, typing
from discord.ext.commands.cooldowns import BucketType
from discord.ext.menus.views import ViewMenuPages

class Bot(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.status_task.start()

  @tasks.loop(seconds=40)
  async def status_task(self):
    await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Testing Bot of JDJG of WIP discord.py versions"))
    await asyncio.sleep(40)
    await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.guilds)} servers | {len(self.bot.users)} users"))
    await asyncio.sleep(40)
    await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Epic stuff is coming soon to JDBot."))
    await asyncio.sleep(40)

  @status_task.before_loop
  async def before_status_task(self):
    await self.bot.wait_until_ready()

  def cog_unload(self):
    self.status_task.stop()
  

  @commands.command(brief="gives you who the owner is.")
  async def owner(self, ctx):
    info = await self.bot.application_info()
    owner_id = info.team.owner_id if info.team else info.owner.id

    support_guild=self.bot.get_guild(438848185008390158)
    owner= await self.bot.getch_member(support_guild,owner_id)
    user_type = user_type = ['User', 'Bot'][owner.bot]

    guilds_list=[guild for guild in self.bot.guilds if guild.get_member(owner.id) and guild.get_member(ctx.author.id)]
    if not guilds_list:
      guild_list = "None"


    if guilds_list:
      guild_list= ", ".join(map(str, guilds_list))
    
    if owner:
      nickname = str(owner.nick)
      joined_guild = owner.joined_at.strftime('%m/%d/%Y %H:%M:%S')
      status = str(owner.status).upper()
      highest_role = owner.roles[-1]
    
    if owner is None:
      nickname = "None"
      joined_guild = "N/A"
      status = "Unknown"
      for guild in self.bot.guilds:
        member=guild.get_member(owner.id)
        if member:
          status=str(member.status).upper()
          break
      highest_role = "None Found"
    
    embed=discord.Embed(title=f"Bot Owner: {owner}",description=f"Type: {user_type}", color=random.randint(0, 16777215),timestamp=ctx.message.created_at)
    embed.add_field(name="Username:", value = owner.name)
    embed.add_field(name="Discriminator:",value=owner.discriminator)
    embed.add_field(name="Nickname: ", value = nickname)
    embed.add_field(name="Joined Discord: ",value = (owner.created_at.strftime('%m/%d/%Y %H:%M:%S')))
    embed.add_field(name="Joined Guild: ",value = joined_guild)
    embed.add_field(name="Mutual Guilds:", value=guild_list)
    embed.add_field(name="ID:",value=owner.id)
    embed.add_field(name="Status:",value=status)
    embed.add_field(name="Highest Role:",value=highest_role)
    embed.set_image(url=owner.avatar.url)
    await ctx.send(embed=embed)

  @commands.command(brief = "about the bot")
  async def about(self, ctx):
    await ctx.send('this bot is meant to test out new features of discord.py(from beta) and also new features in general and I want to be able to test them in discord.py, so I can get cricistim amd such.')

  @commands.command(brief = "ask a command to be ported from JDBot")
  async def port_command(self, ctx, *, args = None):
    if not args:
      return await ctx.send("You need to give me the command name not empty.")

    if args:
      jdjg = await self.bot.getch_user(168422909482762240)
      await jdjg.send(f"{ctx.author} wants {args}")
  

def setup(bot):
  bot.add_cog(Bot(bot))