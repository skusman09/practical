import speech_recognition as sr
filename = "E://4911_MScIT Part 2//NLP//Practical 1//male.wav"

#initialize the recognizer
r = sr.Recognizer()

#open the file
with sr.AudioFile(filename) as source:
    #listen for the data (load audio into memory)
    audio_data = r.record(source)
    #recognize (convert from speech into text)
    text = r.recognize_google(audio_data)
    print(text)
