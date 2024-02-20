import preprocw2v as prep
import nltk
from nltk.corpus import brown
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as pyplot

nltk.download("brown")
doc = brown.sents()
data = prep.preprocess(doc)

print(len(data), ' num of sentences ')
print(data[:20])

model = Word2Vec(sentences = data,
                vector_size = 50,
                window = 10,
                epochs = 20)

print()
print('There are ', len(model.wv), ' unique words')

# Vector for word love
print('Vector for love:')
print(model.wv["love"])
print()

# Finding most similar words
words = model.wv.most_similar('love', topn=5) # cosine similarity
for w in words:
    print(w)

words = ["france", "germany", "italy", "truck", "boat", "car", "teacher", "student"]
X = model.wv[words]
pca = PCA(n_components = 2)
result = pca.fit_transform(X)

pyplot.scatter(result[:,0], result[:,1])
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i,0], result[i,1]))
pyplot.show()
