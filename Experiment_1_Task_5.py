# Student Name: Shwetank Maurya
# Roll Number : 2024UG3018
# Course Name and Code: CS-2101/CD-2101-Python Programming Lab
# Task- Create a Program to convert temperature(celcius and Farenheit)

print('-'*40)
print("Temperature Conversion")
good=True

while(good):
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. EXIT")
    print('-'*40)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        f = (9/5)*c+32
        print("The converted degree in Fahrenheit is :",f," F")
    elif choice == 2:
        ff = float(input("Enter temperature in Fahrenheit: "))
        cc = (5/9)*(ff-32)
        print("The converted fahrenheit in degree is :",cc," C")
    elif choice==3:
        print("BYE BYE")
        good=False
    else:
        print('-'*40)
        print("Invalid CHoice ")
        print('-'*40)
