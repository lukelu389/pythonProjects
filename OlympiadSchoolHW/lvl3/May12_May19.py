# def convert_to_base_10(number, base):
#     result = 0
#     power = 1
#     for digit in reversed(number):
#         if '0' <= digit <= '9':
#             digit_value = ord(digit) - ord('0')
#         else:
#             digit_value = ord(digit) - ord('a') + 10
#         result += digit_value * power
#         power *= base
#     return result
#
#
# def convert_from_base_10(number, base):
#     if number == 0:
#         return "0"
#
#     result = []
#     while number > 0:
#         remainder = number % base
#         result.append(chr(remainder + ord('0')))
#         number //= base
#     return ''.join(reversed(result))
#
#
# for i in range(5):
#     num1 = input().split()
#     number1, base1 = num1[0], int(num1[1])
#     num2 = input().split()
#     number2, base2 = num2[0], int(num2[1])
#     result_base = int(input())
#     decimal1 = convert_to_base_10(number1, base1)
#     decimal2 = convert_to_base_10(number2, base2)
#     product = decimal1 * decimal2
#     result = convert_from_base_10(product, result_base)
#     print(result)
#


# N = int(input())
# dp = [[0] * (N + 1) for _ in range(N + 1)]
#
# for j in range(1, N + 1):
#     dp[1][j] = 1
#
#
# for i in range(2, N + 1):
#         for j in range(i, N + 1):
#             for k in range(1, j - 1):
#                 dp[i][j] += dp[i - 1][k]
#
#
# result = 0
# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if dp[i][j] >= i: result += 1
#
# print(result)

# def countWays(n):
#     A = [0] * (n + 1)
#     B = [0] * (n + 1)
#     A[0] = 1
#     A[1] = 0
#     B[0] = 0
#     B[1] = 1
#     for i in range(2, n + 1):
#         A[i] = A[i - 2] + 2 * B[i - 1]
#         B[i] = A[i - 1] + B[i - 2]
#
#     return A[n]
#
#
# for _ in range(5):
#     print(countWays(int(input())) % 1000000)


s = input()
n = len(s)
dp = 1

last_occurrence = {}
total_subsequences = 0

for i in range(n):
    char = s[i]
    new_subsequences = dp

    if char in last_occurrence:
        new_subsequences -= last_occurrence[char]

    last_occurrence[char] = dp
    dp += new_subsequences


print((dp - 1) % 10007)

