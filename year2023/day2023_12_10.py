length = int(input())
mountains = [int(i) for i in input().split()]

cuts = ["0"]
jumps = 1
fm = 0
collection = [[0] * length]

for i in range(1, length):
    temp = []
    while fm + jumps < length:
        if i > 1:
            temp.append(collection[i - 2][fm + 1] + abs(mountains[jumps + fm] - mountains[fm]))

        else:
            temp.append(abs(mountains[jumps + fm] - mountains[fm]))

        fm += 1
    jumps += 1

    collection.append(temp)
    cuts.append(str(min(temp)))
    fm = 0


# l = 0
# while fm + jumps <= length - 1:
#     while fm + jumps <= length - 1:
#         temp.append(temp[0] + abs(mountains[jumps + fm] - mountains[fm]))
#         temp.pop(0)
#         fm += 1
#         # print(temp)
#
#     jumps += 1
#     fm = 0
#     if jumps > 2:
#         temp.pop(0)
#     a = temp[:length - jumps + 2]
#     cuts.append(str(min(a)))
#
#     if len(a) == 3:
#         l = a[1]
#     temp.pop(0)
#
#
# cuts.append(str(l + abs(mountains[jumps + fm - 1] - mountains[fm])))
print(" ".join(cuts))


