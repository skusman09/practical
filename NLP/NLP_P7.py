"""
NLP Practical 7 - Corrected Code
"""

import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
import spacy
from tensorflow.keras.preprocessing.text import text_to_word_sequence

# Ensure required NLTK resources are downloaded
nltk.download('punkt')

# ---------------- Section a: Text Tokenization using Python split() ----------------

text = "This tool is on beta stage."
data = text.split()

print("Tokenized words using split():", data)

# ---------------- Section b: Text Tokenization using Python Regex ----------------

tk = RegexpTokenizer(r'\s+', gaps=True)  # Use raw string (r'\s+')
tokens = tk.tokenize(text)

print("Tokenized words using Regex:", tokens)

# ---------------- Section c: Text Tokenization using NLTK ----------------

tokens_nltk = word_tokenize(text)
print("Tokenized words using NLTK:", tokens_nltk)

# ---------------- Section d: Text Tokenization using SpaCy ----------------

nlp = spacy.blank("en")
doc = nlp(text)
tokens_spacy = [word.text for word in doc]

print("Tokenized words using SpaCy:", tokens_spacy)

# ---------------- Section e: Text Tokenization using Keras ----------------

tokens_keras = text_to_word_sequence(text)
print("Tokenized words using Keras:", tokens_keras)
