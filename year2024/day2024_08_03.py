# https://usaco.org/index.php?page=viewproblem2&cpid=834
# https://usaco.org/index.php?page=viewproblem2&cpid=967

# binary lifiting: dp[i][j] = dp[dp[i][j-1]][j-1]


n = int(input())
entries = []

for i in range(n):
    value = int(input())
    entries.append((value, i))
entries.sort(key=lambda x: (x[0], x[1]))

answer = 0
for j in range(n):
    answer = max(answer, entries[j][1] - j)
print(answer + 1)


# https://usaco.org/index.php?page=viewproblem2&cpid=1158

