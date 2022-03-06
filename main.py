import os, traceback, logging
import BotConfig
import dotenv

logging.basicConfig(level=logging.INFO)

bot = BotConfig.bot

dotenv.load_dotenv()

bot.run(os.environ["TOKEN"])
