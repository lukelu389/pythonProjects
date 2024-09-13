# data structures
# dictionary, matrix, string, list, queue, stack, priority queue, graph
# prefix sum array
# recursion, bfs, dfs, binary search, dijkstra, spfa, floyd-warshall

# ccc senior 1
# N = int(input())
# arr1 = [int(input()) for _ in range(N//2)]
# arr2 = [int(input()) for _ in range(N//2)]
# out = 0
#
#
# for i in range(N // 2):
#     if arr1[i] == arr2[i]:
#         out += 2
#
# print(out)

# ccc senior 2
# T, N = list(map(int, input().split()))
# arr = [input() for _ in range(T)]
#
#
# def build_freq(arr):
#     frequency = {}
#     for i in arr:
#         if i in frequency.keys():
#             frequency[i] += 1
#         else:
#             frequency[i] = 1
#     return frequency
#
#
# def heavy_light(string, freq):
#     alt = False
#     for i in range(len(string) - 1):
#         if freq[string[i]] > 1 and freq[string[i + 1]] == 1:
#             alt = True
#
#         elif freq[string[i]] == 1 and freq[string[i + 1]] > 1: alt = True
#
#         else: return False
#
#     return alt
#
#
# for i in arr:
#     freq = build_freq(i)
#     if heavy_light(i, freq): print('T')
#     else: print('F')

# ccc senior 3 2/15
# N = int(input())
# initial = list(map(int, input().split()))
# goal = list(map(int, input().split()))
# if initial == goal:
#     print('YES')
#     print(0)
# else:
#     R = initial.copy()
#     R[1] = R[0]
#     L = initial.copy()
#     L[0] = L[1]
#     if goal == R:
#         print('YES')
#         print(1)
#         print('R', 0, 1)
#     elif goal == L:
#         print('YES')
#         print(1)
#         print('L', 0, 1)
#     else:
#         print('NO')
#
# # ccc senior 3 alternative approach to get partial 0/15
# # we need to find all possible way of swiping
# N = int(input())
# initial = list(map(int, input().split()))
# goal = list(map(int, input().split()))
# if initial == goal:
#     print('YES')
#     print(0)
#
# else:
#     connected = {}
#     current = 0
#     strike = 0
#     for i in range(N):
#         if goal[current] != goal[i]:
#             if goal[current] in connected.keys(): connected[goal[current]].append([i-1])
#             else: connected[goal[current]] = [[current, i-1]]
#             current = i
#             i -= 1
#
#         else:
#             if goal[current] in connected.keys():
#                 temp = connected[goal[current]].pop()
#                 temp[1] = i
#             else: connected[goal[current]] = [[current, i]]
#
#     x = 1
#     for i in range(N):
#         if initial[i] in connected.keys():
#             arr = connected[initial[i]]
#             for j in arr:
#                 if len(j) == 2 and j[0] <= i <= j[1]:
#                     pass
#
#                 elif len(j) == 1 and j[0] == i:
#                     pass
#                 else:
#                     print('NO')
#                     x = 0
#                     break
#             if not x: break
#
#     if x: print('YES')
#
#
# def swipeL(arr, i):
#     arr = [str(_) for _ in arr]
#     outcome = []
#     for j in range(len(arr)):
#         temp = arr[:j] + arr[j:i] + arr[i:]
#         temp = list(map(int, temp))
#         outcome.append(temp)
#
#
# def swipeR(arr, i):
#     arr = [str(_) for _ in arr]
#     outcome = []
#     for j in range(len(arr)):
#         temp = arr[:i] + arr[i:j] + arr[j:]
#         temp = list(map(int, temp))
#         outcome.append(temp)
#
#
# visited = []  # List for visited nodes.
# queue = []  # Initialize a queue
#
#
# def bfs(visited, graph, node):  # function for BFS
#     visited.append(node)
#     queue.append(node)
#
#     while queue:  # Creating loop to visit each node
#         m = queue.pop(0)
#         print(m, end=" ")
#
#         for neighbour in graph[m]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
#
# ccc senior 4
# N, M = list(map(int, input().split()))
# times = [list(map(int, input().split())) for _ in range(M)]
# g = []
#
# for a, b in times:
#     g[a] = b
#     g[b] = a
#
# visit = []  # List for visited nodes.
# queue = []  # Initialize a queue
#
#
# def bfs(visited, graph, node):  # function for BFS
#     s = ""
#     visited.append(node)
#     queue.append(node)
#     if s[len(s) - 1] == "R":
#         s += "B"
#     else:
#         s += "R"
#
#     while queue:  # Creating loop to visit each node
#         m = queue.pop(0)
#         for neighbour in graph[m]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
#
#
# print(bfs(visit, g, 1))

# ccc senior 5
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x = 0

if sum(arr[0]) == arr[1][0] == arr[1][1] or sum(arr[1]) == arr[0][0] == arr[1][1] or arr[0][0] + arr[1][0] == arr[1][1] == arr[0][1] or arr[1][1] + arr[0][1] == arr[0][0] == arr[1][0]:
    x = max(x, 3)
if (arr[0][0] + arr[0][1]) == (arr[1][0] + arr[1][1]) or (arr[0][0] + arr[1][0]) == (
        arr[0][1] + arr[1][1]):
    x = max(x, 2)
if sum(arr[0]) + arr[1][0] == arr[1][1] * 3 or sum(arr[0]) + arr[1][1] == arr[1][0] * 3 or sum(arr[1]) + arr[0][0] == arr[0][1] * 3 or sum(arr[1]) + arr[0][1] == arr[0][0] * 3:
    x = max(x, 2)
if arr[0][0] == arr[0][1] == arr[1][0] == arr[1][1]:
    x = max(x, 4)

print(x)

