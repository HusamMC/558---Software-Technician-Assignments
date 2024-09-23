#I Husam Abdelhalim, 000104532, certify that this work
#is my own effort and that I have not allowed anyone else to
#copy from it.

#Sides a, b, and c = 180
#a+b>c, a+c>b, and b+c>a must be true
#assume that the 3 input numbers are valid integer numbers <0
#Identify if triangle is equilateral, isosceles or scalene.

def question1c(a, b, c):
    if (a + b > c and a + c > b and b + c > a):
        if (a == b and b == c):
            return "equilateral triangle"
        elif (a != b and b != c and a != c):
            return "scalene triangle"
        else:
            return "isosceles triangle"
    else:
        return "invalid triangle"


#client code bitches
print("Running solution to question 1c")
print("Assuming valid numeric input")
a = float(input("What is your input for first side? "))
b = float(input("What is your input for second side? "))
c = float(input("What is your input for third side? "))
answer = question1c(a, b, c)
print(answer)
    
    
