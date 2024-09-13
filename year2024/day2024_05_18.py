# def trap(height):
#     n = len(height)
#     ans = 0
#     st = []
#
#     for r, x in enumerate(height):
#         while st and height[st[-1]] < x:
#             m = st.pop()
#             if not st:
#                 break
#             l = st[-1]
#             h = min(x, height[l]) - height[m]
#             w = r - l - 1
#             ans += h * w
#         st.append(r)
#
#     return ans


#  84, 841

def canVisitAllRooms(rooms):
    seen = [False] * len(rooms)
    seen[0] = True
    stack = rooms[0]
    while stack:
        current = stack.pop()
        if not seen[current]:
            seen[current] = True
            stack += rooms[current]

    return all(seen)


def trap(height):
    n = len(height)
    ans = 0
    st = []
    for r, x in enumerate(height):
        while st and height[st[-1]] < x:
            m = st[-1]
            st.pop()
            if not st: break
            l = st[-1]
            h = min(x, height[l]) - height[m]
            w = r - l - 1
            ans += h * w
        st.append(r)
    return ans


def largestRectangleArea(heights):
    max_area = 0
    stack = []
    for i, h in enumerate(heights):
        idx = i
        if not stack:
            stack.append([i, h])
            continue
        while stack and stack[-1][1] > h:
            idx, he = stack.pop()
            max_area = max(max_area, (i - idx) * he)
        stack.append([idx, h])

    while stack:
        idx, he = stack.pop()
        max_area = max(max_area, (i - idx + 1) * he)
    return max_area


N = 8


def solveNQueens(board, col):
    if col == N:
        print(board)
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False


def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

# 131, 40, 37, 738, 417

