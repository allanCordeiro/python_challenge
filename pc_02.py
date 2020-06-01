from collections import Counter

#solving the 3nd challenge
#http://www.pythonchallenge.com/pc/def/ocr.html

with open('content/pc_02.txt', 'r') as file:
    characters = file.read()

#this is the easy way to find out
#print(Counter(characters).most_common()[:-8-1:-1])

counter: dict = {}
for letter in characters:
    so_far = counter.get(letter, 0)
    counter[letter] = so_far + 1

match: str = ""
for word, qty in counter.items():
    if qty == 1:
        match += word

print(f'http://www.pythonchallenge.com/pc/def/{match}.html')