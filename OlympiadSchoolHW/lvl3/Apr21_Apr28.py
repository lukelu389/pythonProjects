# N = int(input())
#
#
# def isGood(temp):
#     f = 0
#     for j in temp:
#         if f < 0:
#             print('NO')
#             return
#         if j == "(":
#             f += 1
#         elif j == ")":
#             f -= 1
#         elif not j.isnumeric():
#             print('NO')
#             return
#
#     if f == 0: print("YES")
#     else: print('NO')
#     return
#
#
# for i in range(N):
#     isGood(input())

# def lcs(str1, str2, m, n):
#     L = [[0 for i in range(n + 1)]
#          for i in range(m + 1)]
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0 or j == 0:
#                 L[i][j] = 0
#             elif str1[i - 1] == str2[j - 1]:
#                 L[i][j] = L[i - 1][j - 1] + 1
#             else:
#                 L[i][j] = max(L[i - 1][j],
#                               L[i][j - 1])
#
#     return L[m][n]
#
#
# def printMinDelAndInsert(str1, str2):
#     m = len(str1)
#     n = len(str2)
#     leng = lcs(str1, str2, m, n)
#     print(m - leng)
#
#
# str1 = "abcdefghijklmnopqrstuvwxyz"
# str2 = input()
# printMinDelAndInsert(str1, str2)

def minimal_drilling(L, D, density_grid, gold_coordinates):
    dp = [[float('inf')] * D for _ in range(L)]
    dp[0][0] = density_grid[0][0]
    for i in range(L):
        for j in range(D):
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + density_grid[i][j])
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + density_grid[i][j])
            if i < L - 1:
                dp[i][j] = min(dp[i][j], dp[i + 1][j] + density_grid[i][j])

    return dp[gold_coordinates[0]][gold_coordinates[1]]


L, D = map(int, input().split())
density_grid = [list(map(int, input().split())) for _ in range(D)]
gold_coordinates = tuple(map(int, input().split()))

print(minimal_drilling(L, D, density_grid, gold_coordinates))
