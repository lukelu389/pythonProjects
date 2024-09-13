# # def count(a, b):
# #     m = len(a)
# #     n = len(b)
# #
# #     lookup = [[0] * (n + 1) for i in range(m + 1)]
# #
# #     for i in range(n + 1):
# #         lookup[0][i] = 0
# #
# #     for i in range(m + 1):
# #         lookup[i][0] = 1
# #
# #     for i in range(1, m + 1):
# #         for j in range(1, n + 1):
# #
# #             if a[i - 1] == b[j - 1]:
# #                 lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
# #
# #             else:
# #
# #                 lookup[i][j] = lookup[i - 1][j]
# #
# #     return lookup[m][n]
# #
# #
# # a = input()
# # b = "love"
# # print(count(a, b))
#
# N = int(input())
# arr = list(map(int, input().split()))
# M = int(input())
# commands = []
# for i in range(M):
#     commands.append(input().split())
#
# print(commands)
#
#

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    if H[-1] != 1:
        print(-1)
        return
    H = H[:-1]
    remaining = [False] + [True] * N
    for h in H:
        if not remaining[h]:
            print(-1)
            return
        remaining[h] = False
    ends = [x for x in range(1, N + 1) if remaining[x]]
    ans = [-1] * N
    l, r = 0, N - 1
    ans[l], ans[r] = ends
    for h in H:
        if ans[l] > ans[r]:
            l += 1
            ans[l] = h
        else:
            r -= 1
            ans[r] = h
    print(" ".join(map(str, ans)))


T = int(input())
for _ in range(T):
    solve()
