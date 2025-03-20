# Text Tokenization using python split().

text = "this tool is on beta stage." data = text.split()

for i in data: print (i)

# Text Tokenization using python Regex.

import nltk

from nltk.tokenize import RegexpTokenizer

tk = RegexpTokenizer(r'\s+', gaps=True) # Use raw string (r'\s+') text = "this tool is on beta stage."

tokens = tk.tokenize(text) print(tokens)

# Text Tokenization using python NLTK.

import nltk

from nltk.tokenize import word_tokenize str = "this tool is on beta stage." print(word_tokenize(str))

# Text Tokenization using spacy library.

# NOTE: code in colab import spacy

nlp = spacy.blank("en")

str = "this tool is on beta stage." doc = nlp(str)

words = [word.text for word in doc] print(words)

# Text Tokenization using Keras.

import tensorflow import keras

from tensorflow.keras.preprocessing.text import text_to_word_sequence str = "this tool is on beta stage."

tokens = text_to_word_sequence(str) print(tokens)