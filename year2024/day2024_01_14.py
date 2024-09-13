# inputs = [[4, 3, 1], [3, 2, 4], [3], [4], []]
#
#
# def bfs(graph):
#     q = [[0]]
#     target = len(graph) - 1
#     res = []
#     i = 1
#     while q:
#         temp = q.pop(0)
#         if temp[-1] == target:
#             res.append(temp)
#         for o in graph[temp[-1]]:
#             q.append(temp + [o])
#         i += 1
#     return res
#
#
# bfs(inputs)

command = input().split(" ")
rows, cols, prows, pcols = int(command[0]), int(command[1]), int(command[2]), int(command[3])

