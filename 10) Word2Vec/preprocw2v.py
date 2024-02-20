import string

def preprocess(document):
    data = []
    for sent in document:
        new_sent = []
        for word in sent:
            new_word = word.lower()
            if new_word[0] not in string.punctuation:
                new_sent.append(new_word)
                
        if len(new_sent) > 0:
            data.append(new_sent)
    return data
