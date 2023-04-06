
# Discord File Converter Bot

This Discord bot allows users to convert audio, image, and text files to different formats using slash commands. The bot currently supports the following conversions:

- Audio: MP3, WAV, OGG, and FLAC
- Image: JPEG, PNG, and GIF
- Text: TXT, PDF, and DOCX

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `config.py` file in the root directory of the project with the following content:

   ```python
   TOKEN = "YOUR_BOT_TOKEN"
   GUILD_ID = YOUR_GUILD_ID
   ```

   Replace `YOUR_BOT_TOKEN` with your Discord bot token and `YOUR_GUILD_ID` with your server's guild ID.

4. Run the bot:

   ```bash
   python main.py
   ```

## Usage

The bot provides three slash commands for converting files:

1. `/convert_audio`: Converts an audio file to a different format.

   Example usage:

   ```
   /convert_audio file_url=https://example.com/song.mp3 output_format=wav
   ```

2. `/convert_image`: Converts an image file to a different format.

   Example usage:

   ```
   /convert_image file_url=https://example.com/image.png output_format=jpeg
   ```

3. `/convert_text`: Converts a text file to a different format.

   Example usage:

   ```
   /convert_text file_url=https://example.com/document.txt output_format=pdf
   ```

Please note that the bot requires appropriate permissions to send messages and upload files in the server.

## Contributing

Feel free to open issues and submit pull requests to add new features or improve existing functionality. Please follow the existing coding style and conventions when submitting code changes.

## License

This project is licensed under the MIT License. 