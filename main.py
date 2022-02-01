import  os, traceback, logging
import B, BotConfig
import dotenv

logging.basicConfig(level = logging.INFO)

bot = BotConfig.bot

B.b()
dotenv.load_dotenv()

bot.run(os.environ["TOKEN"])
