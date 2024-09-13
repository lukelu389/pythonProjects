# def points(mine, opponents):
#     if mine == opponents:
#         return 1
#     elif mine == "R" and opponents == "S":
#         return 2
#     elif mine == "S" and opponents == "P":
#         return 2
#     elif mine == "P" and opponents == "R":
#         return 2
#     return 0
#
#
# R = int(input())
# moves = input()
#
# n_friends = int(input())
# friends = [list(input()) for _ in range(n_friends)]
# turns = list(zip(*friends))
#
# total = 0
# total_best = 0
#
# for i in range(R):
#     move = moves[i]
#     opp = turns[i]
#     score = sum([points(move, opp[j]) for j in range(n_friends)])
#     optimal = max(sum([points("R", opp[j]) for j in range(n_friends)]),
#                   sum([points("P", opp[j]) for j in range(n_friends)]),
#                   sum([points("S", opp[j]) for j in range(n_friends)]))
#
#     total += score
#     total_best += optimal
#
# print(total)
# print(total_best)

# def min_changes_to_partition(s, n):
#     r = [0] * (n + 1)
#     w = [0] * (n + 1)
#     for i in range(1, n + 1):
#         r[i] = r[i - 1] + (1 if s[i - 1] == 'R' else 0)
#         w[i] = w[i - 1] + (1 if s[i - 1] == 'W' else 0)
#     min_value = float('inf')
#     result = float('inf')
#
#     for b in range(2, n):
#         min_value = min(min_value, w[b - 1] - r[b - 1])
#         result = min(result, (w[n] - w[b]) + (r[b] - r[0]) + min_value)
#
#     return result
#
#
# N = int(input())
# for _ in range(N):
#     W = int(input())
#     print(min_changes_to_partition(input(), W))

