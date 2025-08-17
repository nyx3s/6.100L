# i did this assingment nyx
# Problem 1: Lamba Functions Practice
# a) Write a lambda function that calculates the cube root of a given number 
# passed in as an argument
# INSERT CODE BELOW HERE
f1 = lambda x: x**(1/3)

# b) Write a lambda function that takes in two arguments and outputs the product
# of those two numbers. 
# INSERT CODE BELOW HERE
f2 = lambda x,y : x*y

# uncomment to test function
print(f1(8))
print(f1(4))
print(f2(1,2))
print(f2(4,5))



#############################################################################
# Problem 2: Practice working with Tuples:
# Write a function that counts the number of times the number 1 appears 
# in an inputted tuple.
# INSERT CODE BELOW HERE
def count_number_one(t):
    count = 0
    for i in t:
        if i == 1:
            count +=1
    return count



# uncomment to test function
print(count_number_one((1,2,3,4,5,1,1)))  


#############################################################################
# Problem 3: Practice working with Python Tuples
# Write a Function that takes in two tuples and outputs a single tuple containing 
# only common elements of both tuples. 
# INSERT CODE BELOW HERE
def common_elements(t1, t2):
    re = ()
    for i in range(len(t1)):
        if t1[i] in t2:
            re += (t1[i],)
    return re




# uncomment to test function
print(common_elements((2,3,4), (3,4,5,6)))


#############################################################################
# Problem 4: Practice working with Python Lists
# Write a Python program to remove sublists from a given list of lists, which 
# contain an element outside a given range.
# e.g 
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contain an 
# element outside the given range of 12 - 20 (inclusive):
# [[13, 14, 15, 17]]
# INSERT CODE BELOW HERE
def remove_list_range(lst1, low, high):
    
    lst = lst1[:]
    for i in lst:
        #print(f"{ i } {not high <= max(i) and min(i) <= low}")
        #input(" ?? ")
        if not (high <= max(i) and min(i) <= low):
            lst1.remove(i)
    return lst1





# uncomment to test function
print(remove_list_range([[2], [0,8], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]], 13, 17))
print(remove_list_range([[6,7,8],[1,2,3,4,5]],1,5))

