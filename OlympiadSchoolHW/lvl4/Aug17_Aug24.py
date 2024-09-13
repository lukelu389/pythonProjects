# N, D = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# psa = [0] * N
# psa[0] = arr[0]
# for i in range(1, N):
#     psa[i] = psa[i - 1] + arr[i]
# left_bound = 0
#
# for _ in range(D):
#     i = int(input())
#     sum_left = psa[left_bound + i - 1] - (psa[left_bound - 1] if left_bound > 0 else 0)
#     sum_right = psa[N - 1] - psa[left_bound + i - 1]
#     if sum_left >= sum_right:
#         print(sum_left)
#         left_bound += i
#     else:
#         print(sum_right)
#         N = left_bound + i

# After all operations, the remaining array is arr[left_bound:N]


# tle 2 cases, works in java with exactly the same code
# N, P = list(map(int, input().split()))
# stack = [[], [], [], [], [], []]
# m = 0
# for i in range(N):
#     s, f = list(map(int, input().split()))
#     if not stack[s - 1] or stack[s - 1][-1] < f:
#         stack[s - 1].append(f)
#     else:
#         while stack[s - 1]:
#             if stack[s - 1][-1] > f:
#                 stack[s - 1].pop(-1)
#                 m += 1
#             elif stack[s - 1][-1] == f:
#                 stack[s - 1].pop(-1)
#                 m -= 1
#             else:
#                 break
#         stack[s - 1].append(f)
#     m += 1
# print(m)

# java works
# n = int(input())
# arr = list(map(int, input().split()))
#
# OFFSET = 200001
# exists = [False] * OFFSET * 2
# total = 0
#
# for i in range(n):
#     for j in range(i):
#         if exists[OFFSET + arr[i] - arr[j]]:
#             total += 1
#             break
#     for j in range(i + 1):
#         exists[OFFSET + arr[i] + arr[j]] = True
#
# print(total)
