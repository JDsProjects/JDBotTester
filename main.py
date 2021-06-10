import  os, traceback, logging
import B, BotConfig

logging.basicConfig(level=logging.INFO)

bot = BotConfig.bot

B.b()
bot.run(os.environ["TOKEN"])