#Basic Sum
num1 = int(input("Input a number: "))
num2 = int(input("Input another number: "))
sum = num1+num2
print ("The sum of them is: ", sum)

#Odd or even ?
num3 = int(input("Input a number: "))
if num3 % 2 == 0:
    print ("Your number is even.")
else:
    print ("Your number is odd.")

#Swapping 2 variables without using a 3rd one
num1 = 4
num2 = 1
print ("Number one before swap: ", num1,"\nNumber two before swap: ", num2)
num1, num2 = num2, num1
print ("Number one after swap: ", num1,"\nNumber two after swap: ", num2)

#Area of a circle
cradius = float(input("What is the radius of the circle ? "))
from cmath import pi
carea= pi*cradius**2
print ("The rounded area of the circle is:", round(carea, 2))


#Celsius to Fahrenheit
truthtest=1
while (truthtest):
    tempchoice = input("Do you want to star with Celsius (C) or Fahrenheit (F) ?")
    if tempchoice == "C" or tempchoice == "c":
        temperatureCel = int(input("Tell the temperature in Cº: "))
        temperatureFah = (temperatureCel*9/5)+32
        print (temperatureCel, "C° equals to ", round(temperatureFah,2), "F°.")
        truthtest=0
    elif tempchoice == "F" or tempchoice == "f": 
        temperatureFah = int(input("Tell the temperature in Fº: "))
        temperatureCel = (temperatureFah-32)*5/9
        print (temperatureFah, "F° equals to ", round(temperatureCel,2), "C°.")
        truthtest=0
    else :
        print ("Try again!")
    