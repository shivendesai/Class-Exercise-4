#Written by Shiven Desai
#This program uses a function to enter their details
def get_user_info():
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = input("Enter your zip code: ")
    print("Last name:", last_name)
    print("First name:", first_name)
    print("Address:", address)
    print("City:", city)
    print("State:", state)
    print("Zip code:", zip_code)

get_user_info()
