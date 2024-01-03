#BMI Calculate
#BMI = weight / height * height

#Input
weight = int(input("Enter your Weight (kg) : "))
height = int(input("Enter your height (cm) : "))

#process
#cm=>m
height = height/100
#calculate
bmi = weight /( height * height)

#output
print("BMI = " ,bmi)

