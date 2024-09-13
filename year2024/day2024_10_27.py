# MAXV = 5000000
# sieve = [False] * (MAXV + 1)
# i = 2
# while i * i < len(sieve):
#     if not sieve[i]:
#         for j in range(i * i, len(sieve), i):
#             sieve[j] = True
#     i += 1
#
#
# def solve():
#     n = int(input())
#     l = [int(x) for x in input().split()]
#     moves = 1e9
#     for i, x in enumerate(l):
#         if x % 2 == 0:
#             numMoves = x // 2
#         else:
#             cand = x
#             while sieve[cand]:
#                 cand -= 4
#             numMoves = (x - cand) // 2 + 1
#         if numMoves // 2 < moves // 2:
#             moves = numMoves
#             if moves == 1:
#                 break
#     if moves % 2:
#         print("Farmer John")
#     else:
#         print("Farmer Nhoj")
#
#
# t = int(input())
# for _ in range(t):
#     solve()

def solve_min(needs_pos, pos):
    pos.sort()

    def isok(min_y):
        max_slope = []
        for x, y in needs_pos:
            max_slope.append((y - min_y) // x)
        max_slope.sort()
        return all(a <= b for a, b in zip(pos, max_slope))

    min_y = min(y for x, y in needs_pos)
    hi = min_y
    lo = min_y - pos[-1] * max(x for x, y in needs_pos)
    assert isok(lo)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if isok(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def solve_max(needs_neg, neg):
    return -solve_min([(x, -y) for x, y in needs_neg], [-s for s in neg])


def solve():
    N, x1 = map(int, input().split())
    with_x1 = []
    needs_pos = []
    needs_neg = []
    for _ in range(N):
        y1, y2, x2 = map(int, input().split())
        with_x1.append(y1)
        with_x1.append(y2)
        needs_pos.append((x2, y1))
        needs_neg.append((x2, y2))
    slopes = list(map(int, input().split()))
    assert len(slopes) == 4 * N
    neg, pos = [], []
    for s in slopes:
        if s < 0:
            neg.append(s)
        else:
            pos.append(s)
    if len(neg) < N or len(pos) < N:
        print(-1)
        return
    with_x1.sort()
    for y in with_x1:
        if len(needs_neg) < len(neg):
            needs_neg.append((x1, y))
        else:
            needs_pos.append((x1, y))
    assert len(needs_neg) == len(neg)
    assert len(needs_pos) == len(pos)
    y_min = solve_min(needs_pos, pos)
    y_max = solve_max(needs_neg, neg)
    print(y_max - y_min)


T = int(input())
for _ in range(T): solve()
