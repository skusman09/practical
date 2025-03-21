
# Text Tokenization using spacy library.

# NOTE: code in colab import spacy

nlp = spacy.blank("en")

str = "this tool is on beta stage." 
doc = nlp(str)

words = [word.text for word in doc] 
print(words)