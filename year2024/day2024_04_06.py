# front end: existing format and template, angular, Node.js, https://angularjs.org/
# back end: mangod

# 8 queens
# bit mask


# N = 8  # (size of the chessboard)
#
#
# def solveNQueens(board, col):
#     if col == N:
#         print(board)
#         return True
#     for i in range(N):
#         if isSafe(board, i, col):
#             board[i][col] = 1
#             if solveNQueens(board, col + 1):
#                 return True
#             board[i][col] = 0
#     return False
#
#
# def isSafe(board, row, col):
#     for x in range(col):
#         if board[row][x] == 1:
#             return False
#     for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
#         if board[x][y] == 1:
#             return False
#     for x, y in zip(range(row, N, 1), range(col, -1, -1)):
#         if board[x][y] == 1:
#             return False
#     return True
#
#
# board = [[0 for x in range(N)] for y in range(N)]
# if not solveNQueens(board, 0):
#     print("No solution found")


# # Happy Number
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         if n == 1: return True
#         slow = n
#         fast = n
#
#         while True:
#             slow = sumOfSquares(slow)
#             fast = sumOfSquares(sumOfSquares(fast))
#             if slow == fast: break
#         return slow == 1
#
#
# def sumOfSquares(num):
#     sum = 0
#     while num > 0:
#         last_diget = num % 10
#         sum += last_diget ** 2
#         num = num // 10
#     return sum


# def distribute_salt(n, m, salt):
#     for i in range(n - 1):
#         salt[i + 1] = max(salt[i + 1], salt[i] - m)
#     for i in range(n - 1, 0, -1):
#         salt[i - 1] = max(salt[i - 1], salt[i] - m)
#     return salt
#
#
# n, m = map(int, input().split())
# salt = list(map(int, input().split()))
#
#
# result = distribute_salt(n, m, salt)
#
# print(*result)


def minimumCost(costs, n):
    costs = sorted(costs)
    totalCost = 0
    for i in range(n - 1, 1, -2):
        if i == 2: totalCost += costs[2] + costs[0]
        else:
            price_first = costs[i] + costs[0] + 2 * costs[1]
            price_second = costs[i] + costs[i - 1] + 2 * costs[0]
            totalCost += min(price_first, price_second)

        print(totalCost)
    if n == 1: totalCost += costs[0]
    else: totalCost += costs[1]
    
    return totalCost


cost = [1, 2, 5, 10]
n = len(cost)
print(minimumCost(cost, n))

