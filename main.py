from collections import defaultdict
from string import ascii_lowercase
from stats import get_num_words
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def main():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

fc = main()

# print(fc)
print(f"--- Begin report of {sys.argv[1]} ---")
print(get_num_words(fc), 'words found in the document\n')

letter_count = defaultdict(int)

for char in fc:
    letter_count[char.lower()] += 1

print("Letter Counts:")
[print(f"{c}: {i}")
    for c, i in sorted(letter_count.items(), key=lambda k_v: k_v[1], reverse=True)
        if c in ascii_lowercase]

