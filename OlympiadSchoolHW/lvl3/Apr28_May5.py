def process_line(line, nums):
    X = ''
    S = 0
    for c in line:
        if c.isalpha():
            if S == 1:
                nums.append('0')
                S = 0
            if S == 2:
                nums.append(X)
                X = ''
                S = 0
        elif c.isdigit():
            if S == 0 and c == '0':
                S = 1
            if c != '0' or S == 2:
                X += c
                S = 2
    if S == 2: nums.append(X)
    if S == 1: nums.append('0')


N = int(input())

nums = []

for _ in range(N):
    line = input()
    process_line(line, nums)

nums = [int(num) if int(num) != 0 or len(num) == 1 else '0' for num in nums]
nums.sort()
for num in nums:
    print(num)
