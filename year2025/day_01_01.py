# import sys
# sys.setrecursionlimit(300000)
#
# N, M = list(map(int, input().split()))
# adj = [[] for i in range(N + 1)]
# path = ["G"] * M
#
# for i in range(M):
#     u, v = list(map(int, input().split()))
#     adj[u].append([v, i])
#     adj[v].append([u, i])
#
# visited = [False] * (N + 1)
#
#
# def dfs(node, state):
#     for height, index in adj[node]:
#         if visited[height]:
#             continue
#         visited[height] = True
#         if path[index] == "G":
#             if state == 0:
#                 path[index] = "R"
#             else:
#                 path[index] = "B"
#
#         dfs(height, state ^ 1)
#
#
# for n in range(1, N+1):
#     if not visited[n]:
#         visited[n] = True
#         dfs(n, 0)
#
# print("".join(path))
#
# import copy
#
# ipt = ""
# roads = []
# chart = {}
# pathways = []
# duplicates = []
#
# while ipt != "**":
#     ipt = input()
#     if ipt != "**":
#         roads.append(ipt)
#
# for road in roads:
#     if road[0] not in chart:
#         chart[road[0]] = [road[1]]
#     else:
#         chart[road[0]].append(road[1])
#     if road[1] not in chart:
#         chart[road[1]] = [road[0]]
#     else:
#         chart[road[1]].append(road[0])
#
#
# # find all paths
# def bfs(road):
#     graph = copy.deepcopy(chart)
#     graph[road[0]].remove(road[1])
#     graph[road[1]].remove(road[0])
#     queue = ["A"]
#     explored = []
#     while queue:
#         node = queue.pop(0)
#         if node not in explored:
#             explored.append(node)
#             neighbours = graph[node]
#             for neighbour in neighbours:
#                 queue.append(neighbour)
#                 if neighbour == "B":
#                     return 0
#     return 1
#
#
# total = 0
# sucess = []
# for road in roads:
#     temp = bfs(road)
#     if temp == 1:
#         total += 1
#         sucess.append(road)
#
# for element in sucess:
#     print(element)
# print("There are " + str(total) + " disconnecting roads.")

# def solve():
#     N = int(input())
#     H = list(map(int, input().split()))
#     if H[-1] != 1:
#         print(-1)
#         return
#     H = H[:-1]
#     remaining = [False] + [True] * N
#     for h in H:
#         if not remaining[h]:
#             print(-1)
#             return
#         remaining[h] = False
#     ends = [x for x in range(1, N + 1) if remaining[x]]
#     ans = [-1] * N
#     l, r = 0, N - 1
#     ans[l], ans[r] = ends
#     for h in H:
#         if ans[l] > ans[r]:
#             l += 1
#             ans[l] = h
#         else:
#             r -= 1
#             ans[r] = h
#     print(" ".join(map(str, ans)))
#
#
# T = int(input())
# for _ in range(T):
#     solve()

lis = input().split(" ")
for i in range(len(lis)):
    print(lis[i][0].upper() + lis[i][1:])


