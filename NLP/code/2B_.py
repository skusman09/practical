# B. Study Conditional Frequency Distribution

# Frequency Distribution of Modals in News Text
news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']

for m in modals:
    print(m + ':', fdist[m])


# Conditional Frequency Distribution across Genres
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

genres = ['news', 'hobbies', 'science_fiction', 'romance']
modals = ['can', 'could']

print(cfd.tabulate(conditions=genres, samples=modals))

# Conditional Frequency Distribution of 'barley' and 'corn' in Reuters Corpus
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in reuters.fileids()
    for w in reuters.words(fileid)
    for target in ['barley', 'corn']
    if w.lower().startswith(target)
)

import matplotlib.pyplot as plt
cfd.plot()
plt.show()

# Conditional Frequency Distribution for 'america' and 'citizen' in Inaugural Corpus
cdf = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)

cdf.plot()
plt.show()

# Conditional Frequency Distribution for Word Lengths in UDHR Corpus
languages = ['Chickasaw', 'English', 'German_Deutsch']
cdf = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)

cdf.plot(cumulative=True)
plt.show()