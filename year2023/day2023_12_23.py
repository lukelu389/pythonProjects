starting = []
ending = []
visited = [set() for i in range(17)]

for i in range(3):
    s = input().split()
    starting.append(s[0])
    ending.append(s[1])

s = input().split()
steps = int(s[0])
initial = s[1]
desired = s[2]


def replace(word, x, rn):
    list1 = []
    for i in range(len(word)):
        cpos = i
        j = 0
        while j < len(x) and cpos < len(word) and word[cpos] == x[j]:
            cpos += 1
            j += 1
        if j == len(x):
            newword = word[0:i] + ending[rn] + word[cpos:]
            list1.append([rn + 1, i + 1, newword])
    return list1


def getdststring(cur, curstep, records):
    if curstep > steps:
        return False
    if curstep == steps:
        if cur == desired:
            for x in records:
                print(x[0], x[1], x[2])
            return True
        return False
    if cur in visited[curstep]:
        return False
    for i in range(3):
        thelist = replace(cur, starting[i], i)
        for y in thelist:
            tr = records.copy()
            tr.append(y)
            if getdststring(y[2], curstep + 1, tr):
                return True
            else:
                visited[curstep + 1].add(y[2])
    return False


getdststring(initial, 0, [])

# bfs
# water problem v8 ->v5 ->v3
# tower or hanoi
# cross river, farmer, wolf, chicken, cabbage
# mazerunner a* alg, accessed? add something to track

# 1, 4
# 7, 24
# xxx----xxx---------xxxx
# xxxxx--xxxxxxx----xxxxx
# xxxx---xxxxxx----xxxxxx
# x---xxx-------xx--xxxxx
# xxx-----xxxxx----------
# xxxxxxxxxxxxxxxx------x
# xxxxxxxxxxxxxxxxxxxxxx-
