# def remove_duplicates(sample):
#     pointer1 = 0
#     pointer2 = 0
#     while pointer2 < len(sample) - 1:
#         pointer2 += 1
#         if sample[pointer1] == sample[pointer2]:
#             sample.remove(pointer2)
#             pointer2 -= 1
#         else:
#             pointer1 += 1
#
#     return sample
#
sample = [1, 1, 2, 4, 5, 1, 3]
sample.sort()
# print(remove_duplicates(sample))
#
print(sample)