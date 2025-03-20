# Sentence tokenization, word tokenization, Part of speech Tagging and chunking of user defined text.

import nltk

from nltk import tokenize nltk.download('punkt_tab') from nltk import tag

from nltk import chunk nltk.download('averaged_perceptron_tagger_eng') nltk.download('maxent_ne_tagger_tab') nltk.download('words')

para = "today you will learn NLTK" sents = tokenize.sent_tokenize(para)

print("\nSentence Tokenization\n======\n", sents)

# word tokenization

print("\nword tokenization\n======\n") for index in range(len(sents)):

words = tokenize.word_tokenize(sents[index]) print(words)

#POS tagging tagged_words = []

for index in range(len(sents)): tagged_words.append(tag.pos_tag(words))

print("\nPOS tagging\n======\n", tagged_words)

#chunking

tree = []

for index in range(len(sents)): tree.append(chunk.ne_chunk(tagged_words[index]))

print("\nChunking\n======\n", tagged_words) print(tree)

# Named Entity Recognition of user defined text .

import spacy

nlp = spacy.load("en_core_web_sm") text = "we are writing practical"

doc = nlp(text)

print("Noun Phrases:", [chunk.text for chunk in doc.noun_chunks]) print("verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Named Entity Recognition with diagram using NLTK corpus - treebank

import nltk nltk.download('treebank')

from nltk.corpus import treebank_chunk treebank_chunk.tagged_sents() [0]

treebank_chunk.chunked_sents() [0] #for Google colab

#treebank_chunk.chunked_sents() [0].pretty_print() #for Idle

treebank_chunk.chunked_sents() [0].draw()