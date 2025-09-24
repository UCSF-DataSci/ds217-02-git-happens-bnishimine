print("Enter two values, where the first value is lower than the second value, with the number 13 in between.")
low = int(input("Enter the lower value: "))
high = int(input("Enter the higher value: "))

for i in range(low, high):
    if i == 13:
        print(13)
    else:
        print("Not 13")
    i += 1

