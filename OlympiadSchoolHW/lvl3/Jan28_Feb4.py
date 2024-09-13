"""
    A   B   C   D   E
dis 0   10  60  30  100
vis T   T       T

1st one is better if and only if E is about V ^ 2

O(V^2) implementation --> adjacent matrix with java array

loops n rounds
    select an unvisited vertex with min dis
    mark it visited
    use the selected vertex to update other vertices distance
    if(dis[v] > dis[u] +w){
            dis[v] dis[u] + w
    }

O(E logV)
pq = []
priority queue
(dis = 0, source node)
while pq:
    get pq first item
    if the vertex is visited, skip
    mark visited and update other distance


"""

#
# dLimit, bLimit, E, N = [int(i) for i in input().split()]
# ans = 0
#
# foodBasics = []
# for i in range(N):
#     foodBasics.append(int(input()))
#
# times = []
# for i in range(E):
#     times.append([int(j) for j in input().split()])

# temp = input().split()
# times.append([temp[0], temp[1], int(temp[2])])
# graph[to][frm] = float('inf')


n, k = map(int, input().split())
a = list(input())
p = []
for i in range(n):
    if a[i] == '0':
        continue
    if i + 1 < n and a[i + 1] == '1':
        a[i] = "0"
    if a[i] == '1':
        p.append(i)

ans = len(p)
gap = []
for i in range(1, len(p)):
    gap.append(p[i] - p[i-1] - 1)
gap.sort()
for x in gap:
    if k >= x:
        k -= x
        ans -= 1
if k > 0:
    ans = max(ans, 1)
print(ans)

# import collections
# import heapq
#
# V, E = [int(i) for i in input().split()]
# times = []
# for i in range(E):
#     times.append([int(i) for i in input().split()])
#
# g = collections.defaultdict(dict)
# for frm, to, cost in times:
#     g[frm][to] = cost
#
#     g[to][frm] = cost
#
#
# def calculate_distances(graph, v):
#     distances = {vertex: float("inf") for vertex in graph}
#     distances[v] = 0
#     pq = [(0, v)]
#
#     while len(pq) > 0:
#         current_distance, current_vertex = heapq.heappop(pq)
#
#         if current_distance > distances[current_vertex]:
#             continue
#
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#
#     return distances
#
#
# if V == 2:
#     print(times[0][2])
# else:
#     path = []
#     for i in range(V):
#         path.append(calculate_distances(g, 0)[i])
#
#     for i in range(V):
#         path[i] += calculate_distances(g, V - 1)[i]
#
#     print(max(path))

# line = int(input())
# command = [input().split() for i in range(line)]
#
# for i in command:
#     temp = calculate_distances(graph, i[0])
#     if temp[i[1]] < float("inf"):
#         print(temp[i[1]])
#     else:
#         print('Roger')
#
