# I Husam Abdelhalim, 000104532, certify that this work is my own effort and
# that I have not allowed anyone else to copy from it.

# Question 2 




def companysales(SalesData):
     
     Sales_total = sum(sale[2]for sale in SalesData)
     companysales = Sales_total / len(SalesData)
     
     return companysales



def salesperson(SalesData):
     
     max_sales = SalesData[0][2]
     
     for x in SalesData:
         
          if x[2] > max_sales:
               
               max_sales = x[2]
               
               return x 

     return salesperson

SalesData = [["Hamilton", "Dave", 1446.56], ["Toronto", "Hetal", 2345.12],
["Mississauga", "Tony", 2032.80], ["Burlinton", "Michelle", 1820.62],
["Oakville", "Donnie", 1282.09]]


Sales_variable = salesperson(SalesData)
Sale_company = round(companysales(SalesData), 2)

print("The average sales for all locations is: $" + str(Sale_company))
print("Congradulations, " + str(Sales_variable) + ". You are eligible for a bonus!")



