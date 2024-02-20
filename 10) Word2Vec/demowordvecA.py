# pip install nltk
# pip install gensim

import nltk
import gensim

# Australian Broadcasting Company (abc)
from nltk.corpus import abc
nltk.download("abc")
document = abc.sents()
print(len(document), ' number of sentences')
print(document[:5])

import preprocw2v as prep
data = prep.preprocess(document)

from gensim.models import Word2Vec
model = Word2Vec(sentences = data,
                vector_size = 50,
                window = 10,
                epochs = 20)

# finding similar words
print()
print('5 words most similar to fibrosis')
words = model.wv.most_similar('fibrosis', topn=5) # cosine similarity
for w in words:
    print(w)

# finding similar words
print()
print('5 words most similar to science')
words = model.wv.most_similar('science', topn=5) # cosine similarity
for w in words:
    print(w)

# finding similar words
print()
print('5 words most similar to oil')
words = model.wv.most_similar('oil', topn=5) # cosine similarity
for w in words:
    print(w)
