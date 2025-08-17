## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
deposit = float(input("initial deposit"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost = 800000
down_payment = 0.25 * cost

low = 0.0
high = 1.0

r = (low+high) / 2.0
approx = 100
saving = 0
count = 0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while abs(down_payment - saving) > approx:

    saving = deposit *(1+ r/12)**36
    
   # print(f"crr saving {saving} r = {r}")
    
    if saving < down_payment:
        low = r
    else:
        high = r
    
    r = (low + high ) / 2.0
    
    count += 1
   # input(" countenue ")


print(f"crr saving {saving} r = {r} count = {count}")

