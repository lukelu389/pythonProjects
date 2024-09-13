# # CCC 2024 j4
#
# typed = input()
# output = input()
#
# if len(typed) == len(output):
#     for i in range(len(typed)):
#         if typed[i] != output[i]:
#             print(typed[i], output[i])
#             print("-")
#             break
#
# else:
#     dif = list(set(typed).difference(set(output)))  # char that output don't have
#     missing = set(output).difference(set(typed)).pop()  # char that typed don't have
#
#     acopy = list(typed).copy()
#     for i in range(len(typed)):
#         if acopy[i] == dif[0]:
#             acopy[i] = missing
#         elif acopy[i] == dif[1]:
#             acopy[i] = " "
#
#     if "".join(acopy).replace(" ", "") == output:
#         print(dif[0], missing)
#         print(dif[1])
#
#     else:
#         print(dif[1], missing)
#         print(dif[0])

# CCC 2024 j5 tle py ac java
# r = int(input())
# c = int(input())
# grid = [list(input()) for _ in range(r)]
# s, m, l = 0, 0, 0
#
#
# x = int(input())
# y = int(input())
# visited = []
#
#
# def find_pumpkin(ix, iy):
#     global visited
#     global s, m, l
#     if ix == r or ix == -1: return 0
#     if iy == c or iy == -1: return 0
#     if grid[ix][iy] == "*": return 0
#     if (ix, iy) in visited: return 0
#
#     if grid[ix][iy] == "L":
#         l += 10
#     if grid[ix][iy] == "M":
#         m += 5
#     if grid[ix][iy] == "S":
#         s += 1
#     visited.append((ix, iy))
#
#     return find_pumpkin(ix - 1, iy) + find_pumpkin(ix + 1, iy) + find_pumpkin(ix, iy + 1) + find_pumpkin(ix, iy - 1)
#
#
# find_pumpkin(x, y)
# print(sum([s, m, l]))

# 2024 ccc senior 3
# words = int(input())
# initial = list(map(int, input().split()))
# expected = list(map(int, input().split()))
# t = initial.copy()
# l_swaps = []
# r_swaps = []
# j = 0
# temp = []
# for i in range(words):
#     temp = [j, i]
#     while j < words:
#         if initial[i] != expected[j]: break
#         j += 1
#
#     temp[1] = j - 1
#     if temp[0] == temp[1] == i:
#         pass
#     elif temp[0] < i < temp[1]:
#         l_swaps.append((temp[0], i))
#         r_swaps.append((i, temp[1]))
#     elif i <= temp[0] <= temp[1]:
#         r_swaps.append((i, temp[1]))
#     elif temp[0] <= temp[1] <= i:
#         l_swaps.append((temp[0], i))
#
#
# def swap(arr, s, i, j):
#     if s =="R":
#         key = arr[i]
#         for w in range(i, j+1):
#             arr[w] = key
#     else:
#         key = arr[j]
#         for w in range(i, j+1):
#             arr[w] = key
#
#     return arr
#
#
# if initial == expected:
#     print('YES')
#     print('0')
#
# elif len(r_swaps) == len(l_swaps) == 0:
#     print('NO')
#
# else:
#     l_swaps.sort()
#     r_swaps.sort()
#     r = r_swaps.copy()
#     for i in l_swaps:
#         t = swap(t, "L", i[0], i[1])
#
#     for i in range(len(r_swaps)):
#         temp = r.pop()
#         t = swap(t, "R", temp[0], temp[1])
#
#     if t == expected:
#         print('YES')
#         print(len(l_swaps) + len(r_swaps))
#         for i in l_swaps:
#             print("L", i[0], i[1])
#
#         for i in range(len(r_swaps)):
#             temp = r_swaps.pop()
#             print('R', temp[0], temp[1])
#
#     else: print('NO')
#


# N, T = map(int, input().split())
# v = [[0] * 3 for _ in range(2001)]
# t = [[0] * 3 for _ in range(2001)]
# dp = [0] * 10001
#
# for i in range(1, N + 1):
#     temp = list(map(int, input().split()))
#     t[i] = [temp[0], temp[2], temp[4]]
#     v[i] = [temp[1], temp[3], temp[5]]
#
#
# for j in range(1, N + 1):
#     for i in range(T, -1, -1):
#         for k in range(3):
#             if i >= t[j][k]:
#                 dp[i] = max(dp[i], dp[i - t[j][k]] + v[j][k])
#
# print(dp[T])

from sys import stdin

N, T = map(int, stdin.readline().split())
v = [[0] * 3 for _ in range(N + 1)]
t = [[0] * 3 for _ in range(N + 1)]
dp = [0] * (T + 1)

for i in range(1, N + 1):
    temp = list(map(int, stdin.readline().split()))
    t[i] = temp[0:5:2]
    v[i] = temp[1:6:2]

for j in range(1, N + 1):
    for i in range(T, t[j][0] - 1, -1):
        for k in range(3):
            if i >= t[j][k]:
                dp[i] = max(dp[i], dp[i - t[j][k]] + v[j][k])

print(dp[T])


