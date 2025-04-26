def factorialLoop(n):
    if n == 0:
        return 1  
    else:
        return n * factorialLoop(n - 1)
    
#Here I'm going to use a random value of n(5) to test the function
# and see if it returns the correct factorial value.
#output should be 120
print(factorialLoop(5))