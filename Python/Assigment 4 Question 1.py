# I Husam Abdelhalim, 000104532, certify that this work is my own effort and
# that I have not allowed anyone else to copy from it.

user_shape = int(input("Enter shape code (1=square, 2=triangle, 3=arrow head): "))
user_size = int(input("Enter a shape size: "))
square = 0
triangle = 0
arrow = 0

while user_shape == 1 and user_size > 0:
    print("*" * user_size)
    user_shape = user_size * "*"
    while square < user_size:
        print("*" + " " * (user_size - 2) + "*")
        square = square + 1
    print("*" * user_size)
    user_shape = user_size * "*"
   
while user_shape == 2 and user_size > 0:
    while triangle < user_size:
        triangle = triangle + 1
        print(triangle * "*")
        
while user_shape == 3 and user_size > 0:
    while arrow < user_size:
        arrow = arrow + 1
        print(arrow * "*")
    while arrow >= 0:
        arrow = arrow - 1
        print(arrow * "*")
    user_shape = 4
            

            
    
  
    
    
