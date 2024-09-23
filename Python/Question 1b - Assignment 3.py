#I Husam Abdelhalim, 000104532, certify that this work
#is my own effort and that I have not allowed anyone else to
#copy from it.

#temperature minimum temp 0C and max below 100C to have water
#crops grow min temp above 21C and below 32C
#to consider habitable require both water and crops

def question1b(temp):
    if (temp >= 21 and temp <= 32):
        return "habitable, can have water and crops"
    elif (temp > 0 and temp < 100):
        return "not habitable, only has water"
    else:
        return "inhabitable"

#client code
print("Running soultion to question 1b")
print("Assuming valid numeric input")
temp = float(input("What is the current temperature? "))
answer = question1b(temp)
print("The planet is " + (answer))

    
