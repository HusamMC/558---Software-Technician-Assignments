#I Husam Abdelhalim, 000104532, certify that this work
#is my own effort and that I have not allowed anyone else to
#copy from it.


def Question1a(pH):
    if (pH == 7):
        print("Netural")
    elif (pH < 4):
        print("Very Acidic")
    elif (pH > 10):
        print("Very Alkali")    
    elif (pH > 7):
        print("Alkali")
    elif (pH < 7):
        print("Acidic")
    return pH

#client code
print("Running solution to question 1a")
print("Assuming valid numeric input")
pH = float(input("What is the pH that you want to know about? "))
answer = Question1a(pH)
print("The answer is: " + str(answer))
