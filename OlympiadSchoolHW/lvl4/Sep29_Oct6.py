source = str(input())
target = str(input())
try:
    print(source.index(target))
except ValueError:
    print(-1)

# num_columns = int(input())
# row1 = list(input().split())
# row2 = list(input().split())
# perimeter = 0
# if row1[0] == "1":
#     perimeter += 3
# if row2[0] == "1":
#     perimeter += 3
# if row1[0] == row2[0] == "1":
#     perimeter -= 2
# for i in range(1, len(row1)):
#     if row1[i] == "1":
#         perimeter += 3
#     if row1[i] == "1" and row1[i - 1] == "1":
#         perimeter -= 2
# for i in range(1, len(row1)):
#     if row2[i] == "1":
#         perimeter += 3
#     if row2[i] == "1" and row2[i - 1] == "1":
#         perimeter -= 2
#     if i % 2 == 0 and row1[i] == row2[i] == "1":
#         perimeter -= 2
# print(perimeter)
#
# length = int(input())
# mountains = [int(i) for i in input().split()]
# cuts = ["0"]
# jumps = 1
# fm = 0
# collection = [[0] * length]
# for i in range(1, length):
#     temp = []
#     while fm + jumps < length:
#         if i > 1:
#             temp.append(collection[i - 2][fm + 1] + abs(mountains[jumps + fm] - mountains[fm]))
#         else:
#             temp.append(abs(mountains[jumps + fm] - mountains[fm]))
#         fm += 1
#     jumps += 1
#     collection.append(temp)
#     cuts.append(str(min(temp)))
#     fm = 0
# print(" ".join(cuts))


