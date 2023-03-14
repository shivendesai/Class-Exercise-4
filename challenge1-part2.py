#Written by Shiven Desai
#This program coverts km to miles
def convert_to_miles(km):
    miles = km * 0.6214
    return miles

km = float(input("Enter a distance in kilometers: "))

miles = convert_to_miles(km)
print(f"{km} kilometers is equal to {miles:.2f} miles.")
