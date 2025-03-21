# Import the gTTS module for text-to-speech
from gtts import gTTS  

# This module is imported so that we can play the converted audio  
from playsound import playsound

"""
If playsound is not downloading,
install it according to your specific Python version.
You can use GPT for guidance.
This applies to all situations where a package fails to download.
"""

# It is a text value that we want to convert to audio  
text_val = 'You are studying Natural Language Processing. Better speak in English'  

# Here we are converting in English Language  
language = 'en'  

# Passing the text and language to the engine, setting high speed  
obj = gTTS(text=text_val, lang=language, slow=False)  

# Saving the transformed audio in a mp3 file named exam.mp3  
obj.save("exam.mp3")  

# Play the exam.mp3 file  
playsound("exam.mp3")