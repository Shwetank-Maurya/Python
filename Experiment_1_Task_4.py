# Student Name: Shwetank Maurya
# Roll Number : 2024UG3018
# Course Name and Code: CS-2101/CD-2101-Python Programming Lab
# Task- Create a Program to add,substract,multiply complex number
print('-'*40)
first_real = float(input("Enter real part of first complex number: "))
first_imag = float(input("Enter imaginary part of first complex number: "))
second_real = float(input("Enter real part of second complex number: "))
second_imag = float(input("Enter imaginary part of second complex number: "))
c1 = complex(first_real,first_imag)
c2 = complex(second_real,second_imag)
sum = c1 + c2
diff = c1 - c2
prod = c1 * c2
print('-'*40)
print("First Complex Number:",c1)
print("Second Complex Number:",c2)
print('-'*40)
print("Sum:",sum)
print("Difference:",diff)
print("Product:",prod)
print('-'*40)