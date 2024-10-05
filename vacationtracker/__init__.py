from typing import Final

THREAD_ID: Final[int] = 1285410720321638410

from dotenv import load_dotenv

load_dotenv()
 
from discord import Intents

intents = Intents.default()
intents.members = True
intents.message_content = True

# from client import SpendingClient

# client = SpendingClient(intents=intents)
# client.run(os.environ['BOT_KEY'])

from vacationtracker.bot import bot
import os

bot.run(os.environ['BOT_KEY'])
