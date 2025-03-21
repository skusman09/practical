
# Named Entity Recognition of user defined text .
import spacy
nlp = spacy.load("en_core_web_sm") 
text = "we are writing practical"

doc = nlp(text)

print("Noun Phrases:", [chunk.text for chunk in doc.noun_chunks]) 
print("verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
