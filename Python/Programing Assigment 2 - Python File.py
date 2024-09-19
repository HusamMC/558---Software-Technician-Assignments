import random

# I Husam Abdelhalim, 000104352, certify that this work is my own effort
# assume payment>= amount

amount = random.randint(0, 20) + round(random.randint(0,100)/100, 2)
print(amount)
payment = float(input('Please enter payment amount '))

change = payment - amount
dollar_qty=0
quarter_qty=0
dime_qty=0
nickel_qty=0

if change > 0:
    dollar_qty = change // 1
    change = change - dollar_qty*1

if change > 0:
    quarter_qty = change // 0.25
    change = change - quarter_qty*0.25

if change > 0:
    dime_qty = change // 0.10
    change = change - dime_qty*0.10

if change > 0:
    nickel_qty = change // 0.05
    change = change - nickel_qty*0.05
    
change = change - (quarter_qty*0.25+dime_qty*0.10+nickel_qty*0.05)
n = nickel_qty + round(change*2, 1)*10
print("I owe you "+ str(dollar_qty)+ " dollars " + str(quarter_qty) + " quarters " + str(dime_qty) + " dimes " + str(nickel_qty)+ " nickels ")




   
    

    


    
    


    
    





    
    



