# Create and use your own corpora.

import nltk

from nltk.corpus import PlaintextCorpusReader corpus_root = 'D:\MSc.IT'

wordlists = PlaintextCorpusReader(corpus_root, '.*') wordlists.fileids()

wordlists.words("funny.txt")


# Study of tagged corpora with methods like tagged_sents, tagged_words.

import nltk nltk.corpus.brown.tagged_words()
nltk.corpus.brown.tagged_sents()
nltk.corpus.conll2000.tagged_words()
nltk.corpus.conll2000.tagged_sents()
nltk.corpus.treebank.tagged_words()
nltk.corpus.treebank.tagged_sents()


# c.Write a program to find the most frequent noun tags.

wsj = nltk.corpus.treebank.tagged_words() word_tag_fd = nltk.FreqDist(wsj)
[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('N')]