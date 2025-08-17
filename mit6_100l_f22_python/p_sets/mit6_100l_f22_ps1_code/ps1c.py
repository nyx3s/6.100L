import math

annal_slaray = float(input("inter u inner slaray : "))
portion_saved = float(input("inter the amount of savings in dismal : ")) / 100
total_cost = 1000000;
rise = 0.07

portion_down_payment = 0.25

last_pay = portion_down_payment * total_cost

curr_savinges = 0

mounth = 1;
salary = annal_slaray / 12

while curr_savinges <= last_pay:
    
    if mounth % 6 == 0:
        salary += salary * rise

    curr_savinges += portion_saved * salary

    curr_savinges += curr_savinges * (0.04 / 12) 
    
    #print(f"{curr_savinges}") 
    mounth += 1

print(f"the total amount to save in mounths :   {mounth}")
