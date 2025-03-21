# Handling Stop words.
# 1. Adding or removing stop words in NLTKs Default stop word list.
# 2. Using gensim adding and removing stop words in Default gensim stop word list.
# 3. Using spacy adding and removing stop words in Default spacy stop word list.



### 3.) Using spacy adding and removing stop words in Default spacy stop word list.

import spacy
import nltk
from nltk.tokenize import word_tokenize
sp = spacy.load("en_core_web_sm")
all_stopwords = sp.Defaults.stop_words
all_stopwords.add("play")

text = "yasesh likes to play football, however he is not too fond of tennis"
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)

# remove 'not' from word collection

all_stopwords.remove('not')
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)