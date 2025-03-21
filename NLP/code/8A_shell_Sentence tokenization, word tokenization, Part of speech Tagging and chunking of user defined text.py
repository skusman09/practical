# Sentence tokenization, word tokenization, Part of speech Tagging and chunking of user defined text.

import nltk
from nltk import tokenize 
nltk.download('punkt_tab') 
from nltk import tag
from nltk import chunk 
nltk.download('averaged_perceptron_tagger_eng') 
nltk.download('maxent_ne_tagger_tab') 
nltk.download('words')

para = "today you will learn NLTK" 
sents = tokenize.sent_tokenize(para)

print("\nSentence Tokenization\n======\n", sents)

### word tokenization
print("\nword tokenization\n======\n") 
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index]) 
    print(words)


### POS tagging 
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
    print("\nPOS tagging\n======\n", tagged_words)


### chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
    print("\nChunking\n======\n", tagged_words)
    print(tree)
