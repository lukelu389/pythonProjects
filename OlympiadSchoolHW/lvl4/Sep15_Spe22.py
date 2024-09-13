# ccc2024 s3 AC
# import sys
# input = sys.stdin.readline
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# segs, l, r = [], 0, 0
# while l < n:
#     while r < n and b[l] == b[r]:
#         r += 1
#     segs.append([l, r-1])
#     l = r
# left, right, i= [], [], 0
# for l, r in segs:
#     while i < n and a[i] != b[l]:
#         i += 1
#     if i == n:
#         print("NO")
#         sys.exit()
#     else:
#         if l < i: left.append([l, i])
#         if r > i: right.append([i, r])
# print("YES")
# print(len(right)+len(left))
# right.reverse()
# for l, r in left:
#     print("L", l, r)
# for l, r in right:
#     print("R", l, r)

#

# TLE, try on java afterwards
# n, k = map(int, input().split())
# nums = [int(input()) for _ in range(n)]
#
# total = (n * (n + 1)) // 2
#
# freq = [0] * (n + 1)
# unique = 0
# left = 0
# for right in range(n):
#     if freq[nums[right]] == 0:
#         unique += 1
#     freq[nums[right]] += 1
#
#     while unique >= k:
#         left_num = nums[left]
#         freq[left_num] -= 1
#         if freq[left_num] == 0:
#             unique -= 1
#         left += 1
#
#     total -= (right - left + 1)
#
# print(total)


# AC in java
# from collections import deque
# N, K = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# max_deque = deque()
# min_deque = deque()
# left = 0
# count = 0
#
# for right in range(N):
#     value = arr[right]
#
#     while max_deque and max_deque[-1] < value:
#         max_deque.pop()
#     max_deque.append(value)
#     while min_deque and min_deque[-1] > value:
#         min_deque.pop()
#     min_deque.append(value)
#     while max_deque[0] - min_deque[0] > K:
#         left_value = arr[left]
#         left += 1
#         if max_deque[0] == left_value:
#             max_deque.popleft()
#         if min_deque[0] == left_value:
#             min_deque.popleft()
#     count += right - left + 1
#
# print(count)

# sliding window + dp array?

N, D = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]
dp = [float('inf')] * N
dp[0] = arr[0]
l = 0
while l < N:
    min_index = 0
    min_val = float('inf')
    for r in range(1, D + 1):
        if l + r < N:
            dp[l + r] = min(dp[l + r], dp[l] + arr[l + r])
            if dp[l + r] <= min_val:
                min_index = l + r
                min_val = dp[min_index]
    if l == N-1:
        break
    l = min_index
print(dp[-1])
