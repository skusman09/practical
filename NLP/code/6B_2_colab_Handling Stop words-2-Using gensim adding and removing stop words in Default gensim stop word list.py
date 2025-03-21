# Handling Stop words.
# 1. Adding or removing stop words in NLTKs Default stop word list.
# 2. Using gensim adding and removing stop words in Default gensim stop word list.
# 3. Using spacy adding and removing stop words in Default spacy stop word list.



#### 2.) Using gensim adding and removing stop words in Default gensim stop word list. 

import nltk
nltk.download('punkt_tab')
import gensim
from gensim.parsing.preprocessing import remove_stopwords

text = "yasesh likes to play football, however he is not too fond of tennis"
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS 
print(all_stopwords)
from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize import word_tokenize
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))
text = "yasesh likes to play football, however he is not too fond of tennis"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)

#the following script removes the word "not" from the set of stop words
from gensim.parsing.preprocessing import STOPWORDS 
all_stopwords_gensim = STOPWORDS
sw_list = {"not"}
all_stopwords_gensim = STOPWORDS.difference(sw_list)
text = "yasesh likes to play football, however he is not too fond of tennis"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)
