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
avg_stu = total/5
print(avg_stu)

#highest marks of each student
highest_marks = marks.max(axis = 1)
print(highest_marks)

#lowest marks of each student
lowest_marks = marks.min(axis = 1)
print(lowest_marks)

# marks >= 40(in every subject) - pass, else - fail 
passed = np.all(marks >= 40, axis = 1)
print(passed)


result = np.where(passed, 'Pass', 'Fail')
print(result)

#avg of every subject for all studnets
avg_sub = marks.sum(axis = 0)/10
print(avg_sub)

highest_marks_sub = marks.max(axis = 0)
print(highest_marks_sub)

lowest_marks_sub = marks.min(axis = 0)
print(lowest_marks_sub)

greater_90 = marks > 90
print(greater_90)

greater_90_count = greater_90.sum(axis = 0)
print(greater_90_count)

below_40 = marks < 40
print(below_40)

below_40_count = below_40.sum(axis = 0)
print(below_40_count)

max_avg = avg_sub.max()
print(max_avg)

idx = np.where(avg_sub == max_avg)
print(subjects[idx])

class_avg = marks.sum()/(no_of_students*no_of_subjects)
print(class_avg)

class_highest_marks = marks.max()
print(class_highest_marks)

class_lowest_marks = marks.min()
print(class_lowest_marks)

total_passed = passed.sum()
total_failed = no_of_students - total_passed

print("Total students passed are " + str(total_passed))
print("Total students failed are " + str(total_failed))

pass_percentage = (total_passed/no_of_students)*100
print("Pass percentage " + str(pass_percentage) + "%")

