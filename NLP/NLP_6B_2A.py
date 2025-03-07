import gensim
from gensim.parsing.preprocessing import remove_stopwords
text = "Yashesh likes to play football, however he is not too fond of tennis"
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)

#The following script add likes and play to the list of stop words in Gensim
from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize import word_tokenize

all_stopwords_gensim = STOPWORDS.union(set(['likes', 'plsy']))
text = "Yashesh likes to play football, however he is not too fond of tennis"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)
