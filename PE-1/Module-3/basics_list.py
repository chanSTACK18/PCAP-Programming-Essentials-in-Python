hat_list = [1, 2, 3, 4, 5]

num = int(input("input: "))
hat_list[2] = num
print(f"After replaced = {hat_list}")

del hat_list[-1]
print(f"After deletion = {hat_list}")
print("Length of list = ", len(hat_list))
