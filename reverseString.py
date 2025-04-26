def reverseString(string):
    reversed_string = "" # this basically starts with an empty string to store the reversed string

    for char in string: # use of loop to go through every single character in the string
        reversed_string = char + reversed_string 
        return reversed_string

#the output should be the reverse of the test word i put in the function
    
print(reverseString("hellen"))