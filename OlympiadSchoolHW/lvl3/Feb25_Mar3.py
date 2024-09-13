# Q1
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
# arr.pop()
#
# print(sum(arr)//len(arr))

# Q2
# N, D = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# ignitions = 1
# out = []
# cnt = 1
#
# for i in range(0, N-1):
#     j = i + 1
#     if abs(arr[j] - arr[i]) > D:
#         ignitions += 1
#         out.append(cnt)
#         cnt = 1
#     else: cnt += 1
#
# print(ignitions)
# print(max(out))

# Q3
#
# N = int(input())
# nums = list(map(int, input().split()))
#
# DP = [0] * N
# DP[1] = abs(nums[1] - nums[0])
#
# for i in range(2, N):
#     DP[i] = min(DP[i - 1] + abs(nums[i] - nums[i - 1]), DP[i - 2] + abs(nums[i] - nums[i - 2]))
#
# print(DP[N - 1])

# Q4
N = int(input())
nums = [int(input()) for _ in range(N)]

incl = 0
excl = 0
for i in nums:
    new_excl = max(excl, incl)
    incl = excl + i
    excl = new_excl
print(max(excl, incl))

