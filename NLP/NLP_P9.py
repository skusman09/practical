"""
NLP Practical 9 - Corrected Code
"""

# ---------------- Section a: Word Tokenization in Hindi ----------------

# Install and set up INLTK (requires manual installation)
# Uncomment and run the following commands manually if needed
# !pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
# !pip install inltk
# !pip install tornado==4.5.3

from inltk.inltk import setup, tokenize

# Setup Hindi language model
setup('hi')

hindi_text = "प्राकृतिक भाषा सीखना बहुत दिलचस्प है।"
tokens = tokenize(hindi_text, "hi")
print("Tokenized Hindi text:", tokens)

# ---------------- Section b: Generate Similar Sentences in Hindi ----------------

from inltk.inltk import get_similar_sentences

output = get_similar_sentences('मैं आज बहुत खुश हूं', 5, 'hi')
print("Similar sentences in Hindi:", output)

# ---------------- Section c: Identify the Indian Language of a Text ----------------

# Setup for Gujarati language
setup('gu')

from inltk.inltk import identify_language

text = "બીના કાપડિયા"
language = identify_language(text)
print("Identified language:", language)
