import logging
import os
import traceback

import BotConfig

logging.basicConfig(level=logging.INFO)

bot = BotConfig.bot

bot.run(os.environ["TOKEN"])
