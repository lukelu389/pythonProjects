# there was a class on Aug 10th

# https://usaco.org/index.php?page=viewproblem2&cpid=594
N, K = list(map(int, input().split()))
sm = 0
bg = 5e8
arr = [int(input()) for _ in range(N)]
while sm != bg:
    mid = (sm + bg) // 2
    used = 0
    last = 0
    while last < N:
        used += 1
        cur = last + 1
        while cur < N and arr[cur] - arr[last] <= 2 * mid:
            cur += 1
        last = cur

    if used <= K:
        bg = mid

    else:
        sm = mid + 1

print(sm)

# https://usaco.org/index.php?page=viewproblem2&cpid=597
