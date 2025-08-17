# idid this assigment nyx
# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

#x = float(input("Using bisection search calculate the forth root of: " ))
#epsilon = 0.01
#low = # FILL IN
#high = # FILL IN
#ans = # FILL IN




# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 
def in_Range(x, n):

    if x in range(n+1):
        return True
    else:
        return False
    



#print(in_Range(6,6))
# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
def perNum(n):
    sqr = int(n**(1/2))
    x,y  = (0,0)
    for i in range(2,n):

        if n % i == 0:
            x = i
        print(f"{n} % {i} ")
        input("??? ")
    if x != 0:
        y = n / x
    return ((y + x + 1) == n)



print(perNum(6))
print(perNum(28))
print(perNum(50))
# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0



