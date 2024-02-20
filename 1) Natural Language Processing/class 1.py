### The Zen of Python
### is a set of 20 guiding principles, also known as
### aphorisms, that have been influential to Pythons's design
##import this
##
### working with strings
### afterall we are doing NLP
##
##my_string = "This is a String" # storing a string
##print('Type: ', type(my_string))
##print('Value:', my_string)
##
### another string
##simple_string = 'Hi there' + " this is another string "
##print(simple_string)
##
### multi-line strings
##multiline_string = """And I'm
##a multi-line
##string"""
##multi2 = "And so\nam I"
##print(multiline_string)
##print(multi2)
##
### escape sequences
##file_locationA = "D:\myfolder\file.py"
##print(file_locationA)
##file_locationB = "D:\\myfolder\\file.py"
##print(file_locationB)
##file_locationC = r"D:\myfolder\file.py"
##print(file_locationC)
### r denotes a raw string
##
### unicode string literals
##my_friend = 'R\u00e8ne is my friend!'
##print(my_friend)
##story = 'We played \u26F3 in the afternoon'
##print(story)
##
##all_together = ' '.join([my_friend,story])
##print()
##print('ALL TOGETHER:')
##print(all_together)
##print('..... and .....')
##print(all_together[::-1])
##
##print()
##second_str = 'The sun is shining' + ' and it is raining \u2614'
##print(second_str)
##third_str = 'The sun is shining'   ' and it is raining \u2614'
##print(third_str)
### fourth_str = 'But not this' third_str
##
##shorter_str = ' it is raining \u2614'
##cool_str = shorter_str * 3
##print()
##print(cool_str)
##
##one_more = (story + shorter_str) * 2
##print()
##print(one_more)
##
##maybe_just_one = ('So '
##                  'how about yet '
##                  'another way '
##                  'to concatenate?')
##print()
##print(maybe_just_one)
##
### Length of a string
##num = len(maybe_just_one)
##print('which is ', num, ' characters')
##
### checking fro a substring
##print('yet' in maybe_just_one)
##print('yo' in maybe_just_one)
##
### Indexing
##string1 = "Hello bye"
##for index, character in enumerate(string1):
##    print('Character-->', character,'has index-->',index)
##
##print(string1[4], string1[-1], string1[-5])
##
##print()
##print(id(string1))
##string1 = string1.replace('o','y')
##print(string1)
##print(id(string1))
##
###string slicing
##print()
##print(" *** SLICING ***")
##print('string1 is ', string1)
##print('a', string1[:])
##print('b', string1[1:4])
##print('c', string1[:3])
##print('d', string1[3:])
##print('e', string1[-3:])
##print('f', string1[:3] + string1[-3:])
##print('g', string1[::1]) # no offset
##print('h', string1[::2]) # getting every 2 letters Streveler --> Srvlr
##
### Some popular string methods
##s = 'python is used extensively in nlp'
##print(s.capitalize())
##print(s.upper())
##print(s.title())
##print(s.replace('nlp','NLP'))
##print('123'.isdecimal())
##print('abc'.isdecimal())
##print('num1'.isalpha())
##print('abc'.isalpha())
##print('num1'.isalnum())
##print('abc'.isalnum())
##print('123'.isalnum())
##print('cost$'.isalnum())

s = 'Here,is,a,comma,separated,string'
print(s.split(','))

t = ''.join(s.split(','))
print(t)

v = '   A string surrounded by spaces   '
print(v)
print(v.strip())

sentences = 'Hi. Nice to see you.'
print(sentences.split('.'))
