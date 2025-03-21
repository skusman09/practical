# Write a program using python to find synonyms and antonyms.
from nltk.corpus import wordnet as wn
print(wn.synsets("active"))
print(wn.lemma('active.a.01.active').antonyms())