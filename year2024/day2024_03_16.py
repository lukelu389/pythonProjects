def jumpGame(nums):
    n = len(nums)
    if n == 1:
        return 0

    dp = [0] * n
    j = 0
    for i in range(1, n):
        while j + nums[j] < i:
            j += 1
        dp[i] = dp[j] + 1

    return dp[-1]


def longest_bracket(s):
    stack = [-1]
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# 120 huffman tree
