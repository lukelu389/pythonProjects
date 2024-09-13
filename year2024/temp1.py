import collections
import heapq

K, N, M = [int(i) for i in input().split()]
times = []
for i in range(M):
    times.append([int(i) for i in input().split()])

g = collections.defaultdict(dict)
for frm, to, cost, constraint in times:
    g[frm][to] = (cost, constraint)
    g[to][frm] = (cost, constraint)


V, D = [int(i) for i in input().split()]


def calculate_distances(graph, v, k):
    distances = {vertex: float("inf") for vertex in graph}
    distances[v] = 0
    pq = [(0, v)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight[0]
            if distance < distances[neighbor] and weight[1] <= k:
                distances[neighbor] = distance
                k -= weight[1]
                heapq.heappush(pq, (distance, neighbor))

    return distances


ans = calculate_distances(g, V, K)[D]
if ans != float('inf'):
    print(ans)
else:
    print(-1)

