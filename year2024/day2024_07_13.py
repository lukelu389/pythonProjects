def calculate_rsum(x1, y1, x2, y2, Psum):
    return Psum[x2 + 1][y2 + 1] - Psum[x2 + 1][y1] - Psum[x1][y2 + 1] + Psum[x1][y1]


N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort()
for i in range(N):
    points[i] = (i + 1, points[i][1])

points.sort(key=lambda p: p[1])
for i in range(N):
    points[i] = (points[i][0], i + 1)

Psum = [[0] * (N + 1) for _ in range(N + 1)]
for x, y in points:
    Psum[x][y] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        Psum[i][j] += Psum[i - 1][j] + Psum[i][j - 1] - Psum[i - 1][j - 1]

answer = 0
for i in range(N):
    for j in range(i, N):
        x1 = min(points[i][0], points[j][0]) - 1
        x2 = max(points[i][0], points[j][0]) - 1
        answer += calculate_rsum(0, i, x1, j, Psum) * calculate_rsum(x2, i, N - 1, j, Psum)

print(answer + 1)

