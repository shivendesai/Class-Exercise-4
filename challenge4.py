#Written by Shiven Desai
#This program modifies project 5 more
num1 = 0
num2 = 0
num3 = 0
total = 0
average = 0

def main():
    global num1, num2, num3
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    calculate()

def calculate():
    global total, average
    total = num1 + num2 + num3
    average = total / 3
    show_result()

def show_result():
    print(f'The sum of the three numbers is {total}.')
    print(f'The average of the three numbers is {average}.')

main()
