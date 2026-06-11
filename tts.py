from supertonic import TTS

# First run downloads model automatically (~400-500MB download)
tts = TTS(auto_download=True)

# Choose a voice (M1-M5 for male, F1-F5 for female)
style = tts.get_voice_style(voice_name="M1")

# Generate speech
text = "Hello, this is high-quality, local text-to-speech."
wav, duration = tts.synthesize(text, voice_style=style, lang="en")

# Save to file
tts.save_audio(wav, "output.wav")
print(f"Generated {duration:.2f} seconds of audio")