#exchange money

number = int(input("Enter Amount : "))

if number >= 1000:
    print("1000 Baht = ",number//1000)
    number=number%1000
if number >=500:
    print("500 baht = ",number//500)
    number=number%500
if number >=100:
    print("100 baht = ",number//100)
    number=number%100
if number >=50:
    print("50 baht = ",number//50)
    number=number%50