Here’s the content for your `README.md` file that you can upload directly to GitHub:

```markdown
# Eleven Labs API Integration

This project integrates Eleven Labs API to generate text-to-speech (TTS) from user-provided text, cache the audio, and play it back using Pygame and SoundDevice libraries. It also incorporates the use of VB-Cables for virtual audio routing, allowing the TTS output to be routed through virtual audio devices.

## Features
- Generates TTS from text input using the Eleven Labs API.
- Caches generated TTS audio files to avoid re-generating the same audio.
- Plays audio using Pygame and SoundDevice.
- Allows audio output routing through VB-Cables for virtual audio devices.
- Command-line interface for easy interaction.

## Installation

To get started, clone the repository and install the required dependencies.

### Step 1: Clone the Repository
First, clone the repository from GitHub:

```bash
git clone https://github.com/astralchemist/elevenlabs-api-integration.git
```

### Step 2: Install Dependencies
Navigate to the project directory and install the required Python packages using `pip`:

```bash
cd elevenlabs-api-integration
pip install -r requirements.txt
```

Ensure you have Python 3.6+ installed.

### Step 3: Install VB-Cables
To use virtual audio routing, you need to install [VB-Cables](https://vb-audio.com/Cable/). Download and install the software according to the instructions on their website.

### Step 4: Configure API Key and Voice ID
You will need to replace the placeholder for `ELEVEN_LABS_API_KEY` in the script with your own API key from Eleven Labs. Follow the instructions on the Eleven Labs API documentation to create an account and get your API key.

```python
ELEVEN_LABS_API_KEY = "your_api_key"
```

Also, replace the `VOICE_ID` variable with the voice ID you want to use for TTS.

### Step 5: Run the Program
After setting up the API key and voice ID, you can start the program with:

```bash
python elevenlabs_api_integration.py
```

The program will prompt you to enter text. Once you input the text, it will generate the TTS, cache the audio, and play it.

### Commands:
- **Enter text**: Converts the input text into speech and plays it.
- **Type `exit`**: Exits the program.

## Project Structure

```bash
elevenlabs-api-integration/
├── elevenlabs_api_integration.py   # Main Python script
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation
```

## Dependencies

- `requests`: For making HTTP requests to the Eleven Labs API.
- `pygame`: For playing the generated TTS audio.
- `sounddevice`: For additional audio playback functionality.
- `itertools`: For showing a loading animation while processing the TTS request.
- `hashlib`: For creating a unique cache path based on the text input.
- **VB-Cables**: For routing audio output to virtual audio devices.

## Troubleshooting

- If you encounter issues with audio playback, ensure that the `pygame` and `sounddevice` libraries are correctly installed and configured on your machine.
- Ensure that VB-Cables are correctly configured for audio routing. You may need to configure the input/output audio devices in your system or audio software.
- Double-check that your Eleven Labs API key and voice ID are correctly set up.
- If you see `Failed to generate TTS`, check your internet connection or API configuration.

## Contribution
Feel free to fork the repository and submit pull requests. Contributions are welcome!


