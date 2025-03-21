# Handling Stop words.
# 1. Adding or removing stop words in NLTKs Default stop word list.
# 2. Using gensim adding and removing stop words in Default gensim stop word list.
# 3. Using spacy adding and removing stop words in Default spacy stop word list.


#### 1.) Adding or removing stop words in NLTKS default stop word list
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
print(stopwords.words())

text = "yashesh likes to play football, however he is not to fond of tennis"
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw)

all_stopwords = stopwords.words('english')
all_stopwords.append('play')

text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)

all_stopwords.remove('not')
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
