import nltk
import gensim

import loadtext as lt
sentences = lt.loadtext()
print('Our text corpus:')
print(sentences)

from gensim.models import Word2Vec
model = Word2Vec(sentences, min_count=1)

print('There are ', len(model.wv), ' unique words')
print('Each is of vector size: ', model.vector_size)

print(model.wv)
print()

print(list(model.wv.index_to_key))

print(model.wv.get_vector('Natural'))
