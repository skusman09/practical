#NLP_6B_3

import spacy
import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
sp = spacy.load('en_core_web_sm')
all_stopwords = sp.Defaults.stop_words
all_stopwords.add("play")
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
all_stopwords.remove('not')
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)