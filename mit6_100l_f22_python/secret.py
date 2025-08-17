

s = int(input("inter ur num : "))
found = False

for i in range(1,11):

    if i == s:
        found = True
        break

if found:
    print("found")
else:
    print("not found")
