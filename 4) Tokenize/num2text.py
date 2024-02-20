## pip install inflect

# import the inflect library
import inflect

# convert number into words
def convert_number(text):
    # split string into list of words
    p = inflect.engine()
    temp_str = text.split()
    # initialize empty list
    new_string = []
 
    for word in temp_str:
        # if word is a digit, convert the digit
        # to numbers and append into the new_string list
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
 
        # append the word as it is
        else:
            new_string.append(word)
 
    # join the words of new_string to form a string
    temp_str = ' '.join(new_string)
    return temp_str
