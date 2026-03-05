# BMI Calculator in Python

# Ask for user's name
name = input("Enter your name: ")

# Ask for weight in kilograms
weight = float(input("Enter your weight in kg: "))

# Ask for height in meters
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print(f"\nHello {name}!")
print(f"Your BMI is: {bmi:.2f}")

# Give BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("Category: Normal weight")
elif 25 <= bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obesity")
