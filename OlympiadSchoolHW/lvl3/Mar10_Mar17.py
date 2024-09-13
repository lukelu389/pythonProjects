# T = int(input())
# for _ in range(T):
# 	start = input()
# 	print('E' if start[-1] == '0' else 'B')


# N, M = map(int, input().split())
# S = list(input())
# A = [int(x) for x in input().split()]
#
# ans = sum(A)
#
# for i in range(N):
#     if S[i] == 'R' and S[(i + 1) % N] == 'L':
#         j = (i - 1 + N) % N
#         total = 0
#
#         while S[j] == 'R':
#             total += A[j]
#             j = (j - 1 + N) % N
#
#         ans -= min(total, M)
#
#     if S[i] == 'L' and S[(i - 1 + N) % N] == 'R':
#         j = (i + 1) % N
#         total = 0
#
#         while S[j] == 'L':
#             total += A[j]
#             j = (j + 1) % N
#
#         ans -= min(total, M)
#
# print(ans)

# N = int(input())
# inputs = [[0, 0, 0]]
# for _ in range(N): inputs.append(list(map(int, input().split())))
#
# dp = [[0, 0, 0] for i in range(N+1)]
# dp[1][0] = inputs[1][0]
# dp[1][1] = inputs[1][1]
# dp[1][2] = inputs[1][2]
#
# for i in range(2, N+1):
#     dp[i][0] = inputs[i][0] + max(dp[i - 1][1], dp[i - 1][2])
#     dp[i][1] = inputs[i][1] + max(dp[i - 1][0], dp[i - 1][2])
#     dp[i][2] = inputs[i][2] + max(dp[i - 1][0], dp[i - 1][1])
#
#
# print(max(dp[N][0], dp[N][1], dp[N][2]))


# def recur(index, time, food):
#     if index == R:
#         return 0
#     if time == M or food == U:
#         return 0
#     if dp[index][time][food] != -1:
#         return dp[index][time][food]
#     if time + t[index] > M or food + f[index] > U:
#         dp[index][time][food] = recur(index + 1, time, food)
#         return dp[index][time][food]
#     dp[index][time][food] = max(recur(index + 1, time, food),
#                                 recur(index + 1, time + t[index], food + f[index]) + v[index])
#     return dp[index][time][food]
#
#
# M, U, R = map(int, input().split())
# v, t, f = [0] * 155, [0] * 155, [0] * 155
# dp = [[[-1] * 110 for _ in range(310)] for _ in range(155)]
#
# for i in range(R):
#     v[i], t[i], f[i] = map(int, input().split())
#
# print(recur(0, 0, 0))
s = [3, 2, 0]
print(s[-1])
