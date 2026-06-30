# Patient BMI Calculator
print("Healthcare BMI Calculator")
print("-------------------------")

print("Please enter your first and last name")
name = input("Patient Name: ")

# First idea
# print("Choose units:")
# print("1. Metric (kg/m)")
# print("2. Imperial (lbs/in)")

# unit_choice = input("Enter 1 or 2: ")

# height = float(input("Height (meters): "))
# weight = float(input("Weight (kg): "))
# First idea


# Weight func
def parse_weight(user_input):
    user_input = user_input.lower().strip().replace(" ", "")

# Metric
    if user_input.endswith("kg"):
        weight = float(user_input.replace("kg", ""))
        return weight

# Imperial
    elif user_input.endswith(("lbs", "lb")):
        weight = float(user_input.replace("lbs", "").replace("lb", ""))
        return weight * 0.453592

    else:
        weight = float(user_input)
        return weight * 0.453592


# Height func
def parse_height(user_input):
    user_input = user_input.lower().strip().replace(" ", "")

# Metric
    if user_input.endswith("cm"):
        height = float(user_input.replace("cm", ""))
        return height / 100

    elif user_input.endswith("m"):
        height = float(user_input.replace("m", ""))
        return height

    # Imperial
    elif ("'") in user_input :
        feet, inches = user_input.split("'")
        feet = float(feet)
        inches = float(inches)
        total_inches = (feet * 12) + inches
        height = total_inches * 0.0254
        return height 

    else:
        height = float(user_input)
        return height * 0.0254



weight_input = input("Weight: ")
height_input = input("Height: ")
weight = parse_weight(weight_input)
height = parse_height(height_input)
bmi = weight / (height ** 2)

print()
print("Patient:", name)
print("BMI:", round(bmi, 2))




#------------
#testing area
#------------

# user_input =  '5\'8"'
# feet, inches = user_input.split("'")
# feet = float(feet)
# inches = float(inches.replace("\'", ""))
# print(feet)
# print(inches)

# feet = float(feet)
# inches = float(inches)
# total_inches = (feet * 12) + inches
# height = total_inches * 0.0254
# print(height)