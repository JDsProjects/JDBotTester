import contextlib, aiohttp, re, discord, os, traceback
from discord.ext import commands


async def get_prefix(bot, message):
    extras = ["test+", "te+", "t+"]
    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))
    return commands.when_mentioned_or(*extras)(bot, message)


class JDBotTester(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.special_access = {}

    async def start(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()
        await super().start(*args, **kwargs)

    async def close(self):
        await self.session.close()
        await super().close()

    async def getch_member(self, guild, member_id):
        member = None
        with contextlib.suppress(discord.Forbidden, discord.HTTPException):
            member = guild.get_member(member_id) or await guild.fetch_member(member_id)
        return member

    async def getch_user(self, user_id):
        user = None

        with contextlib.suppress(discord.NotFound, discord.HTTPException):
            user = self.get_user(user_id) or await self.fetch_user(user_id)
        return user


bot = JDBotTester(command_prefix=(get_prefix), intents=discord.Intents.all(), strip_after_prefix=True)

bot.load_extension("jishaku")


@bot.event
async def on_error(event, *args, **kwargs):
    more_information = os.sys.exc_info()
    error_wanted = traceback.format_exc()
    traceback.print_exc()
    # print(more_information[0])


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")
        except commands.errors.ExtensionError:
            traceback.print_exc()
