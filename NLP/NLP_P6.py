"""
NLP Practical 6 - Corrected Code
"""

import nltk
from nltk.corpus import wordnet

# ---------------- Section a: Path Similarity Between Two Nouns ----------------

# Ensure the 'wordnet' corpus is downloaded
nltk.download('wordnet')

# Define words to compare
syn1 = wordnet.synsets('football')
syn2 = wordnet.synsets('soccer')

# Compute path similarity
for s1 in syn1:
    for s2 in syn2:
        print("Path similarity of:")
        print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')
        print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
        print("Similarity Score:", s1.path_similarity(s2))
        print()

# ---------------- Section b: Handling Stop Words ----------------

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure stopwords are downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Original text
text = "Yashesh likes to play football, however he is not too fond of tennis"

# Remove default stop words
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if word.lower() not in stopwords.words('english')]
print("Tokens without stop words (NLTK):", tokens_without_sw)

# Adding custom stop words
all_stopwords = stopwords.words('english')
all_stopwords.append('play')

tokens_without_sw = [word for word in text_tokens if word.lower() not in all_stopwords]
print("After adding 'play' as stopword:", tokens_without_sw)

# Removing 'not' from stopwords
all_stopwords.remove('not')
tokens_without_sw = [word for word in text_tokens if word.lower() not in all_stopwords]
print("After removing 'not' from stopwords:", tokens_without_sw)

# ---------------- Handling Stop Words Using Gensim ----------------

import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS

# Removing stop words using gensim
filtered_sentence = remove_stopwords(text)
print("Tokens without stop words (Gensim):", filtered_sentence)

# Custom stopwords in Gensim
custom_stopwords = STOPWORDS.union(set(['likes', 'play']))
tokens_without_sw = [word for word in text_tokens if word.lower() not in custom_stopwords]
print("After adding 'likes' and 'play' as stopwords:", tokens_without_sw)

# Removing 'not' from Gensim stop words
custom_stopwords = STOPWORDS.difference({'not'})
tokens_without_sw = [word for word in text_tokens if word.lower() not in custom_stopwords]
print("After removing 'not' from stopwords (Gensim):", tokens_without_sw)

# ---------------- Handling Stop Words Using SpaCy ----------------

import spacy

# Load English language model
sp = spacy.load("en_core_web_sm")
all_stopwords = sp.Defaults.stop_words

# Adding and removing stopwords in SpaCy
all_stopwords.add("play")
tokens_without_sw = [word for word in text_tokens if word.lower() not in all_stopwords]
print("After adding 'play' as stopword (SpaCy):", tokens_without_sw)

all_stopwords.remove("not")
tokens_without_sw = [word for word in text_tokens if word.lower() not in all_stopwords]
print("After removing 'not' from stopwords (SpaCy):", tokens_without_sw)
