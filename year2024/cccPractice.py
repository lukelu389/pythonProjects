import math
# ccc 2019 senior
#
# def h_flip(g):
#     temp = g[0]
#     g[0] = g[1]
#     g[1] = temp
#     return g
#
#
# def v_flip(g):
#     temp = g[0][0]
#     g[0][0] = g[0][1]
#     g[0][1] = temp
#     temp = g[1][0]
#     g[1][0] = g[1][1]
#     g[1][1] = temp
#     return g
#
#
# grid = [[1, 2], [3, 4]]
# command = input()
# for i in command:
#     if i == "H":
#         grid = h_flip(grid)
#     else:
#         grid = v_flip(grid)
#
# print(grid[0][0], " ", grid[0][1])
# print(grid[1][0], " ", grid[1][1])

# ccc 2019 senior 2
# T = int(input())
# arr = [int(input()) for _ in range(T)]
#
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     for i in range(5, int(math.sqrt(n)) + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#     return True
#
#
# for i in arr:
#     temp = []
#     for j in range(2, i):
#         temp = 2 * i - j
#         if is_prime(j) and is_prime(temp):
#             print(j, " ", temp)
#             break

# ccc 2018 s1
# N = int(input())
# arr = [int(input()) for _ in range(N)]
#
# arr.sort()
# neighborhood = []
# for i in range(1, N - 1):
#     neighborhood.append((arr[i] - arr[i-1]) / 2 + (arr[i+1] - arr[i]) / 2)
#
# neighborhood.sort()
# print(neighborhood[0])

# ccc 2017 s2

# import sys
#
# n = int(sys.stdin.readline())
# measurements = list(map(int, sys.stdin.readline().split()))
#
# measurements.sort()
# if n % 2 == 0:
#     lowtides = measurements[:int(n / 2)]
#     hightides = measurements[int(n / 2):]
# else:
#     lowtides = measurements[:(n // 2 + 1)]
#     hightides = measurements[(n // 2 + 1):]
# lowtides.sort(reverse=True)
#
# if n != 1:
#     if n % 2 == 0:
#         for i in range(int(n / 2)):
#             print(lowtides[i], end=' ')
#             print(hightides[i], end=' ')
#     else:
#         for i in range(n // 2 + 1):
#             try:
#                 print(lowtides[i], end=' ')
#                 print(hightides[i], end=' ')
#             except:
#                 pass
# else:
#     print(measurements[0])


# ccc 2017 s3
# N = int(input())
# arr = list(map(int, input().split()))
# wood = [0] * 2001
# board = [0] * 4001
#
# length = 1
# height_cnt = 0
#
# for i in arr:
#     wood[i] += 1
#
# for i in range(1, 2001):
#     if wood[i] != 0:
#         if wood[i] > 1:
#             board[i*2] += int(wood[i]/2)
#
#         for j in range(i+1, 2001):
#             if wood[j] != 0:
#                 board[i+j] += min(wood[i], wood[j])
#
# for i in range(1, 4001):
#     if board[i] > length:
#         length = board[i]
#         height_cnt = 1
#
#     elif board[i] == length:
#         height_cnt += 1
#
# print(length, height_cnt)
#

# ccc 2017 s1
# N = int(input())
# team1 = list(map(int, input().split()))
# team2 = list(map(int, input().split()))
# score1 = 0
# score2 = 0
# temp = 0
#
# for i in range(N):
#     score1 += team1[i]
#     score2 += team2[i]
#     if score1 == score2:
#         temp = i + 1
#
# print(temp)

# ccc 2020 s2
# from collections import deque
# import sys
#
# M = int(input())
# N = int(input())
#
# visited = [False for _ in range(M * N + 1)]
# rooms = [[] for _ in range(M * N + 1)]
#
# for row in range(1, M + 1):
#     for col, val in enumerate(map(int, input().split()), start=1):
#         if val <= M * N:
#             rooms[row * col].append(val)
#
# q = deque([1])
#
# while q:
#     cur = q.popleft()
#     if cur == M * N:
#         print('yes')
#         sys.exit(0)
#
#     for value in rooms[cur]:
#         if not visited[value]:
#             visited[value] = True
#             q.append(value)
#
# print("no")

# ccc 2022 s3
# n, m, k = map(int, input().split())
# ans = []
# for i in range(n):
#     rem = n - i - 1
#     cur = min(k - rem, m)
#     if cur <= 0:
#         break
#     if cur > i: # add distinct
#         val = min(m, i + 1)
#         cur = val
#     else:   # add common
#         val = ans[i - cur]
#     ans.append(val)
#     k -= cur
#
# if k == 0 and len(ans) == n:
#     print(*ans)
# else:
#     print(-1)

# ccc 2013 s3
# favourite = int(input())
# played = int(input())
#
# perms = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# points = [0] * 6
#
#
# def simulate(games_left, pts, game, w):
#     if w == 1: pts[game[0]] += 3
#     elif w == -1: pts[game[1]] += 3
#     elif w == 0:
#         pts[game[0]] += 1
#         pts[game[1]] += 1
#
#     if not games_left:
#         for i in range(1, 5):
#             if i != favourite:
#                 if pts[i] >= pts[favourite]:
#                     return 0
#
#         return 1
#
#     cGame = games_left.pop()
#     return sum([simulate(list(games_left), list(pts), cGame, k) for k in range(-1, 2)])
#                                                                 # this part is for generate all cases:
#                                                                 # -1 is lost, 0 is tie, 1 is won
#
#
# for i in range(played):
#     a, b, s1, s2 = list(map(int, input().split()))
#     if (a, b) in perms:
#         perms.remove((a, b))
#     if s1 > s2: points[a] += 3
#     elif s2 > s1: points[b] += 3
#     else:
#         points[a] += 1
#         points[b] += 1
#
#
# print(simulate(perms, points, [], 2))


# ccc 2013 s2
# limit = int(input())
# cars = int(input())
# arr = [int(input()) for _ in range(cars)]
# out = 0
#
# if cars > 4:
#     for i in range(cars - 3):
#         temp = arr[i] + arr[i+1] + arr[i+2] + arr[i+3]
#         if temp <= limit:
#             out += 1
#         else:
#             break
#
#     if out > 0:
#         print(out+3)
#     else:
#         if arr[0] + arr[1] + arr[2] <= limit: print(3)
#         elif arr[0] + arr[1] <= limit: print(2)
#         elif arr[0] <= limit: print(1)
#         else:print(0)
#
# else:
#     if cars == 1:
#         if arr[0] <= limit: print(1)
#         else: print(0)
#
#     elif cars == 2:
#         if arr[0] + arr[1] <= limit: print(2)
#         else: print(0)
#
#     elif cars == 3:
#         if arr[0] + arr[1] + arr[2] <= limit: print(3)
#         else: print(0)
#
#     elif cars == 4:
#         if arr[0] + arr[1] + arr[2] + arr[3] <= limit: print(4)
#         else: print(0)

# ccc 2008 s3

