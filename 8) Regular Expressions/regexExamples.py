# Testing out regular expressions

import re

txt = 'The tenth is the date when the tent is to be delivered'

print(re.findall('en', txt))

print(re.findall('day', txt))

print(re.split('t', txt))

print(re.split('[td]', txt))

print(re.search('d', txt))

print(re.split('\s', txt))
print()

print(re.split('\w', txt))
print()

print(re.split('\w', txt, 1))
print()

print(re.split('\W', txt))
print()

print(re.split('\d', txt))
print()

print(re.sub('\s', '3', txt))
print()

txt2 = 'My phone number is 262-524-7368'
x = re.findall('\d{3}-\d{3}-\d{4}', txt2)
y = re.search('\d{3}-\d{3}-\d{4}', txt2)

print()
print('findall', x)
print('search', y)
