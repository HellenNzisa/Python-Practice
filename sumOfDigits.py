def sumOfDigits(n):
    sum = 0
    for digit in str(n):
        sum = int(digit) + sum
    return sum

# My Test cases
print(sumOfDigits(1234))
print(sumOfDigits(2025))
print(sumOfDigits(2005))