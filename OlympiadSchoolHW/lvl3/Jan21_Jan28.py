# # ccc 2014 s1
#
# invitee = int(input())
# rounds = int(input())
# commands = [int(input()) for i in range(rounds)]
#
# people = [i for i in range(1, invitee+1)]
#
# for i in commands:
#     temp = []
#     for j in range(len(people)):
#         if (j+1) % i != 0:
#             temp.append(people[j])
#
#     people = temp
#
# for i in people:
#     print(i)
import heapq

# # ccc 2014 s2
# people = int(input())
# group1 = input().split()
# group2 = input().split()
#
# good = 1
# dic = {}
# for i in range(people):
#     p1 = group1[i]
#     p2 = group2[i]
#     if p1 == p2:
#         good = 0
#     if p1 in dic and dic[p1] != p2:
#         good = 0
#     dic[p1] = p2
#     dic[p2] = p1
#
# if good:
#     print("good")
# else:
#     print("bad")

# # ccc 2005 j4
#
# col = int(input())
# row = int(input())
# removal_col = int(input())
# removal_row = int(input())
# moves = int(input())
#
# grid = [[0] * col for i in range(row)]
#
# # remove corners
# for i in range(removal_row):
#     for j in range(removal_col):
#         grid[i][j] = 1
#
# for i in range(row - removal_row, row):
#     for j in range(removal_col):
#         grid[i][j] = 1
#
# for i in range(removal_row):
#     for j in range(col - removal_col, col):
#         grid[i][j] = 1
#
# for i in range(row - removal_row, row):
#     for j in range(col - removal_col, col):
#         grid[i][j] = 1
#
# x = 0
# y = removal_col
# direction = 1
# grid[x][y] = 1
# # 1 goes to north
# # 2 goes south
# # 3 goes east
# # 4 goes west
#
#
# for times in range(moves):
#     if direction == 1:
#         # up
#         if x - 1 > -1 and grid[x - 1][y] != 1:
#             x -= 1
#             direction = 4
#             grid[x][y] = 1
#         # right
#         elif y + 1 < col and grid[x][y + 1] != 1:
#             y += 1
#             grid[x][y] = 1
#         # down
#         elif x + 1 < row and grid[x + 1][y] != 1:
#             x += 1
#             grid[x][y] = 1
#             direction = 3
#         else:
#             break
#
#     elif direction == 3:
#         # right
#         if y + 1 < col and grid[x][y + 1] != 1:
#             y += 1
#             grid[x][y] = 1
#             direction = 1
#         # down
#         elif x + 1 < row and grid[x + 1][y] != 1:
#             x += 1
#             grid[x][y] = 1
#         # left
#         elif y - 1 > -1 and grid[x][y - 1] != 1:
#             y -= 1
#             grid[x][y] = 1
#             direction = 2
#         else:
#             break
#
#     elif direction == 2:
#         # down
#         if x + 1 < row and grid[x + 1][y] != 1:
#             x += 1
#             grid[x][y] = 3
#         # left
#         elif y - 1 > -1 and grid[x][y - 1] != 1:
#             y -= 1
#             grid[x][y] = 1
#         # up
#         elif x - 1 > -1 and grid[x - 1][y] != 1:
#             x -= 1
#             direction = 4
#             grid[x][y] = 1
#         else:
#             break
#
#     elif direction == 4:
#         # left
#         if y - 1 > -1 and grid[x][y - 1] != 1:
#             y -= 1
#             grid[x][y] = 1
#             direction = 2
#         # up
#         elif x - 1 > -1 and grid[x - 1][y] != 1:
#             x -= 1
#             grid[x][y] = 1
#         # right
#         elif y + 1 < col and grid[x][y + 1] != 1:
#             y += 1
#             grid[x][y] = 1
#             direction = 1
#         else:
#             break
#
# print(y+1)
# print(x+1)


# # ccc 2023 j5
# word = list(input())
# rows = int(input())
# cols = int(input())
#
# grid = []
# count = 0
#
# for i in range(rows):
#     grid.append(input().split())
#
#
# def search(d, x, y, dx, dy, turned=False):
#     global count
#     if x < 0 or x >= rows or y < 0 or y >= cols:
#         return
#     if word[d] != grid[x][y]:
#         return
#     if d == len(word) - 1:
#         count += 1
#         return
#
#     search(d + 1, x+dx, y+dy, dx, dy, turned)
# #   just in case need to turn right angle
#     if not turned and d >= 1:
#         search(d + 1, x - dy, y + dx, -dy, dx, True)
#         search(d + 1, x + dy, y - dx, dy, -dx, True)
#
#
# for i in range(rows):
#     for j in range(cols):
#         if word[0] == grid[i][j]:
#             search(0, i, j, -1, -1)
#             search(0, i, j, -1, 0)
#             search(0, i, j, -1, 1)
#             search(0, i, j, 0, -1)
#             search(0, i, j, 0, 1)
#             search(0, i, j, 1, -1)
#             search(0, i, j, 1, 0)
#             search(0, i, j, 1, 1)
# print(count)

# single source shortest path in dijkstra_addEdge.py

import sys
inputs = sys.stdin.readline
N, M = int(input()), int(input())

adj = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a][b] = adj[b][a] = c

pen = []
for _ in range(int(input())):
    pen.append(list(map(int, input().split())))

dest = int(input())

dis, vis = [float('inf')] * (N+1), [False]*(N+1)

dis[dest] = 0
for _ in range(N):
    mindis, u = float('inf'), -1
    for i in range(1, N+1):
        if not vis[i] and dis[i] < mindis:
            mindis, u = dis[i], i
    if u == -1:break
    vis[u] = True
    for v in range(1, N+1):
        if adj[u][v] and dis[u] + adj[u][v] < dis[v]:
            dis[v] = dis[u] + adj[u][v]

ans = float('inf')
for u, x in pen:
    ans = min(ans, dis[u] + x)
print(ans)

