#PYTHON LIST TRANSFORMATION
#TASK 1

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# grades.sort()     #Normal ascending sort
# print(grades)

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)       #descending sort
print(grades)

#TASK 2
#CALCULATE THE AVERAGE GRADE AND DISPLAY IT.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print()     #Spaces are cosmetic. Output just feels more readable
total = sum(grades)
print('Sum of list is', total)  #sum of all items in list
print()
num_of_grades = len(grades)     #counts the number of items in list
print('There are' ,num_of_grades ,'grades in the list')
print()
avg_grade = total / num_of_grades
print('Average grade is', avg_grade)

#TASK 3
#REPLACE ANY GRADE BELOW 80 WITH THE VALUE FAILED.

    #FIRST attempt. Bad entry logic

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# grades[2, 4, 8] = 'Failed'
# print(grades)

    #SECOND attempt. Did not work. 'Failed' printed as individual letters.

# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# grades.sort(reverse=True)
# grades[7:] = 'Failed'

# print(grades)

    #THIRD attempt
    #Works but I couldnt figure a way to execute it with a single Method.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
grades[6] = 'Failed'
grades[7] = 'Failed'
grades[8] = 'Failed'
grades[9] = 'Failed'

print(grades)