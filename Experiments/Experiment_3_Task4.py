# Define a function highest_grade that accepts a dictionary with student names as keys and their grades as values.
# Use the max() function to find the student with the highest grade.
# Test the function with a sample dictionary.

def highest_grade(grades_dict):
    # max with key=grades_dict.get returns the key (student) with the highest value (grade)
    highest_student = max(grades_dict, key=grades_dict.get)
    return highest_student, grades_dict[highest_student]

# Test the function with a sample dictionary
sample_grades = {"Rakesh":23,"Preet":45,"Child":12,"Rakesh Junior":90}
student, grade = highest_grade(sample_grades)
print(f"The highest grade is {grade}, achieved by {student}.")
