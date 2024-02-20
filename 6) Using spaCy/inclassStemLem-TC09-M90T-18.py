import nltk
from nltk import word_tokenize

# 1. Download the docoument
with open('MelvilleMobyDickChapter1.txt', 'r', encoding = 'utf-8') as file:
    UFO = file.read()

# 2. Use the nltk tokenization to split out the sentences
#nltk.download('punkt')
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(UFO)
#print(sentences)

# 3. Print the sentences one per line with their relative indices
#for index, s in enumerate(sentences):
#    print(index, " ", s)

# 4. Apply Porter and Snowball stemming to each word and print the two stems per word for each sentence
from nltk import word_tokenize

bigstrings = ""
for s in sentences:
    bigstrings = bigstrings + s

bigstrings = bigstrings.replace(',',' ')
bigstrings = bigstrings.replace(',',' ')

word_tokens = word_tokenize(bigstrings)
#print('*** WORDS ***')
#print(word_tokens)

from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

ps = PorterStemmer()
ss = SnowballStemmer(language='english')

#for w in word_tokens:
#    print(w, 'Porter Stem:', ps.stem(w), 'Snowball Stem:', ss.stem(w))

# 5. Lemmatize each sentence using TextBlob
from textblob import TextBlob, Word
sent2 = []
for s in sentences:
    blob_sent = TextBlob(s)
    sent2.append(s)

lemm_list = []
for one_blob_sentence in sent2:
    lem_sentence = " ".join([w.lemmatize() for w in one_blob_sentence.words])
    lemm_list.append(lem_sentence)
# 6. Display each word and its POS for each sentence using TextBlob

# 7. Use TextBlob to display the number of times the word 'light' appears in the text

# 8. Lemmatize each sentence using spaCy

# 9. What do you notice regarding the lemmatization form of each sentence

# 10. Display each word and its POS for each sentence using spaCy
