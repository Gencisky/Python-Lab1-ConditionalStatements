w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))
bmi=w/(h*h)
if bmi==18.5:
    c="Underweight"
elif 18.5 <= bmi <= 24.9:
    c="Normal Weight"

elif 25.0 <= bmi <= 29.9:
    c="Overweight"
else:
    c="Obese"
print(bmi)
print(c)