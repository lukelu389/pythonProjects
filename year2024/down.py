words = int(input())
initial = list(map(int, input().split()))
expected = list(map(int, input().split()))
t = initial.copy()
l_swaps = []
r_swaps = []
j = 0
temp = []
for i in range(words):
    temp = [j, i]
    while j < words:
        if initial[i] != expected[j]: break
        j += 1

    temp[1] = j - 1
    if temp[0] == temp[1] == i:
        pass
    elif temp[0] < i < temp[1]:
        l_swaps.append((temp[0], i))
        r_swaps.append((i, temp[1]))
    elif i <= temp[0] <= temp[1]:
        r_swaps.append((i, temp[1]))
    elif temp[0] <= temp[1] <= i:
        l_swaps.append((temp[0], i))


def swap(arr, s, i, j):
    if s =="R":
        key = arr[i]
        for w in range(i, j+1):
            arr[w] = key
    else:
        key = arr[j]
        for w in range(i, j+1):
            arr[w] = key

    return arr


if initial == expected:
    print('YES')
    print('0')

elif len(r_swaps) == len(l_swaps) == 0:
    print('NO')

else:
    l_swaps.sort()
    r_swaps.sort()
    r = r_swaps.copy()
    for i in l_swaps:
        t = swap(t, "L", i[0], i[1])

    for i in range(len(r_swaps)):
        temp = r.pop()
        t = swap(t, "R", temp[0], temp[1])

    if t == expected:
        print('YES')
        print(len(l_swaps) + len(r_swaps))
        for i in l_swaps:
            print("L", i[0], i[1])

        for i in range(len(r_swaps)):
            temp = r_swaps.pop()
            print('R', temp[0], temp[1])

    else: print('NO')


