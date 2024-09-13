# N = int(input())
# arr = list(map(int, input().split()))
# Q = int(input())
# pos = [float('inf')] * (N+1)
# for i in range(N):
#     pos[arr[i]] = i
#
# for _ in range(Q):
#     a, b = list(map(int, input().split()))
#     if pos[a] < pos[b]:
#         print(a)
#     else:
#         print(b)
#

# N = int(input())
# arr = list(map(int, input().split()))
# total_sum = sum(arr)
# prefix_sum = [0] * N
# prefix_sum[0] = arr[0]
# for i in range(1, N):
#     prefix_sum[i] = prefix_sum[i-1] + arr[i]
#
# min_diff = float('inf')
#
# for i in range(N):
#     left_sum = prefix_sum[i]
#     right_sum = total_sum - left_sum
#     diff = abs(left_sum - right_sum)
#     min_diff = min(min_diff, diff)
#
# print(min_diff)

# N = int(input())
# arr = list(map(int, input().split()))
# modifications = 0
#
# for i in range(1, N):
#     if arr[i] <= arr[i - 1]:
#         modifications += (arr[i - 1] - arr[i] + 1)
#         arr[i] = arr[i - 1] + 1
#
# print(modifications)
#
# N, Q = list(map(int, input().split()))
# arr = [0] * N
#
# for _ in range(Q):
#     o, s, e = list(map(int, input().split()))
#     if o == 1:
#         for i in range(s-1, e):
#             arr[i] += 1
#
#     else:
#         k = 1
#         for i in range(s-1, e):
#             arr[i] += k
#             k += 1
#
# for i in arr:
#     print(i, end=" ")

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort(key=lambda x: x[0])

prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + points[i][1]

max_score = float('-inf')
for i in range(N):
    for j in range(i, N):
        current_sum = prefix_sum[j + 1] - prefix_sum[i]
        ai_max = points[j][0]
        ai_min = points[i][0]
        range_diff = ai_max - ai_min
        score = current_sum - range_diff
        max_score = max(max_score, score)

print(max_score)
