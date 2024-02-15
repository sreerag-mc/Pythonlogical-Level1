num = 10
sum = 0
if num < 0:
    print("Enter a positive number")
else:
    while num > 0:
        sum = sum + num
        num = num -1
    print("The sum is", sum)
