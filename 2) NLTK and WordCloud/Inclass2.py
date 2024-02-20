# pip install natural language toolkit

##import nltk
##nltk.download()

from nltk.corpus import gutenberg
import matplotlib.pyplot as plt

bible = gutenberg.open('bible-kjv.txt')
bible=bible.readlines()

# a. print the first 5 lines in the dataset

print(bible[:5]) # just get a few lines

# b. print the count of the number of lines in the dataset

print('How many lines?', len(bible))

# c. strip away newline characters in the dataset

bible = list(filter(None, [item.strip('\n') for item in bible]))
# d. print the first 10 lines in the dataset

print()
print(bible[:10])

# e. print a count of the number of non-blank lines resulting in the dataset

print()
print('How many lines?', len(bible))

# f. graph the number of characters per sentence using a histogram plot

line_lengths = [len(sentence) for sentence in bible]
plt.hist(line_lengths)
plt.title("number of chars per sentence")
plt.show()

# g. break the sentences up into tokens

tokens = [item.split() for item in bible]

# h. print the tokens resulting for the first 10 lines in the dataset

print()
print('Tokenization - sample:')
print(tokens[:10])

# i. print the number of tokens per sentence for the first 5 lines in the dataset

tokens_per_sentence = [len(sentence.split()) for sentence in bible]
print(tokens_per_sentence[:5])

# j. graph the number of tokens per sentence in a histogram

plt.hist(tokens_per_sentence, color='green')
plt.title('Number of words per sentence')
plt.show()

# k. flatten the list of token lists into one big list of tokens

words = [word for sentence in tokens for word in sentence]
print()
print('First 140 words:')
print(words[:140])
print('Number of words in the bible:', len(words))

# l. print the first 10 tokens in a new list
# m. print the 10 most common words in the text corpus
# n. remove the stopwords from the list of tokens

import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
words = [word.lower() for word in words if word.lower() not in stopwords]

# o. print the 10 most common non-stop words in the text corpus
from collections import Counter
c = Counter(words)
c10 = c.most_common(10)
print()
print('The 10 most common words in the bible (kjv) are')
for x in c10:
    print(x)

# p. create a WordCloud with a bilinear interpolation with axis off and plot it
# q. create a second WordCloud that plots a maximum of 35 words on a white-colored background
# r. create a third WordCloud that plots a maximum of 35 words using the image mask provided on our Canvas site

from PIL import Image
import numpy as np
from wordcloud import WordCloud

words_string = " ".join(words)
word_mask = np.array(Image.open("bookimage.png"))
wordcloud = WordCloud(max_words=35, background_color = "white", mask = word_mask,
                      contour_width=5, contour_color="blue").generate(words_string)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
