

x = int(input("inter num to find cube root : "))

eps = 0.01

low = 0
high = x
mid = (high - low)/2 + low

guss = 0

while abs(mid**3 - x) >= eps:
    if mid**3 < x:
        low = mid
    else:
        high = mid
    
    print(f"low {low} high {high} mid {mid}  {mid**3}")

    mid = (high - low)/2 + low
    guss += 1
    print(f"new mid {mid}")
    input("countune ?? ")
print(f"the cube root of {x} = {mid} \n with eps = {eps} \n and number of gusses = {guss}")
