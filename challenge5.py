#Written by Shiven Desai
#This program gets hours and hourly pay
def calculate_pay(hours_worked, hourly_rate):
    total_pay = hours_worked * hourly_rate
    return total_pay

hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate: "))

total = calculate_pay(hours, rate)
print(f"The total pay is {total:.2f} dollars.")
