import math

N = int(input())
piles = list(map(int, input().split()))
odd = 0
even = 0

for i in piles:
    if i % 2 == 0:
        even += math.ceil(i / 2)
    else:
        odd += math.ceil(i / 2)

if even > odd:
    print('Duke')
else:
    print('Alice')
