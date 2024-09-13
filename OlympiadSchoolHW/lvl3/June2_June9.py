# def search(arr, n):
#     m = {}
#     for i in range(n):
#         if arr[i] in m:
#             m[arr[i]] += 1
#         else:
#             m[arr[i]] = 1
#     for key, value in m.items():
#         if value == 1:
#             return key
#
#
# N = int(input())
# arr = [int(input()) for i in range(N)]
# arr.sort()
# print(search(arr, N))

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = arr1[0] ^ arr2[0]
for i in range(1, 2 * N + 1):
    result ^= arr1[i] ^ arr2[i]
te = {i ^ result for i in arr1}
if te == set(arr2):
    print(result)
else:
    print(-1)

