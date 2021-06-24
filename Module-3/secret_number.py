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

user_input = int(input("Enter a No.: "))

while secret_number:
    if user_input != secret_number:
        print("Ha ha! You're stuck in my loop!")
        user_input = int(input("Enter a No. again: "))
    else:
        print("Well done, muggle! You are free now.")
        break
