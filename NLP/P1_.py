
#################***A- Installing NLTK***##############
import nltk
nltk.download()

from nltk.corpus
import brown brown.words()


#############***B- Convert the given speech to text.***#################
import speech_recognition as sr
filename = "D://MSc.IT//sem_4//NLP//NLP_practical//NLP_prac_codes//female.wav"


#initialize the recognizer r = sr.Recognizer()

#open the file
with sr.AudioFile(filename) as source:
#listen for the data (load audio into memory) audio_data = r.record(source)
#recognize (convert from speech into text) text = r.recognize_google(audio_data) print(text)