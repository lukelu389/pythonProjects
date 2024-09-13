# s = input()
# result = []
# length = len(s)
#
# for i in range(length - 1):
#     result.append(s[i])
#     current = s[i]
#     next_char = s[i + 1]
#     if (current != "A" and next_char != "A") or (current == 'A' and next_char == 'A'):
#         result.append(' ')
#
# result.append(s[-1])  # add the last character
#
# print(''.join(result))

# import heapq
# N = int(input())
# time = [list(map(int, input().split())) for _ in range(N)]
# time.sort(key=lambda x: x[0])
#
# min_heap = []
#
# for interval in time:
#     start, end = interval
#     if min_heap and min_heap[0] <= start:
#         heapq.heappop(min_heap)
#     heapq.heappush(min_heap, end)
#
# print(len(min_heap))


result = 0
for i in range(64):
    result += i

print(result)