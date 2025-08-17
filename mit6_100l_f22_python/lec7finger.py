
############## YOU TRY IT ###################
# Write code that satisfies the following specification:
# Hint, use paper and pen for a strategy before coding!
def is_palindrome(s):
    """ s is a string
    Returns True if s is a palindrome and False otherwise
    """
    # your code here
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
        
    return True
################################################
#print(is_palindrome("absba"))
################################################
################ YOU TRY IT AT HOME #####################
################################################
# 1. Write code that satisfies the following specs:
def keep_consonants(word):
    """ word is a string of lowercase letters
        Returns a string containing only the consonants 
        of word in the order they appear
    """
    # your code here
    s = "aeoiu"
    re = "" 
    for i in word:
        if i not in s:
            re += i
    return re 

# For example
#print(keep_consonants("abcd"))  # prints bcd
#print(keep_consonants("aaa"))  # prints an empty string
#print(keep_consonants("babas"))  # prints bbs



# 2. Write code that satisfies the following specs:
def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    # your code here
    
    if c not in s:
        return -1

    i = 0
    j = len(s) - 1
    k = 0 
    while i < j and k < len(s):
        
        print(f" {s[i]}  {s[j]}")
        print(f" {i}  {j}")
        input(" ?? ")
        
        if s[i] != c:
            i += 1

        if s[j] != c:
            j -= 1
        
        k += 1
    
    return j - i



# For example
#print(first_to_last_diff('aaaa', 'a'))  # prints 3
#print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
print(first_to_last_diff('bxyc', 'b'))  # prints -1
