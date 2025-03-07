#P7

###############   7A   ################
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
data = text.split()
for i in data:
    print(i)


##############  7B  ###################
import nltk
from nltk.tokenize import RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps = True)
str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
tokens = tk.tokenize(str)
print(tokens)


################  7C  ##################
import nltk
from nltk.tokenize import word_tokenize
str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print(word_tokenize(str))


################  7D  ##################
import spacy
nlp = spacy.blank("en")
str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
doc = nlp(str)
words = [word.text for word in doc]
print(words)


################  7E  ##################
import tensorflow
import keras
from tensorflow.keras.preprocessing.text import text_to_word_sequence
str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
tokens = text_to_word_sequence(str)
print(tokens)
