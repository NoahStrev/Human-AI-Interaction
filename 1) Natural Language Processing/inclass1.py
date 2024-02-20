# A glance at NLP

import matplotlib.pyplot as plt
import sampletext as st
# get the text data

example = st.load_example()
print(example)
print('How many lines do we have?', len(example))

# we see there are empty (blank) lines so let's strip them
# Remove all empty newlines in our corpus and strip away
# any newline characters from other lines

print()
print('Removing blank lines')
example = list(filter(None,[item.strip('\n') for item in example]))
print(example)
print('How many lines do we have?', len(example))

# Let's visualize sentence or line lengths
# so how many characters in sentences

line_lengths = [len(sentence) for sentence in example]
print(line_lengths)
plt.hist(line_lengths)
plt.title('Number of characters per sentence.')
plt.show()

# Break each sentence (line) up into tokens (tokenize):

tokens = [item.split() for item in example]
print()
print('Tokenization:')
print(tokens)

# Let's plot the total words per sentence (line) in the example

total_tokens_per_line = [len(sentence.split()) for sentence in example]
print()
print('Number of tokens per sentence', total_tokens_per_line)
plt.hist(total_tokens_per_line, color='green')
plt.title('Number of tokens per line.')
plt.show()

# Now flatten the list of lists into one big list of tokens:

words = [word for sentence in tokens for word in sentence]
print()
print('The words in this document:')
print(words)

# Find the 10 most common words in our text corpora
# but first lowercase all of the words in the text

from collections import Counter
words = [word.lower() for word in words]
print()
print(words)
c = Counter(words)
c10 = c.most_common(10)
print()
print('10 most common words:')
print(c10)
for x in c10:
    print(x)

# Remove the filler words like pronouns and articles that don't convey much information:
# Generate a WordCloud - version 1
### Need to pip install wordcloud

from wordcloud import WordCloud
words_string = " ".join(words)
my_wordcloud = WordCloud().generate(words_string)

# Display the generated image

plt.imshow(my_wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

wordcloud2 = WordCloud(max_font_size=50, max_words=30,
                       background_color="white").generate(words_string)

plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis('off')
plt.show()

# WordCloud with a mask image
# pip install pillow

from PIL import Image
import numpy as np # pip install numpy on your own computers
word_mask = np.array(Image.open("robot.png"))
wordcloud3 = WordCloud(max_words=30, background_color="white",
                       mask=word_mask, contour_width=3, contour_color="teal").generate(words_string)

plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis('off')
plt.show()

