height=(int(input("Enter your height (cm):")))
weight=(int(input("Enter your weight (kg):")))
height_m = height/100

BMI = weight / (height_m **2)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
