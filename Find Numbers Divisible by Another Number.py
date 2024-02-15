def find_divisible_numbers(dividend, divisor):
    divisible_numbers = []
    for number in range(1, dividend + 1):
        if number % divisor == 0:
            divisible_numbers.append(number)
    return divisible_numbers
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
result = find_divisible_numbers(dividend, divisor)
print(f"Numbers divisible by {divisor} in the range 1 to {dividend}: {result}")
