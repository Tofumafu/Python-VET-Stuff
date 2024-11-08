#Input Name
student_name = input("Enter Student's Full Name: ")

#Input Scores 
maths = float(input("Enter Marks in Maths out of 100: "))
english = float(input("Enter Marks in English out of 100: "))
science = float(input("Enter Marks in Science out of 100: "))
economics = float(input("Enter Marks in Economics out of 100: "))
history = float(input("Enter Marks in History out of 100: "))

#Calculation: Adding 
subjects = [maths, english, science, economics, history]
grade_overall = sum(subjects)

#Calculation: Percentage
percentage = (grade_overall / 500) * 100

#Determine: Grades 
if 91 <= percentage <= 100:
        grade = "A1"
elif 81 <= percentage <= 90:
        grade = "A2"
elif 71 <= percentage <= 80:
        grade = "B1"
elif 61 <= percentage <= 70:
        grade = "B2"
elif 51 <= percentage <= 60:
        grade = "C1"
elif 41 <= percentage <= 50:
        grade = "C2"
elif 33 <= percentage <= 40:
        grade = "D"
elif 21 <= percentage <= 32:
        grade = "E1"
else:
        grade = "E2"
 
#Output 
print("Name: ", student_name)
print("Total Marks out of 500: ", grade_overall)
print("Percentage: ", percentage)
print("Grade: ", grade)