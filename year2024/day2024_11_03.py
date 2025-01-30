# https://usaco.org/index.php?page=open23results field day

t = input()
target = "bessie"
idx = [0] * len(target)
ans = float("inf")
lst = [-1] * len(t)

for i in range(len(t)):
    for j in range(len(target)):
        idx[j] = max(idx[j], i if j == 0 else idx[j - 1] + 1)
        while idx[j] < len(t) and t[idx[j]] != target[j]:
            idx[j] += 1
    lst[i] = min(idx[-1], len(t)) + 1

total = [0] * (len(t) + 1)
for i in reversed(range(len(lst))):
    total[i] = len(lst) + 1 - lst[i]
    if total[i] > 0:
        total[i] += total[lst[i]]

print(sum(total))
# nov 17 class, week before no
