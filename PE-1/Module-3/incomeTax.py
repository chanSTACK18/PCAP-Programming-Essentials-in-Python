income = float(input("Enter the annual income: "))

tax = 0.0
# Write your code here.
if income < 85528:
    tax = income * 0.18 - 556.06
else:
    tax = (income - 85528) * 0.32 + 14839.02

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
