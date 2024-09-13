# # SAC 22
# H = int(input())
# S = int(input())
# Q = int(input())
#
# for i in range(Q):
#     H -= S
#     print(H)


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    return f(n-1) + f(n-2)