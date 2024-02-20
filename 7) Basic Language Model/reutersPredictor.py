# Build a basic language model using trigrams of the Reuters corpus
# Reuters corpus is a collection of 10,788 news documents
# totaling 1.3 million words

import nltk
nltk.download('reuters')

from nltk.corpus import reuters
#print(type(reuters))
sentences = reuters.sents()
print(sentences[:10])
print('There are ', len(sentences))

# Text cleaning - remove punctuation
# and fix contractions
# pip install contractions
import contractions
import string

cleaned_up1 = []
for s in sentences:
    text_cleaned = []
    for m in s:
        if m != '':
            text_cleaned.append(m)
    cleaned_up1.append(text_cleaned)

print(cleaned_up1[:10])
print()
print()
cleaned_up = []
for s in cleaned_up1:
    new_sent = [''.join(char for char in item
                if char not in string.punctuation)
            for item in s if item !='']
    text_cleaned = []
    for x in new_sent:
        if x !='':
            text_cleaned.append(x.lower())
    cleaned_up.append(text_cleaned)

print('******** CLEANED UP ********')
print(cleaned_up[:10])

#N-Grams
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

# Crate a placeholder for language model
model = defaultdict(lambda: defaultdict(lambda:0))
# Split each sentence into trigrams and the calculate the frequency
# in which each combination of trigrams occurs in the reuters data

for sentence in cleaned_up:
    for word1,word2,word3 in trigrams(sentence,pad_right = True, pad_left=True):
        model[(word1,word2)][word3] += 1

# Use the frequency to calculate probabilities of a word given the previous two words
for word1_word2 in model:
    total_count = float(sum(model[word1_word2].values()))
    for word3 in model[word1_word2]:
        model[word1_word2][word3] = model[word1_word2][word3] / total_count

# Now we have a Language Model
# It can be used to make predictions of "next" word:
# For example: -- let's test it out
print(dict(model["today","the"]))
print()
predictors = dict(model["today","the"])
for x, y in predictors.items():
    print(x,'\t',y)
print()
print('******** NEXT WORD ********')
max_next_word = max(predictors.items(), key = lambda a:a[1])
print(max_next_word)

    
