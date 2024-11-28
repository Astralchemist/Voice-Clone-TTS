import requests
import pygame
import tempfile
import os
import time
import hashlib
import threading
import io
import sounddevice as sd
import itertools

# Configuration
ELEVEN_LABS_API_KEY = "your api key"
VOICE_ID = "your voice id "

temp_dir = tempfile.gettempdir()
loading = False

def generate_tts(text):
    """Generate TTS using Eleven Labs API."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.85, "similarity_boost": 1.0}
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def play_audio(audio_data):
    """Play audio using Pygame."""
    try:
        pygame.mixer.init()
        audio = io.BytesIO(audio_data)
        pygame.mixer.music.load(audio, 'mp3')
        pygame.mixer.music.play()
        
        # Non-blocking playback
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"Error during audio playback: {e}")
    finally:
        pygame.mixer.quit()

def get_cache_path(text):
    """Generate a unique file path for the cached TTS audio."""
    hash_value = hashlib.md5(text.encode()).hexdigest()
    return os.path.join(temp_dir, f"{hash_value}.mp3")

def generate_and_cache_tts(text):
    """Generate and cache TTS audio."""
    cache_path = get_cache_path(text)
    if os.path.exists(cache_path):
        print("Using cached TTS audio.")
        with open(cache_path, "rb") as f:
            return f.read()

    print("Generating new TTS audio...")
    audio_data = generate_tts(text)
    if audio_data:
        with open(cache_path, "wb") as f:
            f.write(audio_data)
    return audio_data

def show_loading_message():
    """Show loading animation while generating TTS."""
    for char in itertools.cycle('|/-\\'):
        if not loading:
            break
        print(f"\rGenerating TTS... {char}", end="")
        time.sleep(0.1)

def main():
    """Main function to interact with the user and handle TTS generation and playback."""
    print("TTS Google Meet Integration")
    print("Type your text to generate and play audio. Type 'exit' to quit.")
    
    while True:
        text = input("\nEnter text: ").strip()
        if not text:
            print("No text entered. Please try again.")
            continue
        if text.lower() == "exit":
            print("Exiting program. Goodbye!")
            break

        # Start loading animation in a separate thread
        global loading
        loading = True
        thread = threading.Thread(target=show_loading_message)
        thread.start()

        # Generate and play TTS audio
        audio_data = generate_and_cache_tts(text)
        loading = False
        thread.join()  # Wait until the loading message finishes

        if audio_data:
            play_thread = threading.Thread(target=play_audio, args=(audio_data,))
            play_thread.start()
        else:
            print("Failed to generate TTS. Please check your input or API configuration.")

if __name__ == "__main__":
    main()
