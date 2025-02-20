
# Senior1 - simple math - goal AC
# a, b, c, d = map(int, input().split())
#
# perimeter1 = 2 * ((a + c) + max(b, d))
# perimeter2 = 2 * ((max(a, c)) + (b + d))
#
# print(min(perimeter1, perimeter2))

# Senior2 - string manipulation - goal AC
# def find_nth_character(s, n):
#     parsed = []
#     total_length = 0
#     i = 0
#
#     while i < len(s):
#         char = s[i]
#         i += 1
#         num = 0
#
#         while i < len(s) and s[i].isdigit():
#             num = num * 10 + int(s[i])
#             i += 1
#
#         repeat_count = num if num > 0 else 1
#         parsed.append((char, repeat_count))
#         total_length += repeat_count
#
#     mod_n = n % total_length
#     current_length = 0
#
#     for char, count in parsed:
#         if current_length + count > mod_n:
#             return char
#         current_length += count
# s = input().strip()
# n = int(input())
# print(find_nth_character(s, n))



# Senior4 - dp - goal - Partial
import sys
import heapq
from collections import defaultdict, deque

def bfs_shortest_path(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    distances = [float('inf')] * (n + 1)
    distances[1] = 0

    queue = deque([(1, 0)])

    while queue:
        node, prev_w = queue.popleft()

        for neighbor, edge_w in graph[node]:
            if distances[neighbor] == float('inf'):
                new_cost = distances[node] + abs(edge_w - prev_w)
                distances[neighbor] = new_cost
                queue.append((neighbor, edge_w))

    return distances[n] if distances[n] != float('inf') else -1

def dijkstra(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = float('inf')
    dist = [{} for _ in range(n + 1)]
    pq = [(0, 1, 0)]

    while pq:
        cost, node, prev_w = heapq.heappop(pq)

        if node == n:
            return cost

        if prev_w in dist[node] and dist[node][prev_w] <= cost:
            continue

        dist[node][prev_w] = cost

        for neighbor, edge_w in graph[node]:
            new_cost = cost + abs(edge_w - prev_w)
            if edge_w not in dist[neighbor] or new_cost < dist[neighbor][edge_w]:
                heapq.heappush(pq, (new_cost, neighbor, edge_w))

    return -1

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

if m == n - 1:
    print(bfs_shortest_path(n, edges))
else:
    print(dijkstra(n, edges))
