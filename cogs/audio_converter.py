import os
import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from pydub import AudioSegment
from config import GUILD_ID


async def download_file(url: str, file_name: str, extension: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(f"{file_name}.{extension}", 'wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)
            return f"{file_name}.{extension}"


class AudioConverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="convert_audio",
        description="Convert audio file to a different format",
        guild_ids=[GUILD_ID]
    )
    async def _convert_audio(self, interaction: Interaction, file_url: str, output_format: str):
        try:
            # Detect the input format
            input_format = os.path.splitext(file_url)[-1].lstrip(".")

            # Download the input file
            input_file_name = "input_audio"  # You can generate a unique file name using uuid if needed
            await download_file(file_url, input_file_name, input_format)

            # Convert the file
            # Convert the file
            print(f"Input file path: {input_file_name}.{input_format}")  # Add this line to print the input file path
            audio = AudioSegment.from_file(f"{input_file_name}.{input_format}", format=input_format)
            output_file_name = f"output_audio.{output_format}"
            audio.export(output_file_name, format=output_format)

            # Upload the converted file
            with open(output_file_name, "rb") as file:
                await interaction.response.send_message(file=nextcord.File(file, f"converted_audio.{output_format}"))

            # Cleanup
            os.remove(f"{input_file_name}.{input_format}")
            os.remove(output_file_name)
        except Exception as e:
            await interaction.response.send_message(f"Error converting file: {str(e)}")


def setup(bot):
    bot.add_cog(AudioConverter(bot))
