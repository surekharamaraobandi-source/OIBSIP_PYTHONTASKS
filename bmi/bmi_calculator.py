def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal Weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight <= 0 or height <= 0:
        print("Please enter valid positive values.")
    else:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print("\n----- BMI RESULT -----")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

except ValueError:
    print("Invalid input! Please enter numeric values.")