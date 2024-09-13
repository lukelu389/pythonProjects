# a, b = list(map(int, input().split()))
# def findZeroes(x):
#     sum = 0
#     i = 5
#     while i <= x:
#         sum += x // i
#         i *= 5
#     return sum
# def binSearch(x):
#     start = 1
#     end = 5e9
#     while start < end:
#         mid = (start + end) // 2
#         if findZeroes(mid) >= x:
#             end = mid
#         else:
#             start = mid + 1
#     return start
# print(int(binSearch(b+1) - binSearch(a)))



