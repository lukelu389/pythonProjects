# length = int(input())
# mountains = [int(i) for i in input().split()]
#
# cuts = ["0"]
# jumps = 1
# fm = 0
# collection = [[0] * length]
#
# for i in range(1, length):
#     temp = []
#     while fm + jumps < length:
#         if i > 1:
#             temp.append(collection[i - 2][fm + 1] + abs(mountains[jumps + fm] - mountains[fm]))
#
#         else:
#             temp.append(abs(mountains[jumps + fm] - mountains[fm]))
#
#         fm += 1
#     jumps += 1
#
#     collection.append(temp)
#     cuts.append(min(str(temp)))
#     fm = 0
#
# print(" ".join(cuts))
#
# K = int(input())
# query = list(map(int, input().split()))
# Q = int(input())
# ran = [list(map(int, input().split())) for _ in range(Q)]
# seen = {}
# cycle_start = -1
# cycle_length = 0
#
# i = len(query)
# while True:
#     if i >= K:
#         xor_value = 0
#         for j in range(i - K, i):
#             xor_value ^= query[j]
#     else:
#         xor_value = query[i]
#
#     if tuple(query[-K:]) in seen:
#         cycle_start = seen[tuple(query[-K:])]
#         cycle_length = i - cycle_start
#         break
#
#     seen[tuple(query[-K:])] = i
#     query.append(xor_value)
#     i += 1
#
#
# def get_value_at(index):
#     if index < len(query):
#         return query[index]
#     index_in_cycle = (index - cycle_start) % cycle_length
#     return query[cycle_start + index_in_cycle]
#
#
# for r in ran:
#     l, r = r
#     l -= 1
#     result = get_value_at(l)
#     for i in range(l + 1, r):
#         result ^= get_value_at(i)
#     print(result)
