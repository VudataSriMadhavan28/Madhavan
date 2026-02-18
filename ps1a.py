#All Inputs
annualsalary = float(input("Enter your annual salary: "))
saved = float(input("Enter the percent of your salary to save (decimal): "))
total_cost = float(input("Enter the cost of your dream home: "))

#Fi nding the down payment 
down_payment = 0.25 * total_cost
annualreturn = 0.04
savings = 0
monthlysalary = annualsalary / 12
monthlyreturn = annualreturn / 12
months = 0
#finding the no of months to buy his dream house
while savings < down_payment:
   
   current_savings = current_savings + (savings * monthlyreturn)
   current_savings = current_savings + (monthlysalary * saved)
   months = months + 1
print("Number of months:", months)
