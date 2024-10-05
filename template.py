from typing import Final

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# The bot command has the format <command_prefix><command_name>. The current command
# prefix is the question mark (?), but you can feel free to change it here to whatever
# character you like.
bot = commands.Bot(command_prefix='?', intents=intents)

# Replace <command_name> with the name of your command.
@bot.command(name='<command_name>')
# Optional: Specify any additional parameters after the "ctx" in the following function signature.
# Each function parameter corresponds to a parameter in your bot command.
async def run_command(ctx):
    # Get the message that triggered the execution of the bot command.
    bot_msg = ctx.message
    if not bot_msg:
        raise Exception
    
    # Get the channel where the message was sent. From here, you can retrieve various
    # channel info, such as all its messages, member info, etc.
    channel = ctx.channel
    if not channel:
        raise Exception

    # Get each message in the channel.
    async for channel_msg in channel.history():
        # Get the actual content of the message. USE THIS VARIABLE TO READ THE MESSAGE.
        content = channel_msg.content

        poll = channel_msg.poll
        reactions = channel_msg.reactions
        stickers = channel_msg.stickers

        # Get the user who sent the channel message.
        author = channel_msg.author
        print(author)

        avatar = author.avatar
        bot = author.bot
        display_name = author.display_name
        global_name = author.global_name
        name = author.name
        joined_at = author.joined_at
        status = author.status

        # Write code here to do whatever you want to do with the message.
        ...

        # Replace <placeholder> with your favorite emoji.
        emoji = "<placeholder>"
        await channel_msg.add_reaction(emoji)

        thread_name = "<placeholder>"
        await channel_msg.create_thread(thread_name)

        reply_content = None
        await channel_msg.reply(reply_content)

        await channel_msg.end_poll()

        await channel_msg.pin()

    # Replace <placeholder> with the message you want the bot to send back to
    # the Discord channel.
    await ctx.send("<placeholder>")

    # Replace <placeholder> with the name of the file you want the bot to
    # send back to the Discord channel.
    await ctx.send(file=discord.File("<placeholder>"))


BOT_ID: Final[str] = 0 # replace with your bot id
bot.run(BOT_ID)
