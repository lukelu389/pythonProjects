# Homework 77, convert binary tree to a balanced tree using rotation

# Classwork 115
def numDistinct(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]

    return dp[0][0]


print(numDistinct("rabbbit", "rabbit"))

# 1971, 695, 127, kmp string alg
