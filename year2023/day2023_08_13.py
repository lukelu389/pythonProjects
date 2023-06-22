
# def find_max_pair(sample):
#     sample = set(sample)
#     counter = 0
#     for i in range(len(sample)):
#         if list(sample)[i][::-1] in sample:
#             counter += 1
#
#     return counter//2
#
# print(find_max_pair(["cd", "ac", "dc", "ca", "zz"]))

dic = {2.5: 2, 3.5:1}
print(max(dic.values()))
