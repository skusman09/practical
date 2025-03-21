# Word Tokenization In Hindi CODE:
!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

!pip install inltk

!pip install tornado==4.5.3 from inltk.inltk import setup setup('hi')

from inltk.inltk import tokenize

hindi_text = """प्राTकृ! तिKकृ भाTषाT सी(खनाT बहुK तिKलचस्प है1।"""

tokenize(hindi_text, "hi")

# Generate Similar Sentences From A Given Hindi Text Input CODE:
!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

!pip install inltk

!pip install tornado==4.5.3 

from inltk.inltk import setup 
setup('hi')

from inltk.inltk import get_similar_sentences

output = get_similar_sentences('मैं4आज बहुK ख7श हूं:', 5, 'hi')
print(output)

# Identify The Indian Language Of A Text CODE:
!pip install torch==1.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

!pip install inltk

!pip install tornado==4.5.3 

from inltk.inltk import setup 
setup('gu')

from inltk.inltk import identify_language
identify_language('@tનાL કાL4PCuL')