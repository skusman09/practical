"""
NLP Practical 1 - Corrected Code
"""

# ---------------- Section a: Import NLTK ----------------

import nltk

# Download required datasets (optional UI will open)
# Run this manually if needed
# nltk.download()

# Import Brown corpus and display some words
from nltk.corpus import brown
nltk.download('brown')

print("Sample words from Brown corpus:", brown.words()[:20])

# ---------------- Section b: Convert Speech to Text ----------------

import speech_recognition as sr

filename = "D://MSc.IT//sem_4//NLP//NLP_practical//NLP_prac_codes//female.wav"  # Update with a valid path

# Initialize the recognizer
r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        # Listen for the data (load audio into memory)
        audio_data = r.record(source)
        # Recognize (convert from speech into text)
        text = r.recognize_google(audio_data)
        print("Converted Text:", text)
except FileNotFoundError:
    print("Error: Audio file not found.")

# ---------------- Section c: Convert Text to Speech ----------------

# Import the gTTS module for text-to-speech
from gtts import gTTS
from playsound import playsound

text_val = 'You are studying Natural Language Processing. Better Speak in English'

# Convert text to speech
language = 'en'
tts = gTTS(text=text_val, lang=language, slow=False)

# Save and play the audio
tts.save("exam.mp3")
playsound("exam.mp3")

print("Audio file 'exam.mp3' generated and played successfully.")
