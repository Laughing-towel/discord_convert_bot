import os
import aiohttp
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from PIL import Image
from config import GUILD_ID


async def download_file(url: str, file_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open(file_name, 'wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)
            return file_name


class ImageConverter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="convert_image",
        description="Convert image file to a different format",
        guild_ids=[GUILD_ID]
    )
    async def _convert_image(self, interaction: Interaction, file_url: str, output_format: str):
        try:
            # Download the input file
            input_file_name = "input_image"  # You can generate a unique file name using uuid if needed
            await download_file(file_url, input_file_name)

            # Open the image
            input_image = Image.open(input_file_name)

            # Convert the image if necessary
            if input_image.mode == "RGBA" and output_format.lower() == "jpeg":
                input_image = input_image.convert("RGB")

            # Save the image in the desired format
            output_file_name = f"output_image.{output_format}"
            input_image.save(output_file_name, format=output_format.upper())

            # Upload the converted file
            with open(output_file_name, "rb") as file:
                await interaction.response.send_message(file=nextcord.File(file, f"converted_image.{output_format}"))

            # Cleanup
            os.remove(input_file_name)
            os.remove(output_file_name)
        except Exception as e:
            await interaction.response.send_message(f"Error converting file: {str(e)}")


def setup(bot):
    bot.add_cog(ImageConverter(bot))
