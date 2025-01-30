# N, M = list(map(int, input().split()))
#
# freq = [0] * (M)
# for i in range(N):
#     temp = list(map(int, input().split()))
#     for j in range(M):
#         if temp[j] == 1:
#             freq[j] += 1
#
#
# for i in range(M-1):
#     m = freq.index(max(freq))
#     print(m + 1, end=" ")
#     freq[m] = -1
#
# m = freq.index(max(freq))
# print(m + 1)
#
#
#
# N = int(input())
# s = input()
#
# for _ in range(N):
#     result = []
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count += 1
#             i += 1
#         result.append(str(count) + s[i])
#         i += 1
#     s = ''.join(result)
# print(s)
#
#
#
# n = int(input())
# s = list(map(int, input().split()))
# t = list(map(int, input().split()))
#
# pos_in_t = {t[i]: i for i in range(n)}
#
#
# breaks = 0
# for i in range(n - 1):
#     if pos_in_t[s[i]] + 1 != pos_in_t[s[i + 1]]:
#         breaks += 1
#
# print(breaks + 1)

# def generate_partitions(n, start, partition, result):
#     if n == 0:
#         result.append(" ".join(map(str, partition)))
#         return
#
#     for i in range(start, 0, -1):
#         if i <= n:
#             generate_partitions(n - i, i, partition + [i], result)
#
#
# n = int(input().strip())
# result = []
# generate_partitions(n, n, [], result)
# print("\n".join(result))



