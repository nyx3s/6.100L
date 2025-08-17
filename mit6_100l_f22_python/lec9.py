def char_count(s):
    """ @pram s the string that whanna aboreet
        @return tuple the frist is number of voles
        secuned is number of constent"""
    vol = "aeoiu"
    cvol = 0
    count = 0
    for i in s:
        if i in vol:
            cvol +=1
        else:
            count += 1
    return (count,cvol)

#print(char_count("abcd"))

def dot_product(tA, tB):
    """
    tA: a tuple of numbers
    tB: a tuple of numbers of the same length as tA
    Assumes tA and tB are the same length.
    Returns a tuple where the:
    * first element is the length of one of the tuples
    * second element is the sum of the pairwise products of tA and tB
    """
    # Your code here
    sum  = 0
    i = 0
    while i < len(tA):

        sum += tA[i] * tB[i]
        i += 1
    return (len(tA), sum)
# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)

