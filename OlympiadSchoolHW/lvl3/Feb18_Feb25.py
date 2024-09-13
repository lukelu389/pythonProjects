# ccc 2009 s1 in java

# ccc 2011 j5
n = input()
arr = []
for i in range(int(n) - 1):
    arr.append(input())


def connectedTo(x):
    list = []
    for i in range(len(arr)):
        if arr[i] == str(x):
            list.append(i + 1)
    return list


def ways(node, total):
    if not connectedTo(node):
        return 2

    for i in (connectedTo(node)):
        total = (total * ways(i, 1))

    return total + 1


print(ways(n, 1) - 1)

# ccc 2007 j5
# def trucking_paths(n, index):
#     total = 0
#     if n == 7000:
#         return 1
#
#     elif n in memoization.keys():
#         return memoization[n]
#
#     else:
#         for i in range(index+1, len(trucking_motels)):
#             if A <= trucking_motels[i]-n <= B:
#                 total += trucking_paths(trucking_motels[i], i)
#             elif trucking_motels[i]-n > B:
#                 break
#
#     memoization[n] = total
#     return total
#
# if __name__ == '__main__':
#     trucking_motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
#     A = int(input())
#     B = int(input())
#     C = int(input())
#     if C > 0:
#         for i in range(C):
#             trucking_motels.append(int(input()))
#
#     trucking_motels = sorted(trucking_motels)
#     memoization = {}
#
#     print(trucking_paths(0, 0))

# ccc 2009 s2


