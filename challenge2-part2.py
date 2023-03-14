#Written by Shiven Desai
#This program displays automobile costs
def calculate_total_monthly_cost(loan, insurance, gas, oil, tires, maintenance):
    total_cost = loan + insurance + gas + oil + tires + maintenance
    return total_cost

loan_payment = float(input("Enter monthly loan payment: "))
insurance = float(input("Enter monthly insurance cost: "))
gas = float(input("Enter monthly gas cost: "))
oil = float(input("Enter monthly oil cost: "))
tires = float(input("Enter monthly tire cost: "))
maintenance = float(input("Enter monthly maintenance cost: "))

total_monthly_cost = calculate_total_monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance)
total_annual_cost = total_monthly_cost * 12

print(f"The total monthly cost of these expenses is {total_monthly_cost:.2f} dollars.")
print(f"The total annual cost of these expenses is {total_annual_cost:.2f} dollars.")
