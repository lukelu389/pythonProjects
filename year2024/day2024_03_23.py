# # def minimumTotal(triangle):
# #     for i in range(1, len(triangle)):
# #         for j in range(i + 1):
# #             triangle[i][j] += min(triangle[i - 1][j - (j == i)],
# #                                   triangle[i - 1][j - (j > 0)])
# #     return min(triangle[-1])
# #
#
# # find numbers of ways to fill out a 2 by n rectangle with only 1 by 2 or 2 by 1tiles -- dp
# # 1
#
# def twoSum(nums, target):
#     sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
#     left, right = 0, len(nums) - 1
#     counts = 0
#
#     while left < right:
#         current_sum = sorted_nums[left][1] + sorted_nums[right][1]
#         if current_sum == target:
#             counts += 1
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
#
#     return counts
#
# # 658
# # time complexity O(n)
# def findClosestElements(self, arr, k, x):
#     left = 0
#     right = len(arr) - 1
#
#     while right - left >= k:
#         if abs(x - arr[left]) > abs(x - arr[right]):
#             left += 1
#         else:
#             right -= 1
#
#     return sorted(arr[left:right + 1])

# # https://codeforces.com/gym/104114/problem/N
#
#
def count_ways_to_fill_2_by_N(N):
    # Initialize the dynamic programming array
    dp = [0] * (N + 1)

    # Base cases
    dp[0] = 1
    dp[1] = 1

    # Fill the dynamic programming array
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]


# how to build server, build one
# html page


