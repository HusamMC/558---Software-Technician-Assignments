#I Husam Abdelhalim, 000104532, certify that this work
#is my own effort and that I have not allowed anyone else to
#copy from it.

#question 2 creating a loop
#loop will exit when user enters the input"quit"

def Question1a(pH):
    if (pH == 7):
        print("The pH is netural")
    elif (pH < 4):
        print("The pH is very Acidic")
    elif (pH > 10):
        print("The pH is very Alkali")    
    elif (pH > 7):
        print("The pH is Alkali")
    elif (pH < 7):
        print("The pH is Acidic")
    return pH

choice = 0
while (choice < 2):

    print("1) Enter a valid pH value")
    print("2) quit")
    choice = int(input("Select a menu option: "))

    if choice > 2:
        choice = 0
    elif choice == 1:
        pH = float(input("What is the pH that you want to know about? "))
        Question1a(pH)
    else:
        print("Goodbye")


