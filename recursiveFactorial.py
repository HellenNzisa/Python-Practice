def recursiveFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursiveFactorial(n - 1)
    
# Here I'm going to use a random value of n(4) to test the function
# and see if it returns the correct factorial value.
#recursive factorial is where the function calls itself to calculate the factorial of a number.
# output should be 24
print(recursiveFactorial(4))