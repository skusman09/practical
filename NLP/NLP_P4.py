"""
NLP Practical 4 - Corrected Code
"""

# ---------------- Section a: Mapping Words to Properties ----------------

# Creating a dictionary to map words to their properties
pos = {}
print("Initial dictionary:", pos)

# Adding word-property mappings
pos['colorless'] = 'ADJ'
pos['ideas'] = 'N'
pos['sleep'] = 'v'
pos['furiously'] = 'ADV'

print("Updated dictionary:", pos)
print("Access 'ideas':", pos['ideas'])
print("Access 'colorless':", pos['colorless'])

# Listing keys and sorted keys
print("List of keys:", list(pos))
print("Sorted keys:", sorted(pos))
print("Keys ending with 's':", [w for w in pos if w.endswith('s')])

# Iterating over sorted keys to display key-value pairs
print("\nDictionary items (sorted):")
for word in sorted(pos):
    print(word + ":", pos[word])

# Showing dictionary keys and items
print("\nKeys:", pos.keys())
print("Items:", pos.items())

# Changing the value of 'sleep' to a list of properties
pos['sleep'] = ['N', 'V']
print("After updating 'sleep':", pos.items())

# Alternatively, reassigning the entire dictionary
pos = {'colorless': 'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
print("Final dictionary:", pos)


# ---------------- Section b: Tagging with Default, Regex, and Unigram Taggers ----------------

import nltk
from nltk.corpus import brown

# Ensure the 'brown' corpus is downloaded
nltk.download('brown')

# Fetching Brown corpus tagged sentences and raw sentences (news category)
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

# Default Tagger: Tags every token as 'NN'
raw_text = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw_text)
default_tagger = nltk.DefaultTagger('NN')
print("\nDefault Tagger Output:", default_tagger.tag(tokens))
print("Default Tagger Evaluation:", default_tagger.evaluate(brown_tagged_sents))

# Regex Tagger: Use regular expressions to tag tokens based on patterns
patterns = [
    (r'.*ing$', 'VBG'),   # gerunds
    (r'.*ed$', 'VBD'),     # simple past
    (r'.*es$', 'VBZ'),     # 3rd singular present
    (r'.*ould$', 'MD'),    # modals
    (r'.*\'s$', 'NN$'),    # possessive nouns
    (r'.*s$', 'NNS'),      # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')         # default: nouns
]
regexp_tagger = nltk.RegexpTagger(patterns)
print("\nRegex Tagger Output (sample sentence):", regexp_tagger.tag(brown_sents[3]))
print("Regex Tagger Evaluation:", regexp_tagger.evaluate(brown_tagged_sents))

# Unigram Tagger: Uses the most frequent tag for each word from the training data
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
# Using a sentence from the corpus to tag
print("\nUnigram Tagger Output (sample sentence):", unigram_tagger.tag(brown_sents[2007]))
print("Unigram Tagger Evaluation:", unigram_tagger.evaluate(brown_tagged_sents))