year = int(input("Enter a year: "))


# Write your code here.
if year > 1580:
    if year % 4 != 0:
        print("This is common Year")
    elif year % 100 != 100:
        print("This is Leap Year")
    elif year % 400 != 400:
        print("This is common Year")
    else: print("This is Leap Year")
else: print("Not within the Gregorian calendar period.")