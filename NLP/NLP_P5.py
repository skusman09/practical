"""
NLP Practical 5 - Corrected Code
"""

import nltk
from nltk.corpus import wordnet as wn

# Ensure the 'wordnet' corpus is downloaded
nltk.download('wordnet')

# ---------------- Section a: WordNet Dictionary Exploration ----------------

# Exploring synsets, definitions, examples, and lemmas
print("Synsets for 'motorcar':", wn.synsets('motorcar'))

print("\nLemma names for 'car.n.01':", wn.synset('car.n.01').lemma_names())
print("Examples for 'car.n.01':", wn.synset('car.n.01').examples())
print("Definition for 'car.n.01':", wn.synset('car.n.01').definition())
print("Definition for 'fruit.n.01':", wn.synset('fruit.n.01').definition())
print("Definition for 'cartoon.n.01':", wn.synset('cartoon.n.01').definition())
print("Definition for 'bike.n.01':", wn.synset('bike.n.01').definition())
print("Definition for 'animal.n.01':", wn.synset('animal.n.01').definition())

# Exploring lemmas
print("\nLemmas for 'fruit.n.01':", wn.synset('fruit.n.01').lemmas())
print("Lemma for 'car.n.01.automobile':", wn.lemma('car.n.01.automobile'))
print("Synset for lemma 'car.n.01.automobile':", wn.lemma('car.n.01.automobile').synset())
print("Lemma name for 'car.n.01.automobile':", wn.lemma('car.n.01.automobile').name())
print("Lemmas for 'car':", wn.lemmas('car'))

# Printing lemma names for each synset of 'car'
print("\nSynonym sets for 'car':")
for synset in wn.synsets('car'):
    print(synset.lemma_names())


# ---------------- Section b: Hyponyms, Hypernyms, Meronyms, and Entailments ----------------

motorcar = wn.synset('car.n.01')
print("\nMotorcar synset:", motorcar)

# Hyponyms (more specific instances)
types_of_motorcar = motorcar.hyponyms()
print("Number of hyponyms for motorcar:", len(types_of_motorcar))
if len(types_of_motorcar) > 8:
    print("Hyponym example (index 8):", types_of_motorcar[8])
else:
    print("Less than 9 hyponyms available.")

# Hypernyms (more general classes)
print("Hypernyms for motorcar:", motorcar.hypernyms())

# Hypernym paths
paths = motorcar.hypernym_paths()
print("Number of hypernym paths for motorcar:", len(paths))
if len(paths) > 0:
    print("First hypernym path:", [syn.name() for syn in paths[0]])
if len(paths) > 1:
    print("Second hypernym path:", [syn.name() for syn in paths[1]])

# Root hypernyms
print("Root hypernyms for motorcar:", motorcar.root_hypernyms())

# Meronyms and entailments
print("Part meronyms of 'tree.n.01':", wn.synset('tree.n.01').part_meronyms())
print("Substance meronyms of 'tree.n.01':", wn.synset('tree.n.01').substance_meronyms())
print("Entailments of 'walk.v.01':", wn.synset('walk.v.01').entailments())
print("Entailments of 'eat.v.01':", wn.synset('eat.v.01').entailments())

# Antonyms
print("Antonyms for 'supply' (noun):", wn.lemma('supply.n.02.supply').antonyms())
print("Antonyms for 'rush' (verb):", wn.lemma('rush.v.01.rush').antonyms())
print("Antonyms for 'horizontal' (adjective):", wn.lemma('horizontal.a.01.horizontal').antonyms())


# ---------------- Section c: Finding Synonyms and Antonyms ----------------

from nltk.corpus import wordnet
print("\nSynsets for 'active':", wordnet.synsets("active"))
print("Antonyms for 'active.a.01.active':", wn.lemma('active.a.01.active').antonyms())