"""  Write functions to convert kilometers to meters, meters to centimeters, centimeters to millimeters, feets
to inches, and inches to centimeter. Write a function distance_converter() that takes a distance,
conversion type as a string (e.g. km to m, m to cm, etc.) and a conversion function as argument. This
function does the converion using given function and print the result. Input a distance from user and
print all conversions."""


# Conversion functions
def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

def cm_to_mm(cm):
    return cm * 10

def feet_to_inches(feet):
    return feet * 12

def inches_to_cm(inch):
    return inch * 2.54

def distance_converter(distance, conv_type, func):
    result = func(distance)
    print(f"{distance} {conv_type} = {result}")

# Main

while True:
    print("---------------------------")
    distance = float(input("Enter distance: "))
    
    print("\n---- Calculator Menu ----")
    print("1. Convert kilometers to meters")
    print("2. Convert meters to centimeters")
    print("3. Convert centimeters to millimeters")
    print("4. Convert feets to inches")
    print("5. Convert inches to centimeter")
    print("---------------------------")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            distance_converter(distance, "km to m", km_to_m)
        case 2:
           distance_converter(distance, "m to cm", m_to_cm)
        case 3:
            distance_converter(distance, "cm to mm", cm_to_mm)
        case 4:
            distance_converter(distance, "feet to inches", feet_to_inches)
        case 5:
            distance_converter(distance, "inches to cm", inches_to_cm)
        case _:
          print("Invalid choice!")
    

    