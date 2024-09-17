import discord
from discord.ext import commands
from vacationtracker import THREAD_ID, intents

import re
import uuid
import pathlib
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Match
from functools import total_ordering

import numpy as np 
import matplotlib.pyplot as plt 

from tabulate import tabulate

bot = commands.Bot(command_prefix='?', intents=intents)

@dataclass
@total_ordering
class Spending:
    total: float = 0
    payments: dict[datetime, float] = field(default_factory=dict)

    def __eq__(self, other):
        return self.total == other.total
    
    def __lt__(self, other):
        return self.total > other.total
    
    def __repr__(self):
        formatted_payments = {date.strftime('%m/%d/%Y'): f"${amt:.2f}" for date, amt in self.payments.items()}
        return f"{self.__class__.__name__}<Total=${self.total}, Payments={formatted_payments}>"

def get_new_spending(txt: str) -> Match[str] | None:
    if r'!excepted' in txt:
        return None

    return re.search('\$(\d+(?:\.\d+)?)', txt)

def create_graph(d: dict[str, Spending]) -> uuid.UUID:
    for name, spending in d.items():
        x = []
        y = []
        for date, amount in sorted(spending.payments.items(), reverse=True):
            x.append(date.strftime('%m/%d'))
            y.append(amount)

        plt.plot(np.array(x), np.array(y), marker='o', label=name)

    graph_id = uuid.uuid4()

    plt.title("Spending over time")
    plt.xlabel("Date")
    plt.ylabel("Amount (in $)")
    plt.ylim(ymin=0)
    plt.legend(loc='upper right')
    plt.grid()
    plt.savefig(f"{graph_id}.png")
    plt.close()

    return graph_id

def create_ranking(d: dict[str, Spending]) -> str:
    rankings = []
    rank = 1
    for name, spending in sorted(d.items(), key=lambda item: item[1]):
        rankings.append([rank, name, f"${spending.total:.2f}"])
        rank += 1
    
    if rankings:
        return f"```{tabulate(rankings, headers=['Rank', 'Name', 'Total'], tablefmt='orgtbl')}```"
    else:
        return f"```No money spend yet!```"

@bot.command(name='spending')
async def calculate_spending(ctx, output_form=None):
    channel = ctx.message.channel
    if not channel:
        raise Exception('Channel not found!')

    d = defaultdict(Spending)

    async for message in channel.history():
        if message.author.bot or not (m := get_new_spending(message.content)):
            continue

        traveller = message.author.display_name or message.author.global_name or "Unknown"
        spending = d[traveller]
        amount = float(m.group(1))
        date = message.edited_at.date() if message.edited_at else message.created_at.date()

        if date in spending.payments:
            spending.payments[date] += amount
        else:
            spending.payments[date] = amount

        spending.total += amount
    
    if __debug__:
        print(dict(d))

    match output_form:
        case 'simple':
            await ctx.send(dict(d))
        case 'graph':
            graph_name = f"{create_graph(d)}.png"
            await ctx.send(file=discord.File(graph_name))
            pathlib.Path(graph_name).unlink(missing_ok=True)
        case 'table' | _:
            await ctx.send(create_ranking(d))
