# NLP_6B_2


import nltk
nltk.download('punkt')
nltk.download('punkt_tab') # Download the 'punkt_tab' resource
import gensim
from gensim.parsing.preprocessing import remove_stopwords
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)

from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize import word_tokenize

all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)

from gensim.parsing.preprocessing import STOPWORDS
all_stopwords_gensim = STOPWORDS
sw_list = {"not"}
all_stopwords_gensim = STOPWORDS.difference(sw_list)
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)
from gensim.parsing.preprocessing import remove_stopwords
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)

from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize import word_tokenize

all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)

from gensim.parsing.preprocessing import STOPWORDS
all_stopwords_gensim = STOPWORDS
sw_list = {"not"}
all_stopwords_gensim = STOPWORDS.difference(sw_list)
text = "Shravan likes to play Valorant, however he is not too fond of CS2"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)