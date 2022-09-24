import logging
import os
import traceback

import dotenv

import BotConfig

logging.basicConfig(level=logging.INFO)

bot = BotConfig.bot

dotenv.load_dotenv()

bot.run(os.environ["TOKEN"])
