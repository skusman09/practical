
################  8A  ##################
import nltk
from nltk import tokenize
nltk.download('punkt')
from nltk import tag
from nltk import chunk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
para = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
sents = tokenize.sent_tokenize(para)
print("\nSentence tokenization\n============\n",sents)
# Word tokenization
print("\nWord tokenization\n============\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
# POS Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
print("\nPOS tagging\n============\n",tagged_words)
# Chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
print("\nChunking\n============\n",tree)


################  8B  ##################
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
doc = nlp(text)
print("Noun Phrases: ", [chunk.text for chunk in doc.noun_chunks])
print("Verbs: ", [token.lemma_ for token in doc if token.pos_ == "VERB"])


################  8C  ##################
import nltk
nltk.download('treebank')
from nltk.corpus import treebank_chunk
treebank_chunk.tagged_sents()[0]
treebank_chunk.chunked_sents()[0]
treebank_chunk.chunked_sents()[0].draw()