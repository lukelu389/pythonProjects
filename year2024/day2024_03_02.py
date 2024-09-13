# leetcode 62 72


# 62
def find_routes(m, n):
    dp = [[1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1] + dp[i - 1][j]

    return dp[m - 1][n - 1]


# 72

def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i

    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


# 22 32 45


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

seg = []
lft = []
rit = []

l = r = 0
while l < N:
    while r < N and b[l] == b[r]:
        r += 1
    seg.append((l, r - 1))
    l = r

j = 0
for i in range(len(seg)):
    l, r = seg[i]
    while j < N and a[j] != b[l]:
        j += 1
    if j == N:
        print("NO")
        exit()
    if l < j:
        lft.append((l, j))
    if j < r:
        rit.append((j, r))

print("YES")
print(len(lft) + len(rit))
for l, r in lft:
    print("L", l, r)
for l, r in reversed(rit):
    print("R", l, r)


