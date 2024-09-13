# n, k = map(int, input().split())
# freq = [0]*(n+1)
# a = list(map(int, input().split()))
# i, l, r, distinct, ans = 0, 0, 0, 0, 0
# while r < n and i < n:
#     x = a[i]
#     freq[x] += 1
#     if freq[x] == 1:
#         distinct += 1
#     while distinct >= k:
#         ans += n - r
#         freq[a[l]] -= 1
#         if freq[a[l]] == 0:
#             distinct -= 1
#         l += 1
#     r += 1
#     i += 1
# print(ans)


