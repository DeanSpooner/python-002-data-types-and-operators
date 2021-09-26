weight = int(input("What is your weight in kg? "))
height = int(input("What is your height in cm? "))

height = height / 100

bmi = weight / height ** 2

print("Your BMI is: " + str(round(bmi, 1)))

# round(num, dp) rounds a float to the nearest integer (if dp = 0 or not given), or to the specified decimal place (dp)
