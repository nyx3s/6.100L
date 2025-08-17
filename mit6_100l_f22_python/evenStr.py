

s = input(" inter ur string ")
re = ""

for i in range(len(s)):

    if i % 2 == 0:
        re += s[i]
print(re)
