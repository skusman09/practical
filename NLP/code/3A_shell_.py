# Create and use your own corpora.
import nltk
from nltk.corpus import PlaintextCorpusReader corpus_root = 'D:\MSc.IT'
wordlists = PlaintextCorpusReader(corpus_root, '.*') wordlists.fileids()
wordlists.words("funny.txt")
