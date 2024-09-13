# N = int(input())
# shoes = list(map(int, input().split()))
#
# dp = [0 for _ in range(N + 1)]
#
# i = 0
# while i < N - 2:
#     if N - i == 3:
#         dp[i] += shoes[i] + shoes[i + 1] + shoes[i + 2] - min(shoes[i], shoes[i + 1], shoes[i + 2])
#         break
#
#     elif N - i == 2:
#         dp[i] += 0.5 * min(shoes[i], shoes[i + 1]) + max(shoes[i], shoes[i + 1])
#     else:
#         two = 0.5 * min(shoes[i], shoes[i + 1]) + max(shoes[i], shoes[i + 1])
#         three = shoes[i] + shoes[i + 1] + shoes[i + 2] - min(shoes[i], shoes[i + 1], shoes[i + 2])
#         dp[i] += min(two, three)
#         if two < three:
#             dp[i + 2] = dp[i]
#             i += 2
#         else:
#             dp[i + 3] = dp[i]
#             i += 3
#
# print(max(dp))

# a, b = list(map(int, input().split()))
#
#
# def lcm_of_array(x):
#     power = x
#     exp = 1
#     while True:
#         if b // power - a // power == 0:
#             return exp - 1
#         power *= x
#         exp += 1
#
#
# print(min(lcm_of_array(2), lcm_of_array(5)))


dist = int(input())
n = int(input())
clubs = [int(input().strip()) for x in range(n)]
dp = [10000 for x in range(dist + 1)]
dp[0] = 0
for i in range(dist):
    for j in range(n):
        if clubs[j] + i <= dist:
            dp[i + clubs[j]] = min(dp[i + clubs[j]], dp[i] + 1)

if dp[-1] != 10000:
    print("Roberta wins in", dp[-1], "strokes.")
else:
    print("Roberta acknowledges defeat.")
