# spaCy Lemmatizer example

# pip install spaCy
# python -m spaCy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp('The happiest elephant lovingly rinsed his foot thinking it better to show some effort')

tokens = []
for token in doc:
    tokens.append(token)

print(tokens)

lemmatized_sentence = " ".join([token.lemma_ for token in doc])

print()
print(lemmatized_sentence)
