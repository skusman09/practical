"""
NLP Practical 2 - Corrected Code
"""

import nltk
import matplotlib.pyplot as plt

# ---------------- Section a: Study of Various Corpora ----------------

# Download required corpora
nltk.download('brown')
nltk.download('reuters')
nltk.download('inaugural')
nltk.download('udhr')

from nltk.corpus import brown, reuters, inaugural, udhr

# Brown corpus examples
print("Brown Corpus Categories:", brown.categories())
print("Words in Brown (news category):", brown.words(categories='news')[:20])

# Reuters corpus examples
print("Reuters Categories:", reuters.categories())
print("Words in Reuters (first file):", reuters.words(reuters.fileids()[0])[:20])

# Inaugural corpus examples
print("First 10 words in inaugural speech:", inaugural.words()[:10])

# UDHR corpus examples
print("First 10 words in UDHR corpus:", udhr.words()[:10])

# ---------------- Section b: Conditional Frequency Distribution ----------------

# Brown corpus Conditional Frequency Distribution
cfd = nltk.ConditionalFreqDist(
    (genre, word.lower()) 
    for genre in brown.categories() 
    for word in brown.words(categories=genre)
)

genres = ['news', 'hobbies', 'science_fiction', 'romance']
modals = ['can', 'could']

print("Conditional Frequency Distribution Table:")
cfd.tabulate(conditions=genres, samples=modals)

# Reuters corpus Conditional Frequency Distribution
cfd_reuters = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in reuters.fileids()
    for w in reuters.words(fileid)
    for target in ['barley', 'corn']
    if w.lower().startswith(target)
)

cfd_reuters.plot()
plt.show()

# Inaugural corpus Conditional Frequency Distribution
cfd_inaugural = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)

cfd_inaugural.plot()
plt.show()

# UDHR corpus Conditional Frequency Distribution
languages = ['Chickasaw', 'English', 'German_Deutsch']
cfd_udhr = nltk.ConditionalFreqDist(
     (lang, len(word))
     for lang in languages
     for word in udhr.words(lang+'-Latin1')
)

cfd_udhr.plot(cumulative=True)
plt.show()
