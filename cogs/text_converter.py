import os
import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from config import GUILD_ID


class TextConverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="convert_text",
        description="Convert text file to a different format",
        guild_ids=[GUILD_ID]
    )
    async def _convert_text(self, interaction: Interaction, file_url: str, output_format: str):
        try:
            # Download the input file
            async with aiohttp.ClientSession() as session:
                async with session.get(file_url) as response:
                    input_text = await response.text()

            # Save the converted file
            output_file_name = f"converted_text.{output_format}"
            with open(output_file_name, "w", encoding="utf-8") as output_file:
                output_file.write(input_text)

            # Upload the converted file
            with open(output_file_name, "rb") as file:
                await interaction.response.send_message(file=nextcord.File(file, f"converted_text.{output_format}"))

            # Cleanup
            os.remove(output_file_name)

        except Exception as e:
            await interaction.response.send_message(f"Error converting file: {str(e)}")


def setup(bot):
    bot.add_cog(TextConverter(bot))
