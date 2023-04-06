import nextcord
from nextcord.ext import commands
import config

intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)


# Load cogs (extensions)
for cog in ("audio_converter", "image_converter", "text_converter"):
    bot.load_extension(f"cogs.{cog}")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")


bot.run(config.TOKEN)
