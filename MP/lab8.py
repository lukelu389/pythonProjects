"""
Xiao Lu
420-SN1 Programming, Section #21
Winter 2025
J. Gullifer, instructor
Lab Assignment #8
"""

# temps = [-8.7, -11.7, -0.4, -4.0, -12.8, 0.6, 0.4, -5.5, -4.2, -6.2]
# ntemps = len(temps)
# ix=0
# while ix < ntemps:
#     print(ix, temps[ix])
#     ix+=1
# 0 -8.7
# 1 -11.7
# 2 -0.4
# 3 -4.0
# 4 -12.8
# 5 0.6
# 6 0.4
# 7 -5.5
# 8 -4.2
# 9 -6.2

# temps = [-8.7, -11.7, -0.4, -4.0, -12.8, 0.6, 0.4, -5.5, -4.2, -6.2]
# ntemps = len(temps)
# ix=0
# while ix <= ntemps:
#     temps[ix] = temps[ix] * 9/5 + 32
#     print(ix, temps[ix])
#     ix+=1
#
# print(temps)
# 0 16.34
# 1 10.940000000000001 => round off error
# 2 31.28
# 3 24.8
# 4 8.96
# 5 33.08
# 6 32.72
# 7 22.1
# 8 24.439999999999998 => round off error
# 9 20.84
# [16.34, 10.940000000000001, 31.28, 24.8, 8.96, 33.08, 32.72, 22.1, 24.439999999999998, 20.84]
# 9
# yes because you reassigned the initial temp[ith] with modified temp[ith]
# Runtime Error, ListIndexOutOfBound

# temps = [-8.7, -11.7, -0.4, -4.0, -12.8, 0.6, 0.4, -5.5, -4.2, -6.2]
# for element in temps:
#     print(element)
# -8.7
# -11.7
# -0.4
# -4.0
# -12.8
# 0.6
# 0.4
# -5.5
# -4.2
# -6.2

# temps = [-8.7, -11.7, -0.4, -4.0, -12.8, 0.6, 0.4, -5.5, -4.2, -6.2]
# ntemps = len(temps)
# for ix in range(ntemps):
#     print(ix, temps[ix])

# 0 -8.7
# 1 -11.7
# 2 -0.4
# 3 -4.0
# 4 -12.8
# 5 0.6
# 6 0.4
# 7 -5.5
# 8 -4.2
# 9 -6.2
# no

# temps = [-8.7, -11.7, -0.4, -4.0, -12.8, 0.6, 0.4, -5.5, -4.2, -6.2]
# for index_number in range(len(temps)):
#     temps[index_number] = temps[index_number] * 9/5 + 32
#     print(temps[index_number])
#
# print(temps)

# 0 -8.7
# 1 -11.7
# 2 -0.4
# 3 -4.0
# 4 -12.8
# 5 0.6
# 6 0.4
# 7 -5.5
# 8 -4.2
# 9 -6.2
# yes
