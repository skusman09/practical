# Study Default Tagger, Regular Expression tagger, Unigram Tagger
#default_tagger import nltk

from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

tags = [tag for (word, tag) in brown.tagged_words(categories='news')] 
nltk.FreqDist(tags).max()

raw = 'I do not like green eggs and ham, I do not like them Sam I am!' 
tokens = nltk.word_tokenize(raw)

default_tagger = nltk.DefaultTagger('NN') 
default_tagger.tag(tokens)

default_tagger.evaluate(brown_tagged_sents)


#regex_tagger import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news') 
brown_sents = brown.sents(categories='news')

patterns = [

(r'.*ing$', 'VBG'), # gerunds

(r'.*ed$', 'VBD'), # simple past (r'.*es$', 'VBZ'), # 3rd singular present (r'.*ould$', 'MD'), # modals

(r'.*\'s$', 'NN$'), # possessive nouns (r'.*s$', 'NNS'), # plural nouns

(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers (r'.*', 'NN') # nouns (default)

]

regexp_tagger = nltk.RegexpTagger(patterns) 
regexp_tagger.tag(brown_sents[3])

regexp_tagger.evaluate(brown_tagged_sents)

#unigram_tagger import nltk

from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news') 
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) 
unigram_tagger.tag(brown_sents[2007])

unigram_tagger.evaluate(brown_tagged_sents)