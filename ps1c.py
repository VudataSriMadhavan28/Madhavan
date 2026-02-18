# All Inputs 
startingsalary = float(input("Enter the starting salary: "))
total_cost = 1000000
down_payment = 0.25 * total_cost
semiannual_raise = 0.07
annualreturn = 0.04
months = 36

# Bisection search method
low = 0
high = 10000 
steps = 0
best_rate = None

# Using Function method to calculate savings in 36 months
def savings_after_36(rate):
    current_savings = 0
    annual_salary = startingsalary
    monthly_salary = annual_salary / 12
    monthly_return = annualreturn / 12
    
    for m in range(1, months + 1):
        current_savings += current_savings * monthly_return
        current_savings += monthly_salary * rate
        
        if m % 6 == 0:
            annual_salary += annual_salary * semiannual_raise
            monthly_salary = annual_salary / 12
    
    return current_savings

#  impossible case 
if savings_after_36(1.0) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000
        
        savings = savings_after_36(rate)
        diff = savings - down_payment
        
        if abs(diff) <= 100:
            best_rate = rate
            break
        elif savings < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)
