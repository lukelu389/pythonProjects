# usaco bronze 1
#
# N = int(input())
# piles = [int(input()) for _ in range(N)]
#
#
# def check(n):
#     turn = 0
#     if 1 <= n <= 9:
#         return "B"
#     elif n % 11 == 0:
#         return "B"
#     elif n % 10 == 0:
#         if turn == 0:
#             return "E"
#         else:
#             return "B"
#
#     optimal = 0
#     while n > 0:
#         for i in range(1, 10):
#             if (n - i) > 9 and (n - i) % 11 != 0 and (n-i) % 10 == 0:
#                 optimal = i
#         if optimal == 0:
#             if turn == 1:
#                 return "B"
#             else:
#                 return "E"
#         n -= optimal
#         turn ^= 1
#     if turn == 1: return "E"
#     if turn == 0: return "B"
#
#
# for j in piles:
#     print(check(j))

cows, rotations = list(map(int, input().split()))
command = input()
amount = list(map(int, input().split()))
capacity = [_ for _ in amount]

def check(arr):
    global capacity
    global cows
    for j in range(cows):
        if arr[j] > capacity[j]:arr[j] = capacity[j]
    return arr


for _ in range(rotations):
    for i in range(0, cows):
        if i == 0 and command[0] == "L" and amount[0] > 1:
            amount[0] -= 1
            amount[cows - 1] += 1
        elif i == cows - 1 and command[cows - 1] == "R":
            amount[0] += 1
            amount[cows - 1] -= 1

        elif amount[i] > 0:
            if command[i] == "R":
                amount[i] -= 1
                amount[i + 1] += 1

            else:
                amount[i-1] += 1
                amount[i] -= 1

amount = check(amount)
print(sum(amount))

# N, Q = map(int, input().split())
# close = list(map(int, input().split()))
# weight = list(map(int, input().split()))
# tasks = [list(map(int, input().split())) for _ in range(Q)]
#
# tolerance = [max(0, close[i] - weight[i]) for i in range(N)]
#
# for goal, start in tasks:
#     x = 0
#     points = 0
#     for j in tolerance:
#         if j > start:
#             x += 1
#             points += 1
#         if x == goal:
#             print('YES')
#             break
#     if x == 0 or points < goal:
#         print('NO')
#

