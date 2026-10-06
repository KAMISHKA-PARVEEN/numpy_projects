import numpy as np

#storing daat as numpy array
#students' name:

names = np.array(["Jacob", "Kendall", "Kylie", "Kim", "Gigi", "Stormi", "Zayn", "Khloe", "Hailey", "Kourtney"])
print(names)

subjects = np.array(["Automata", "DSA", "COA", "CN", "OOPS"])

marks = np.array([
    [45, 87, 89, 88, 94],
    [34, 93, 77, 62, 66],
    [78, 89, 98, 79, 54],
    [23, 70, 65, 57, 82],
    [56, 88, 90, 65, 67],
    [63, 76, 88, 50, 64],
    [45, 44, 60, 55, 77],
    [76, 65, 81, 91, 86],
    [50, 51, 93, 40, 42],
    [76, 64, 65, 62, 66]
])

#number of students
no_of_students = names.size
print(no_of_students)

#number of subjects
no_of_subjects = subjects.size
print(no_of_subjects)

#dimensionality of marks
print(marks.ndim)

#shape of marks
print(marks.shape)

#total marks stored 
print(marks.size)

#total of marks for each student
total = marks.sum(axis = 1)
print(total)

#average of marks for each student
avg = total/5
print(avg)

#highest marks of each student
highest_marks = marks.max(axis = 1)
print(highest_marks)

#lowest marks of each student
lowest_marks = marks.min(axis = 1)
print(lowest_marks)

# marks >= 40(in every subject) - pass, else - fail 
passed = np.all(marks >= 40, axis = 1)
print(passed)



