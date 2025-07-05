# Step1a: Setup Text to Speech – TTS – model with gTTS
import os
import platform
import subprocess
from gtts import gTTS

# Step1b: Setup Text to Speech – TTS – model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

# Set your ElevenLabs API key
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_gtts(input_text, output_filepath, autoplay=False):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    if autoplay:
        _play_audio(output_filepath)

def text_to_speech_with_elevenlabs(input_text, output_filepath, autoplay=False):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Alice",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

    if autoplay:
        _play_audio(output_filepath)

def _play_audio(filepath):
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['ffplay', '-nodisp', '-autoexit', filepath])
        elif os_name == "Linux":
            subprocess.run(['aplay', filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# For manual test
if __name__ == "_main_":
    input_text = "Hi, this is Doctor Wahhaj speaking to you for voice testing."
    text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3", autoplay=True)