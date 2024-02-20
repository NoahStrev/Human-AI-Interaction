# Netflix Show descriptions
import matplotlib.pyplot as plt
with open('netflixshowdescriptions.txt', 'r',encoding='utf-8') as file:
    netflix = file.readlines()

#a. Print the first 10 lines in the dataset

print(netflix[:10])

#b. Print the count of the number of lines in the dataset

print('How many lines?', len(netflix))

#c. Strip away newline characters in the dataset

netflix = list(filter(None, [item.strip('\n') for item in netflix]))

#d. Print a count of the number of non-blank lines resulting in the dataset

print()
print('How many lines?', len(netflix))

#e. Graph the number of characters per sentence using a histogram plot

line_lengths = [len(sentence) for sentence in netflix]
plt.hist(line_lengths)
plt.title("number of chars per sentence")
plt.show()

#f. Break the sentences up into tokens.

tokens = [item.split() for item in netflix]

#g. Print the tokens resulting for the first 5 lines in the dataset

print()
print('Tokenization - sample:')
print(tokens[:5])

#h. Print the number of tokens per sentence for the first 10 lines in the dataset

tokens_per_sentence = [len(sentence.split()) for sentence in netflix]
print(tokens_per_sentence[:5])

#i. Graph the number of tokens per sentence in a histogram plot

plt.hist(tokens_per_sentence, color='green')
plt.title('Number of words per sentence')
plt.show()

#j. Flatten the list of token lists into one big list of tokens

words = [word for sentence in tokens for word in sentence]

#k. Print the first 20 tokens in the new list

print()
print('First 20 words:')
print(words[:20])

#l. Print the 10 most common words in the text corpus

from collections import Counter
c = Counter(words)
c10 = c.most_common(10)
print()
print('The 10 most common words in the netflix show descriptions are')
for x in c10:
    print(x)

#m. Remove the stopwords from the list of tokens

import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
words = [word.lower() for word in words if word.lower() not in stopwords]

#n. Print the 10 most common non-stop words in the text corpus

c = Counter(words)
c10 = c.most_common(10)
print()
print('The 10 most common non-stop words in the netflix show descriptions are')
for x in c10:
    print(x)

#o. Create a WordCloud with a bilinear interpolation with axis off and plot it

from PIL import Image
import numpy as np
from wordcloud import WordCloud

words_string = " ".join(words)
wordcloud = WordCloud().generate(words_string)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()

#p. Create a second WordCloud that plots a maximum of 40 words on a red-colored background

words_string = " ".join(words)
wordcloud = WordCloud(max_words=40, background_color = "red",
                      contour_width=5, contour_color="black").generate(words_string)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()

#q. Create a third WordCloud that plots a maximum of 40 words using the image mask provided on our Canvas course site

words_string = " ".join(words)
word_mask = np.array(Image.open("netflix.png"))
wordcloud = WordCloud(max_words=40, background_color = "red", mask = word_mask,
                      contour_width=5, contour_color="black").generate(words_string)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
