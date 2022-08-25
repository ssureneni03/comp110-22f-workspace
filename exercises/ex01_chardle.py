"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730469374"

word: str = str(input("Enter a 5-character word: "))

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_char: str = str(input("Enter a single character: "))

if len(single_char) > 1 or len(single_char) == 0:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + single_char + " in " + word)

count = 0
if single_char == word[0]:
    count += 1
    print(single_char + " found at index 0")
if single_char == word[1]:
    count += 1
    print(single_char + " found at index 1")
if single_char == word[2]:
    count += 1
    print(single_char + " found at index 2")
if single_char == word[3]:
    count += 1
    print(single_char + " found at index 3")
if single_char == word[4]:
    count += 1
    print(single_char + " found at index 4")
if single_char not in word:
    print("No instances of " + single_char + " found in " + word)
print(str(count) + " instances of " + single_char + " found in " + word)







