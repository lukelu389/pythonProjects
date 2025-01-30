# from collections import defaultdict
#
#
# l = int(input())
# n = int(input())
# events = defaultdict(int)
# events[l] = 0
#
# for i in range(1, n + 1):
#     a, b = list(map(int, input().split()))
#     events[a] += 1
#     events[b] -= 1
#
# sorted_events = sorted(events.items())
# lim = sorted_events[0][0]
# lst = 0
# ci = 0
# f = False
#
# for x, v in sorted_events:
#     ci += v
#     if ci == 0:
#         if f and x - lst > lim:
#             lim = x - lst
#         f = True
#         lst = x
#     if f and x - lst > lim:
#         lim = x - lst
#     if ci != 0:
#         f = False
#
# if l - lst > lim:
#     lim = l - lst
#
# print(lim)

# from math import gcd
#
#
# def lcm(a, b):
#     return abs(a * b) // gcd(a, b)
#
#
# N, M = list(map(int, input().split()))
# A = input()
# B = input()
#
# c = lcm(len(A), len(B))
#
# a = A * (c // len(A))
# b = B * (c // len(B))
# ans = 0
# for i in range(c):
#     if a[i] == b[i]:
#         ans += 1
#
# ans *= (M // len(A)) * gcd(len(A), len(B))
# print(ans)

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        sum_ = 0
        while index > 0:
            sum_ += self.tree[index]
            index -= index & -index
        return sum_

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)


from math import gcd, lcm

N, M = map(int, input().split())
S = input()
T = input()

len_S, len_T = len(S), len(T)
lcm_len = lcm(len_S, len_T)
gcd_len = gcd(len_S, len_T)
fenwick = FenwickTree(lcm_len)

for i in range(lcm_len):
    if S[i % len_S] == T[i % len_T]:
        fenwick.update(i + 1, 1)
total_length_A = N * len_S
blocks = total_length_A // lcm_len
matches_per_block = fenwick.query(lcm_len)
result = matches_per_block * blocks

print(result)

#
# class FenwickTree:
#     def __init__(self, size):
#         self.bit = [0] * (size + 1)
#
#     def update(self, i: int, diff: int) -> None:
#         while i < len(self.bit):
#             self.bit[i] += diff
#             i += i & (-i)
#
#     def query(self, i: int):
#         total = 0
#         while i > 0:
#             total += self.bit[i]
#             i -= i & (-i)
#         return total
#
#
# n, m = map(int, input().split())
# roomba = [list(map(int, input().split())) for _ in range(n)]
# coord = [list(map(int, input().split())) for _ in range(m)]
#
# all_x = {x[0] for x in roomba}.union({x[0] for x in coord})
# all_x = sorted(all_x)
# compress_x = {all_x[i]: i + 1 for i in range(len(all_x))}
#
# coord.sort(key=lambda x: x[1], reverse=True)
# roomba.sort(key=lambda x: x[1], reverse=True)
#
# total = 0
# bit = FenwickTree(len(all_x))
# c_i = 0
#
# for x, y in roomba:
#     x = compress_x[x]
#     while c_i < m and coord[c_i][1] >= y:
#         bit.update(compress_x[coord[c_i][0]], 1)
#         c_i += 1
#
#     total += bit.query(x)
#
# print(total)
