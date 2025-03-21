
# Text Tokenization using Keras.

import tensorflow 
import keras
from tensorflow.keras.preprocessing.text import text_to_word_sequence 
str = "this tool is on beta stage."
tokens = text_to_word_sequence(str) 
print(tokens)