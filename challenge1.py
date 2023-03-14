#Written by Shiven Desai
#This program is an extension of project 3
#This program demonstrates two functions that
#have local variables with the same name.

def main():
    #Call the texas function
    texas()
    #Call the california function
    california()

    #Definition of the texas function. It creates 
    #a local variable named birds.
def texas():
        birds = int(input('Enter the number of birds in texas: '))
        print(f'texas has {birds} birds.')

    #Definition of the california function. It also
    #creates a local variable named birds.
def california():
        birds = int(input('Enter the number of birds in california: '))
        print(f'california has {birds} birds.')

#Call the main function.
main()