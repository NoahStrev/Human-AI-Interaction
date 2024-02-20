# Porter and Snowball Stemmers

from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

ps = PorterStemmer()
ss = SnowballStemmer(language='english')

from nltk.tokenize import word_tokenize

sentence = 'Programmer program with programming language fairly and sportingly'

words = word_tokenize(sentence)

print("Stemming the sentence")
print()

for w in words:
    print(w, 'porter stem:', ps.stem(w))
    print(w, 'snowball stem:', ss.stem(w))
    print()
