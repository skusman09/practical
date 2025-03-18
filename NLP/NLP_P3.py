"""
NLP Practical 3 - Corrected Code
"""

# ---------------- Section a: Create and Use Your Own Corpora ----------------

import nltk
from nltk.corpus import PlaintextCorpusReader

# Ensure the path exists and contains text files
corpus_root = r"D:\MSc.IT"  # Update with a valid path
wordlists = PlaintextCorpusReader(corpus_root, '.*')

print("Files in Corpus:", wordlists.fileids())

# Ensure the file exists in the corpus directory
try:
    print("Words in funny.txt:", wordlists.words("funny.txt"))
except FileNotFoundError:
    print("Error: 'funny.txt' not found in the specified directory.")

# ---------------- Section b: Study of Tagged Corpora ----------------

import nltk

# Download required corpora if not already installed
nltk.download('brown')
nltk.download('conll2000')
nltk.download('treebank')

# Fetch and display tagged corpora
print("Brown Tagged Words:", nltk.corpus.brown.tagged_words()[:10])
print("Brown Tagged Sentences:", nltk.corpus.brown.tagged_sents()[:2])
print("CONLL2000 Tagged Words:", nltk.corpus.conll2000.tagged_words()[:10])
print("CONLL2000 Tagged Sentences:", nltk.corpus.conll2000.tagged_sents()[:2])
print("Treebank Tagged Words:", nltk.corpus.treebank.tagged_words()[:10])
print("Treebank Tagged Sentences:", nltk.corpus.treebank.tagged_sents()[:2])

# ---------------- Section c: Find the Most Frequent Noun Tags ----------------

import nltk

# Ensure treebank corpus is available
nltk.download('treebank')

wsj = nltk.corpus.treebank.tagged_words()

# Fix: Extract only tags from (word, tag) pairs
word_tag_fd = nltk.FreqDist(tag for (_, tag) in wsj)

# Get the most common noun-related tags
noun_tags = [tag for tag in word_tag_fd if tag.startswith('N')]
most_common_nouns = [(tag, word_tag_fd[tag]) for tag in noun_tags]

print("Most Common Noun Tags:", sorted(most_common_nouns, key=lambda x: x[1], reverse=True)[:10])
