# Study of hyponyms, hypernyms, meronyms and entailments.

motorcar = wn.synset('car.n.01') 
motorcar

types_of_motorcar = motorcar.hyponyms() 
types_of_motorcar

types_of_motorcar[8]

motorcar.hypernyms()

paths = motorcar.hypernym_paths()
len(paths)

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
