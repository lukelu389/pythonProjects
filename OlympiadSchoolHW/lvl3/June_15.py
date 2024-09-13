N = int(input())
arr = list(map(int, input().split()))
maximum = max(arr)
best_start = 0
best_end = 0
min_and_sum = float('inf')

for i in range(N):
    current_and = arr[i]
    for j in range(i, N):
        current_and &= arr[j]
        if current_and < min_and_sum:
            min_and_sum = current_and
            best_start = i
            best_end = j

print(maximum, min_and_sum)


# N, regular_d, power_t = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# arr.sort(reverse=True)
# result = 0
# for i in range(power_t):
#     arr.pop(0)
#
# for health in arr:
#     if health > 0:
#         regular_attacks = (health + regular_d - 1) // regular_d
#         result += regular_attacks
# print(result)

# binary_string = input()
# stack = []
# for char in binary_string:
#     if stack and stack[-1] != char:
#         stack.pop()
#     else:
#         stack.append(char)
#
# print(len(binary_string) - len(stack))
import itertools
import random

# word = input()
# N = int(input())
# bank = []
# for _ in range(N):
#     temp = list(map(str, input()[1:].split()))
#     temp.append("")
#     bank.append(temp)
#
# result = 0
# combinations = ["".join(x) for x in itertools.product(*bank)]
# for i in combinations:
#     if i == word:
#         result = random.randint(1, N+1)
#
# if result == 0:
#     print(-1)
# else:
#     print(result)
#



