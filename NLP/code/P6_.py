# Compare two nouns and find out path similarity between them.

import nltk

from nltk.corpus import wordnet syn1 = wordnet.synsets('football') syn2 = wordnet.synsets('soccer')

for s1 in syn1: for s2 in syn2:

print("Path similarity of: ")

print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')

print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']') print(" is", s1.path_similarity(s2))

print()

# Handling Stop words.
# Adding or removing stop words in NLTKs Default stop word list.
# Using gensim adding and removing stop words in Default gensim stop word list.
# Using spacy adding and removing stop words in Default spacy stop word list.
#Adding or removing stop words in NLTKs Default stop word list. import nltk

from nltk.corpus import stopwords nltk.download('stopwords')

from nltk.tokenize import word_tokenize print(stopwords.words())

text = "yashesh likes to play football, however he is not to fond of tennis" text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()] print(tokens_without_sw)

all_stopwords = stopwords.words('english') all_stopwords.append('play')

text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] print(tokens_without_sw)

all_stopwords.remove('not') text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] print(tokens_without_sw)

#Using gensim adding and removing stop words in Default gensim stop word list. import nltk

nltk.download('punkt_tab')

import gensim

from gensim.parsing.preprocessing import remove_stopwords

text = "yasesh likes to play football, however he is not too fond of tennis" filtered_sentence = remove_stopwords(text)

print(filtered_sentence)

all_stopwords = gensim.parsing.preprocessing.STOPWORDS print(all_stopwords)

from gensim.parsing.preprocessing import STOPWORDS from nltk.tokenize import word_tokenize

all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))

text = "yasesh likes to play football, however he is not too fond of tennis" text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim] print(tokens_without_sw)

#the following script removes the word "not" from the set of stop words from gensim.parsing.preprocessing import STOPWORDS all_stopwords_gensim = STOPWORDS

sw_list = {"not"}

all_stopwords_gensim = STOPWORDS.difference(sw_list)

text = "yasesh likes to play football, however he is not too fond of tennis" text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim] print(tokens_without_sw)

#Using spacy adding and removing stop words in Default spacy stop word list. import spacy

import nltk

from nltk.tokenize import word_tokenize sp = spacy.load("en_core_web_sm") all_stopwords = sp.Defaults.stop_words all_stopwords.add("play")

text = "yasesh likes to play football, however he is not too fond of tennis" text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] print(tokens_without_sw)

# remove 'not' from word collection all_stopwords.remove('not')

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] print(tokens_without_sw)