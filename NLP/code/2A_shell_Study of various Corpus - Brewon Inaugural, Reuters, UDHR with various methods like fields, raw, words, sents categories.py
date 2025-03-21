# a. Study of various Corpus - Brown, Inaugural, Reuters, UDHR 
# with various methods like fileids, raw, words, sents, categories.

# Brown Corpus
import nltk
from nltk.corpus import brown
brown.categories()
brown.words()
brown.words(categories='news')
brown.words(categories='adventure')
brown.words(categories='government')
brown.raw()
brown.fileids()
brown.words(fileids=['cg22'])
brown.sents()

# Reuters Corpus
from nltk.corpus import reuters
reuters.categories()
reuters.words()
reuters.sents()
reuters.raw()
reuters.fileids()
reuters.fileids(['corn'])
print(reuters.words('training/9865')[:14])
print(reuters.words('training/9865')[:3])

# Inaugural Corpus
from nltk.corpus import inaugural
inaugural.words()
inaugural.sents()
inaugural.raw()
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]

# UDHR Corpus
from nltk.corpus import udhr
udhr.words()
udhr.sents()
udhr.raw()
udhr.fileids()