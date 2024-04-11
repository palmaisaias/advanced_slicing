#DEEP DIVE INTO LISTS
#TASK 1: GIVEN THE LISTS

students = ['John', 'Doe', 'Jane', 'Smith']
grades = [85, 90, 78, 88]
activities = ['Football', 'Music', 'Art', 'Dance']

name = students.pop(2)
grade = grades.pop(2)
activity = activities.pop(2)

print(name,',', grade,',', activity)

#TASK 2

students_approved = students[:]

print(students_approved)