# n = int(input())
# mx = 0
# twoCnt = 1
#
# for i in range(n - 2, 1, -2):
#     mx = max(mx, (i - 1) * i // 2 * twoCnt)
#     twoCnt += 1
#
# print(mx)
#
# from collections import deque, defaultdict
#
#
# def build_graph(N, edges):
#     graph = defaultdict(list)
#     for u, v in edges:
#         graph[u].append(v)
#     return graph
#
#
# def remove_edge(graph, u, v):
#     if v in graph[u]:
#         graph[u].remove(v)
#
#
# def bfs(graph, start, end):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()
#         if node == end:
#             return True
#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#
#     return False
#
#
# def can_reach_after_deletion(N, edges, edge_to_delete):
#     u, v = edge_to_delete
#     graph = build_graph(N, edges)
#     remove_edge(graph, u, v)
#     return bfs(graph, 1, N)
#
#
# N, M = list(map(int, input().split()))
# edges = [tuple(map(int, input().split())) for _ in range(M)]
#
#
# for i in range(M):
#     result = can_reach_after_deletion(N, edges, edges[i])
#     print("YES" if result else "NO")
#

N, L, S = map(int, input().split())

changes = {}
for _ in range(N):
    a, b, s = map(int, input().split())
    if a - 1 in changes:
        changes[a - 1] += s
    else:
        changes[a - 1] = s

    if b in changes:
        changes[b] -= s
    else:
        changes[b] = -s

current_sum = 0
cnt = 0
prev_pos = 0
sorted_positions = sorted(changes.keys())

for pos in sorted_positions:
    if current_sum < S:
        cnt += pos - prev_pos
    current_sum += changes[pos]
    prev_pos = pos

if current_sum < S:
    cnt += L - prev_pos
print(cnt)
