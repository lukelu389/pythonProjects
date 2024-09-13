# from collections import defaultdict
#
# N = int(input())
# tasks = [list(map(int, input().split())) for _ in range(N)]
#
# events = defaultdict(int)
# for start, end in tasks:
#     events[start] += 1
#     events[end] -= 1
#
# current_machines = 0
# max_machines = 0
# for time in sorted(events):
#     current_machines += events[time]
#     max_machines = max(max_machines, current_machines)
#
# print(max_machines)


# import bisect
#
# N = int(input())
# tasks = [list(map(int, input().split())) for _ in range(N)]
# tasks.sort(key=lambda x: x[1])
#
# dp = [0] * (N + 1)
# ends = [task[1] for task in tasks]
#
# for i in range(1, N + 1):
#     idx = bisect.bisect_right(ends, tasks[i - 1][0]) - 1
#     dp[i] = max(dp[i - 1], dp[idx + 1] + 1)
#
# print(dp[N])
# import bisect
#
# K, N = list(map(int, input().split()))
# tasks = [list(map(int, input().split())) for _ in range(N)]
# tasks.sort(key=lambda x: x[1])
#
# dp = [0] * (N + 1)
# ends = [task[1] for task in tasks]
#
# for i in range(1, N + 1):
#     weight = tasks[i - 1][1] - tasks[i - 1][0] + 1
#     idx = bisect.bisect_right(ends, tasks[i - 1][0]) - 1
#     dp[i] = max(dp[i - 1], dp[idx + 1] + weight)
#
# print(K - dp[N])


# import sys
# from collections import deque
#
# N, M, K = map(int, input().split())
# maze = [[0] * M for _ in range(N)]
#
# for _ in range(K):
#     x, y = map(int, input().split())
#     maze[y-1][x-1] = 1
#
# start_pos = (0, 0)
# end_pos = (N-1, M-1)
#
# queue = deque([start_pos])
# visited = set()
# parent = {}
# found = False
#
# while queue:
#     current = queue.popleft()
#     if current == end_pos:
#         found = True
#         break
#     visited.add(current)
#     x, y = current
#     for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 0 and (nx, ny) not in visited:
#             queue.append((nx, ny))
#             visited.add((nx, ny))
#             parent[(nx, ny)] = current
#
# if found:
#     print('YES')
# else:
#     print('NO')
import bisect

N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j and sum(tasks[i-1]) == sum(tasks[j-1]):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)

        else:
            dp[i][j] = dp[i-1][j]

print(dp)

