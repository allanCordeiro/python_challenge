import re

#solving the 4th challenge
#http://www.pythonchallenge.com/pc/def/equality.html

with open('content/pc_03.txt', 'r') as file:
    characters = file.read()

pattern: str = '[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
words = re.findall(pattern, characters)

word: str = ''
for letter in words:
    word += letter

print(f'http://www.pythonchallenge.com/pc/def/{word}.html')