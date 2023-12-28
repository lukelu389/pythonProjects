# import csv
#
# def getStudentInfo():
#     name = input("Enter the student name: ")
#     student_id = input("Enter the student ID: ")
#     courses = input("Enter the courses that this student takes(use comma to separate): ").split(", ")
#     makes = input("Enter the student marks: ").split()
#
#     return name, student_id, courses, makes
#
#
# student_list = []
# id_list = []
# courses_list = {}
# marks_records = {}
#
# number_of_students = int(input("Enter the same of students: "))
#
# for i in range(number_of_students):
#     name, student_id, courses, marks = getStudentInfo()
#     student_list.append(name)
#     id_list.append(student_id)
#     courses_list[student_id] = courses
#     marks_records[student_id] = marks
#
#
# def write_co_csv(student_list, id_list, courses_list, marks_records):
#     filename = "student_info.csv"
#     with open(filename, "w", newline="") as csvfile:
#         fieldnames = ["Name", "Student ID", "Courses", "Marks"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for i in range(len(student_list)):
#             writer.writerow({
#                 "Name": student_list[i],
#                 "Student ID": id_list[i],
#                 "Courses": ", ".join(courses_list[i]),
#                 "Marks": ", ".join(marks_records[i])
#             })
#
#
# write_co_csv(student_list, id_list, courses_list, marks_records)

import numpy as np
import matplotlib.pyplot as plt


matrix1 = np.random.randint(0, 10, (3, 3))
matrix2 = np.random.randint(0, 10, (3, 2))
matrix_1__2 = np.dot(matrix1, matrix2)
matrix1_trans = matrix1.transpose()
det_matrix1 = np.linalg.det(matrix1)
matrix1_inverse = np.linalg.inv(matrix1)
# E^-1 = 1/detE * adj(E)

plt.matshow(matrix1, cmap="turbo") # inferno, viridis, turbo, magma, cividis, plasma
plt.colorbar()
plt.show()


print(matrix1)
print(matrix2)
print(matrix1_trans)
print(det_matrix1)
print(matrix1_inverse)
print(matrix_1__2)




