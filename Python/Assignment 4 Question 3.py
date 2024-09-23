# I Husam Abdelhalim, 000104532, certify that this work is my own effort and
# that I have not allowed anyone else to copy from it.

# Question 3


def checkFormat(is_number):
   
    length = len(is_number)

    if length == 14 and is_number[0] == "(" and is_number[4] == ")" and is_number[5] == " " and is_number[9] == "-":

        if is_number[1:4].isdecimal() and is_number[6:9].isdecimal() and is_number[10:14].isdecimal():
               

            return True
   
    else:

        return True
   
   
def verifyAreaCode(is_number):
   
    cityList =[["Hamilton", 905],["Ottawa", 613],["Montreal", 514],["Halifax", 782]]
    area = 0
    area_code = is_number[1:4]
   
    area_code = int(area_code)

   
    for city in cityList:
        if area_code == city[1]:
           
            city = True
           
            return city
           
        else:
           
            city = False
           
        area = area + 1
       
    return city
           
       

   
is_number = input("Give me a phone number ")
is_valid = checkFormat(is_number)

if is_valid is True:
   
    is_area = verifyAreaCode(is_number)
   
    print("Format OK")
   
    if is_area == True:
       
        print("Valid Area code")
       
    else:
        print("Invalid Area code")
   
else:
    print("Format Error")
