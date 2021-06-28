secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user_input = int(input("Gauss the secret number: "))

if user_input != secret_number:
    print("Ha ha! You're stuck in my loop!")
    
    while True:
        input("Gauss the number again: ")
else: print("Well done, muggle! You are free now.")