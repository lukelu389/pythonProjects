# def sum_to_zero(sample):
#     if len(sample) == 3:
#         return sum(sample) == 0
#
#     i = 0
#     j = 1
#     n = 2
#     output = []
#     sample.sort()
#     while i < len(sample) - 2:
#         temp = [sample[i], sample[j], sample[n]]
#         if sum(temp) == 0 and temp not in output:
#             output.append(temp)
#
#         n += 1
#
#         if n >= len(sample):
#             j += 1
#             n = j + 1
#         if j == len(sample) - 1:
#             i += 1
#             j = i + 1
#             n = j + 1
#
#     return output
#
#
# print(sum_to_zero([-5, 2, -1, -2, 3]))

a = {1:[0], 2:[1]}
print(a.values())
