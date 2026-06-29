# Patient BMI Calculator
print("Healthcare BMI Calculator")
print("-------------------------")

print("Please enter your first and last name")
name = input("Patient Name: ")

print("Choose units:")
print("1. Metric (kg/m)")
print("2. Imperial (lbs/in)")

unit_choice = input("Enter 1 or 2: ")

# height = float(input("Height (meters): "))
# weight = float(input("Weight (kg): "))

if unit_choice == "1":
    height = float(input("Height (meters): "))
    weight = float(input("Weight (kg): "))
    bmi = weight / (height ** 2)

elif unit_choice == "2":
    height = float(input("Height (in): "))
    weight = float(input("Weight (lbs): "))
    bmi = (weight * 703) / (height ** 2)

else:
    print("Invalid choice. Please restart and enter 1 or 2.")
    exit()

# The BMI formuala was created with metric system but because I am from the US I will be using a modified formula for lbs and inches

bmi = weight / (height ** 2)

print()
print("Patient:", name)
print("BMI:", round(bmi, 2))
