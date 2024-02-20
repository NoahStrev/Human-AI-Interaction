import txt_preprocessing_code as prep
import pandas as pd

sentences = ["We are reading about Natural Language Processing Here",
            "Natural Language Processing making computers comprehend language data",
            "The field of Natural Language Processing is evolving everyday"]

# Create a Pandas Series of the object

corpus = pd.Series(sentences)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print('Original data:')
print(corpus)

common_dot_words = ['U.S.', 'Mr.', 'Mrs.', 'D.C.']

preprocessed_corpus  = prep.preprocess(corpus,
                                       keep_list=common_dot_words,
                                       stemming = False,
                                       stem_type=None,
                                       lemmatization = True,
                                       remove_stopwords = True)
print()
print('Data after preprocessing:')
print(preprocessed_corpus)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
tokenCountMatrix = vectorizer.fit_transform(preprocessed_corpus)
print()
print(' Count Vectorizer Results - features (ie vocabulary):')
print(vectorizer.get_feature_names())
print()
print('Count of tokens in respective sentences:')
print(tokenCountMatrix.toarray())

# **********************************************************************************
from sklearn.feature_extraction.text import TfidfVectorizer
# The data is fitted to the TfidVectorizer 
vectorizer = TfidfVectorizer()
# and then transformed into TF-IDF vector forms using fit_transform
tf_idf_matrix = vectorizer.fit_transform(preprocessed_corpus)

print()
print(' TF-IDF Vectorizer Results - features (ie vocabulary):')
print(vectorizer.get_feature_names())
print()
print('The weights for the terms:')
print(tf_idf_matrix.toarray())
print('The shape of the TF-IDF matrix is: ', tf_idf_matrix.shape)
# compare the output to the CountVectorizer output

### ***********************************************************************************
##from sklearn.metrics.pairwise import cosine_similarity
##for i in range(tokenCountMatrix.shape[0]):
##    for j in range(i+1, tokenCountMatrix.shape[0]):
##        print('The cosine similarity between the documents ', i, ' and ',
##              j, ' is: ',prep.cosine_similarity(tokenCountMatrix.toarray()[i],
##                                           tokenCountMatrix.toarray()[j]))
