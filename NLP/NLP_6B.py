import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
print(stopwords.words())

text = "Usman Likes to play football"
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print('1.', tokens_without_sw)

all_stopwords = stopwords.words('english')
all_stopwords.append('play')
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print('2.', tokens_without_sw)


all_stopwords.remove('not')
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print('3.', tokens_without_sw)
