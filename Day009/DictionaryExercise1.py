student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Don't change the code above
#TODO-1: Create an empty dictionary called student_grades.
#TODO-2: Write your code below to add the grades to student_grades.
def get_grade(score):
    if score <= 70:
        return "Fail"
    elif score <= 80:
        return "Acceptable"
    elif score <= 90:
        return "Exceeds Expectations"
    elif score <= 100:
        return "Outstanding"
    else:
        return "Invalid Grade"
    
student_grades = {}
for key in student_scores:
    student_grades[key] = get_grade(student_scores[key])


# Don't change the code below
print(student_grades)