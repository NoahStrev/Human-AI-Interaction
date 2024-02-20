# Porter and Snowball Stemmers

import nltk

from nltk import word_tokenize

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk import wordnet as wn

sentence = 'The happiest elephant lovingly rinsed his feet thinking it better to show some effort'

# convert sentence into tokens
word_tokens = nltk.word_tokenize(sentence)


# Create a Word Net Memmatizer object
wnl = WordNetLemmatizer()

lem_sentence = ' '.join([wnl.lemmatize(words) for words in word_tokens])

print(lem_sentence)
print()
print(wnl.lemmatize("happiest", 'a')) # adjective
print(wnl.lemmatize("rinsed", 'v')) # verb
print(wnl.lemmatize("better", 'a')) # adjective
print(wnl.lemmatize("lovingly", 'r')) # adverb

# So above tells that suppling POS info improves lemmatization

print()
print('Synonyms for lovingly:')
# In the meantime:
from nltk.corpus import wordnet as wn
syns = wn.synsets("lovingly") # synset = synonym set
print(syns)

synonyms = []
antonyms = []

for syn in wn.synsets("delight"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print()
print('*** Wordnet lexical db ***')
print('for word delight:')
print()
print('synonyms', set(synonyms))
print('antonyms', set(antonyms))
