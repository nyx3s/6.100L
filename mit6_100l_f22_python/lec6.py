n = int(input("inter num between 0 and 1000 "))

low = 0
high = 1000

mid = (high - low)/2 + low

gess = 0
while mid != n: 

    if mid < n:
        low = mid
    else:
        high = mid
    
    mid = int((high - low)/2 + low)
    gess += 1
    
    print(f"low {low} high {high} mid {mid} ")
    input("countenue ?? ")

print(f"u gess = {mid} number of gess is {gess}")
