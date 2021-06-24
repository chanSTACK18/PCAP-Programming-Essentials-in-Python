# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Name the word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter == ("A") or letter == ("E") or letter == ("I") or letter == ("O") or letter == ("U"):
        continue
    print(letter)
