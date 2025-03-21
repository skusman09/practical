# Study of wordnet dictionary with methods such as synsets, definitions, examples and lemmas.

import nltk
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()
wn.synset('car.n.01').examples()
wn.synset('car.n.01').definition()
wn.synset('fruit.n.01').definition()
wn.synset('cartoon.n.01').definition()
wn.synset('bike.n.01').definition()
wn.synset('animal.n.01').definition()
wn.synset('fruit.n.01').lemmas
wn.lemma('car.n.01.automobile')
wn.lemma('car.n.01.automobile').synset()
wn.lemma('car.n.01.automobile').name()
wn.lemmas('car')
for synset in wn.synsets('car'): 
    print(synset.lemma_names())
