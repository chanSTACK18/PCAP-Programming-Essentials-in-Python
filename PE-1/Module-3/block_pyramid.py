blocks = int(input("Enter the number of blocks: "))

height = 0
inLayer = 1

while inLayer <= blocks:
    height += 1
    blocks -= inLayer
    inLayer += 1

print("The height of the pyramid: ", height)
