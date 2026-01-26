# This program calculates the factorial of a non-negative integer using a while loop

num = int(input("enter a non-negative integer: "))     # takes input from the user
factorial = 1                                          # initialize variable
i = 1                                                  # loop counter
while i <= num:
    factorial *= i                                     # update factorial by multiplying with the next number in sequence
    i += 1
print("the factorial of", num, "is:", factorial)       # prints the result