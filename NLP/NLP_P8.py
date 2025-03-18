"""
NLP Practical 8 - Corrected Code
"""

import nltk
from nltk import tokenize, tag, chunk
import spacy

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# ---------------- Section a: Sentence Tokenization, Word Tokenization, POS Tagging & Chunking ----------------

para = "Today you will learn NLTK."

# Sentence Tokenization
sents = tokenize.sent_tokenize(para)
print("\nSentence Tokenization:\n", sents)

# Word Tokenization
print("\nWord Tokenization:")
for sent in sents:
    words = tokenize.word_tokenize(sent)
    print(words)

# POS Tagging
tagged_words = [tag.pos_tag(tokenize.word_tokenize(sent)) for sent in sents]
print("\nPOS Tagging:\n", tagged_words)

# Chunking
tree = [chunk.ne_chunk(tagged) for tagged in tagged_words]
print("\nChunking:\n", tree)

# ---------------- Section b: Named Entity Recognition using SpaCy ----------------

nlp = spacy.load("en_core_web_sm")
text = "We are writing practical."
doc = nlp(text)

print("\nNamed Entities:")
print("Noun Phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# ---------------- Section c: Named Entity Recognition with Diagram (NLTK Treebank) ----------------

nltk.download('treebank')
from nltk.corpus import treebank_chunk

print("\nFirst tagged sentence from Treebank:", treebank_chunk.tagged_sents()[0])
print("First chunked sentence from Treebank:", treebank_chunk.chunked_sents()[0])

# Uncomment this line to visualize in a GUI (works in Python IDLE, not Colab)
# treebank_chunk.chunked_sents()[0].draw()
