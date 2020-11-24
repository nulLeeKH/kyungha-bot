import discord
from discord.ext import commands

from property import discord_prp

# create bot instance
prefix = discord_prp.botname + "야"
bot = commands.Bot(command_prefix=prefix,
                   status=discord.Status.online,
                   activity=discord.Game(prefix + ' 도와줘'),
                   help_command=commands.DefaultHelpCommand(width=69,
                                                            sort_commands=True,
                                                            dm_help=False,
                                                            indent=3,
                                                            commands_heading='Commands:',
                                                            case_insensitive=True,
                                                            no_category='Default'))


# when bot is ready
@bot.event
async def on_ready():
    # print username which logged in
    print(f'logged in as {bot.user}')


# if this scrypt run as __main__
if __name__ == "__main__":
    # load extensions
    exts = discord_prp.extensions
    for ext in exts:
        bot.load_extension(ext)

    # run bot
    tocken = discord_prp.token
    bot.run(tocken)
