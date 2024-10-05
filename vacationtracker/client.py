# import discord
# import re

# from collections import defaultdict
# from typing import override

# from discord.ext import tasks

# class SpendingClient(discord.Client):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # @override
    # async def setup_hook(self) -> None:
    #     self.read_spending.start()

    # @tasks.loop(seconds=10)
    # async def read_spending(self):
    #     print(dict(get_spending(self.get_channel(self.CHANNEL_ID))))

    # @read_spending.before_loop
    # async def before_read_spending(self):
    #     await self.wait_until_ready()
