#Written by Shiven Desai
#This program modified project 5
number = 0
total = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print(f'The number you entered is {number}.')

main()

def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    return total

add(3, 4, 5)
print(total)
