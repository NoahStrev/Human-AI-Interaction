# pip install textblob
from textblob import TextBlob, Word

sentence = "The happiest elephant lovingly rinsed his feet thinking it better to show some effort"

sent = TextBlob(sentence)

# then lemmatize it
lem_sen = " ".join([w.lemmatize() for w in sent.words])

print(lem_sen)

print()

print("each words POS:")
for word, pos in sent.tags:
    print(word,"==>",pos)

print()
print('Noun phrases')
for np in sent.noun_phrases:
    print(np)
