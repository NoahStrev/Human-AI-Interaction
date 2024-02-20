##############################################
# ONE SENTENCE EXAMPLE
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
sentence = "Natural Language Processing is very important to understanding in the real world"
ex_words = word_tokenize(sentence)
print(ex_words)

# Load Moby Dick Chapter 1
with open('MelvilleMobyDickChapter1.txt', 'r', encoding='utf-8') as file:
    book = file.read()

# Sentence tokenize
from nltk.tokenize import sent_tokenize
chapter1 = sent_tokenize(book)
#print(chapter1)

import string
new_chapter1 = []
for each_string in chapter1:
    new_string = each_string.translate(str.maketrans('','',string.punctuation))
    new_chapter1.append(new_string)

print(new_chapter1)

# Let's do two things
# 1 Let's build a list of word lists (a list of words for each sentence)

words = []
for one_sentence in chapter1:
    its_words = word_tokenize(one_sentence)
    # print(its_words)
    words.append(its_words)

print('The words in each sentence:')
print(words)

# 2 Let's build one list of all the words
# words now is a list of lists. Each list corresponds to one sentence
# But I also want just one big list of words
just_words = []
for each_sentence_word_list in words:
    for each_word in each_sentence_word_list:
        just_words.append(each_word)

print('JUST THE WORDS ************')
print(just_words)

# remove the puncuation
