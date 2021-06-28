word_without_vowels = ""

user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    word_without_vowels = word_without_vowels + letter

print(word_without_vowels)
