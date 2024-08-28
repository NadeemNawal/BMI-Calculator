# BMI calculator
system = input("which measurements would you like to use? \n Type 'm' for metric (kg/ m) or 'i' for imperial (lb/ in) ")

if system == ("m"):
    weight = float(input("Enter your weight in kg."))
    height = float(input("Enter your height in m."))
    bmi = weight / height ** 2  # weight/ height square

elif system == ("i"):
    weight = float(input("Enter your weight in pounds."))
    height = float(input("Enter your height in inches."))
    bmi = weight / (height ** 2)*703  # weight/ height square x 703

if bmi < 18.5:  
    print("You're under weight")

elif bmi < 25:  
    print("Your weight is normal")

elif bmi < 30:
    print("You're overweight")

elif bmi < 35:
    print("You're obese")

else:
    print("you're clinically obese")
