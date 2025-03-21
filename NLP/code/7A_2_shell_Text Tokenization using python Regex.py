# Text Tokenization using python Regex.

import nltk
from nltk.tokenize import RegexpTokenizer

tk = RegexpTokenizer(r'\s+', gaps=True) # Use raw string (r'\s+') 
text = "this tool is on beta stage."
tokens = tk.tokenize(text) 
print(tokens)