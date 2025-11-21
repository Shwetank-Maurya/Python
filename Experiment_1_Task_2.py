# Student Name: Shwetank Maurya
# Roll Number : 2024UG3018
# Course Name and Code: CS-2101/CD-2101-Python Programming Lab
# Task- Create a Program to compute marks and assign grades to the marks.

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
n = int(input("Enter number of subjects: "))
marks =0
for i in range(n):
    score = float(input(f"Enter marks for subject {i+1}: "))
    marks=marks+score
average = marks / n
grade = calculate_grade(average)
print(f"\nAverage Marks: {average:.2f}")
print(f"Grade: {grade}")
