high = 0
low = 0

while 13 not in range(low, high):
    print("Enter two values, where the first value is lower than the second value, with the number 13 in between.")
    low = int(input("Enter the lower value: "))
    high = int(input("Enter the higher value: "))
    if(13 not in range(low, high)):
        print("The number 13 is not in the range. Please try again.")

for i in range(low, high):
    if i == 13:
        print(13)
    else:
        print("Not 13")
    i += 1

