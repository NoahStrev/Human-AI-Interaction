# An example of dependency parsing

import spacy

sentence = 'I have seldom heard her mention his name under any other name'

# load the spacy engine
nlp = spacy.load('en_core_web_sm')

# create the dependency structure
doc = nlp(sentence)

# display the dependency tags
for token in doc:
    print(token.text, '\t', token.tag_, '\t', token.dep_, '\t')
    spacy.explain(token.dep_)

from spacy import displacy
displacy.serve(doc, style='dep')
