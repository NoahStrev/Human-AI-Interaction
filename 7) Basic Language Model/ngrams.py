# Example of n-grams: bigrams and trigrams

from nltk.util import ngrams

sample_sentence = "Natural Language Processing is a very big topic"

# simply split words at the blank space (rather than word_tokenize)
tokens = sample_sentence.split(' ')

# bigrams
bigrams = list(ngrams(tokens,2))
print('BIGRAMS:')
for token in bigrams:
    print(token)
print()

# trigrams
trigrams = list(ngrams(tokens,3))
print('TRIGRAMS:')
for token in trigrams:
    print(token)
