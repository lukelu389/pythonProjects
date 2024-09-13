import copy
N, M = list(map(int, input().split()))
grid = []
for _ in range(N):
    temp = list(input())
    grid.append(temp)

ref = copy.deepcopy(grid)

for i in range(N-1):
    for j in range(M-1):
        if ref[i][j] == "#":
            grid[i+1][j] = "#"
            grid[i+1][j+1] = "#"
            grid[i][j+1] = "#"


for i in grid:
    print("".join(i))

