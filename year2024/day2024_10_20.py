# from collections import deque
# field day
# import sys
#
#
# def main():
#     c, n = map(int, sys.stdin.readline().split())
#     teams = []
#     queue = deque()
#     dists = [-1] * (1 << c)
#     for j in range(n):
#         team = sys.stdin.readline().strip().replace('G', '0').replace('H', '1')
#         teams.append(int(team, 2))
#         queue.append(teams[j])
#         dists[teams[j]] = 0
#     while queue:
#         mask = queue.popleft()
#         for d in range(c):
#             new_mask = mask ^ (1 << d)
#             if dists[new_mask] == -1:
#                 dists[new_mask] = dists[mask] + 1
#                 queue.append(new_mask)
#     out = []
#     for j in range(n):
#         out.append(str(c - dists[((1 << c) - 1) ^ teams[j]]) + '\n')
#     sys.stdout.write(''.join(out))
#
#
# if __name__ == '__main__':
#     main()

# https://usaco.org/index.php?page=viewproblem2&cpid=1398