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

# N, Q = (int(x) for x in input().split())
# c = [int(x) for x in input().split()]
# t = [int(x) for x in input().split()]
# diffs = sorted([ci - ti for ci, ti in zip(c, t)], reverse=True)
# for _ in range(Q):
#     V, S = (int(x) for x in input().split())
#     print("YES" if (V <= N and (V <= 0 or diffs[V-1] > S)) else "NO")

