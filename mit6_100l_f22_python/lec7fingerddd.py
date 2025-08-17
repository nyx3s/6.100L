def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    if c not in s:
        return -1
    # if reach here, c is in s
    for i in range(len(s)):
        if s[i]==c:
            # break here to save i as the first instance of c in s
            break
    # loop through s backwards
    for j in range(len(s)-1,-1,-1):
        if s[j]==c:
            # break here to save j as the last instance of c in s
            break
    # this return is ok becasue the loops iterated through indices not chars of s
    return j-i

# For example
print(first_to_last_diff('aaaa', 'a'))  # prints 3
print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
print(first_to_last_diff('xyz', 'b'))  # prints -1

################################################
################################################
################################################

