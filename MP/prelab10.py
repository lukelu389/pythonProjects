"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Pre Lab Assignment #10
"""

# Q1
# v = [1, 2, 3, 4, 5]
# n = len(v)
# y = 1
# for i in range (n):
#     y += v[i]**2
# print(y)


# Q2
# matrix2d = [[1, 3, 8, 3], [6, 5, 4, 9], [7, 2, 9, 10]]
# output = 0
# for i in range(len(matrix2d)):
#     for j in range(len(i)):
#         output += matrix2d[i][j]
#
# print(output)

# not nested way, shorter but same time complexity
# for i in range(len(matrix2s)):
#   output += sum(i)

# Q3 modified code
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
counter = 0
for h in range(hours_in_day):
    for m in range(minutes_in_hour):
        for s in range(seconds_in_minute):
            counter += 1
            print("loop " +str(counter))
            print(f"{h:02d}:{m:02d}:{s:02d}")

# the print statement will run 24*60*60 times
