#All Inputs
annualsalary = float(input("Enter your starting annual salary: "))
saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semiannual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
#Finding down payment
down_payment = 0.25 * total_cost
annualreturn = 0.04
savings = 0
monthlysalary = annualsalary / 12
monthlyreturn = annualreturn / 12
months = 0
#finding the no of months to buy his dream house
while savings < down_payment:
    savings += savings * monthlyreturn

    savings += monthlysalary * saved

    months += 1
    if months % 6 == 0:
        annualsalary += annualsalary * semiannual_raise
        monthlysalary = annualsalary / 12
print("Number of months:", months)
   
    
    
   
    
    
  
    
 
    



