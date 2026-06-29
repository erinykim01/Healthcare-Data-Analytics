# Patient BMI Calculator
print("Healthcare BMI Calculator")
print("-------------------------")

name = input("Patient Name: ")

height = float(input("Height (meters): "))
weight = float(input("Weight (kg): "))

bmi = weight / (height ** 2)

print()
print("Patient:", name)
print("BMI:", round(bmi, 2))
