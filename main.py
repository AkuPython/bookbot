from collections import defaultdict
from string import ascii_lowercase

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    return file_contents

def count_words(fc):
    return len(fc.split())

fc = main()

# print(fc)
print("--- Begin report of books/frankenstein.txt ---")
print(count_words(fc), 'words found in the document\n')

letter_count = defaultdict(int)

for char in fc:
    letter_count[char.lower()] += 1

[print(f"The '{c}' character was found {i} times")
    for c, i in sorted(letter_count.items(), key=lambda k_v: k_v[1], reverse=True)
        if c in ascii_lowercase]

