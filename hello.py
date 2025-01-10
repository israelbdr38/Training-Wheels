#Basic function make text show up
print("Hello, world!")

#Showing variables mid text
name = "Israel"
age = 29
print (name,"is", age, "years old")

#Receiving text input
username = input("What is your name? ")
print ("Hello,", username)

#Receiving int input and using a condition
userage = int(input("How old are you? "))
if userage >= 18:
    print ("You're an adult!")
else:
    print ("You're a minor!")