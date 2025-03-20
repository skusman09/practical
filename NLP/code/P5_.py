# Study of wordnet dictionary with methods such as synsets, definitions, examples and lemmas.

import nltk

from nltk.corpus import wordnet as wn wn.synsets('motorcar')

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

for synset in wn.synsets('car'): print(synset.lemma_names())

# Study of hyponyms, hypernyms, meronyms and entailments.

motorcar = wn.synset('car.n.01') motorcar

types_of_motorcar = motorcar.hyponyms() types_of_motorcar

types_of_motorcar[8]

motorcar.hypernyms()

paths = motorcar.hypernym_paths() len(paths)

[synset.name for synset in paths[0]]

[synset.name for synset in paths[1]]

motorcar.root_hypernyms()

wn.synset('tree.n.01').part_meronyms()

wn.synset('tree.n.01').substance_meronyms()

wn.synset('walk.v.01').entailments()

wn.synset('eat.v.01').entailments()

wn.lemma('supply.n.02.supply').antonyms()

wn.lemma('rush.v.01.rush').antonyms()

wn.lemma('horizontal.a.01.horizontal').antonyms()

# Write a program using python to find synonyms and antonyms.

from nltk.corpus import wordnet print(wordnet.synsets("active"))

print(wn.lemma('active.a.01.active').antonyms())