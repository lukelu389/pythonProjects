# # ccc 2011 s2
# numbers = int(input())
# s_response = [input() for _ in range(numbers)]
# c_response = [input() for _ in range(numbers)]
#
# ans = 0
# for i in range(numbers):
#     if s_response[i] == c_response[i]:
#         ans += 1
# print(ans)
import collections
import sys

# # usaco january bronze q1
# # majority of three in each array given, if in the selected three there is
# # majority, then it is the one that every cow will choose
#
# meetings = int(input())
# procedure = []
#
# for i in range(meetings):
#     temp = int(input())
#     procedure.append(list(map(int, input().split())))
#
#
# def majority_op(arr):
#     result = []
#     for i in range(len(arr) - 1):
#         if arr[i] == arr[i+1] or (i < len(arr) - 2 and arr[i] == arr[i+2]):
#             result.append(arr[i])
#
#     result = sorted(list(set(result)))
#
#     if len(result) == 0:
#         return [-1]
#
#     return result
#
#
# for i in procedure:
#     print(*majority_op(i))

# # usaco january bronze q2
# n, x = list(map(int, input().split()))
# pads = [[0, 0]]
# broken = [False] * (n+1)
#
# for i in range(n):
#     pads.append(list(map(int, input().split())))
#     broken.append(False)
#
# direction, power, ans = 1, 1, 0
# i = 0
# while i < 5000000 and 1 <= x <= n:
#     if pads[x][0] == 1 and power >= pads[x][1] and not broken[x]:
#         broken[x] = True
#         ans += 1
#     if pads[x][0] == 0:
#         direction = -1
#         power += pads[x][1]
#     x = direction * power
#
# print(ans)


# # usaco january bronze q3
# in intellij
#
# n = int(input())
# a = list(map(int, input().split()))
#
# ans = 0
# contribution = 0
# cnt_ops = 0
# for i in range(n):
#     contribution += cnt_ops
#     a[i] += contribution
#
#     cur_ops = -a[i]
#     ans += abs(cur_ops)
#     cnt_ops += cur_ops
#     contribution += cur_ops
#
# print(ans)

# bob video game
import heapq

N, M, T = list(map(int, input().split()))
times = []
for i in range(M):
    times.append(list(map(int, input().split())))

g = collections.defaultdict(dict)

for frm, to, cost in times:
    g[frm][to] = cost
    g[to][frm] = sys.maxsize

targets = []
for _ in range(T):
    targets.append(list(map(int, input().split())))


def calculate_distances(graph, v, d):
    global N
    distances = {vertex: float("inf") for vertex in graph}
    distances[v] = float('inf')
    pq = [(0, v)]
    shortest_path = [float('inf')] * (N + 1)

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


print(calculate_distances(g, 1, 2))

# for i in targets:
#     temp = calculate_distances(g, i[0], i[1])
#     if temp != float('inf'):
#         print(temp)
#
#     else:
#         print(-1)
