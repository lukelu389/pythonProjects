# ccc 2012 s1
# n = int(input())
# ans = 0
# for i in range(n+1):
#     for j in range(n):
#         for k in range(n - 1):
#             if i < j < k: ans += 1
#
# print(ans)

# ccc 2012 s2
# s = input()
#
# R_rule = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
# A_rule = [1, 5, 10, 50, 100, 500, 1000]
# ans = int(s[0]) * A_rule[R_rule.index(s[1])]
#
# for i in range(2, len(s), 2):
#     j = i + 1
#     if R_rule.index(s[j]) > R_rule.index(s[j - 2]): ans -= 2 * (int(s[i - 2]) * A_rule[R_rule.index(s[j - 2])])
#     ans += int(s[i]) * A_rule[R_rule.index(s[j])]
#
#
# print(ans)
#
# ccc 2012 s3
# ns = int(input())
# temp = []
# for i in range(ns):
#     temp.append(int(input()))
#
# freq = {}
# for i in temp:
#     if temp.count(i) not in freq.keys():
#         freq[temp.count(i)] = set()
#     freq[temp.count(i)].add(i)
#
# most_freq = max(freq.keys())
#
# if len(freq[most_freq]) > 1:
#     x = sorted(freq[most_freq])
#     print(abs(x.pop() - x[0]))
# else:
#     v = freq[most_freq].pop()
#     del freq[most_freq]
#     s_most_freq = max(freq.keys())
#     x = sorted(freq[s_most_freq])
#     print(max(abs(v-x.pop()), abs(v-x.pop(0))))
#
# # first two test cases past, the third resulted in TLE but the answer is correct when I check with the offical
# # CCC test cases


# Thanksgiving Feast --> TLE Python, AC Java
# import collections
# import heapq
#
#
# N, E, C, V, D = [int(i) for i in input().split()]
# c = [int(i) for i in input().split()]
#
# times = []
# for i in range(E):
#     times.append([int(i) for i in input().split()])
#
# g = collections.defaultdict(dict)
# # for frm, to, cost in times:
# #     g[frm][to] = cost
# #     g[to][frm] = cost
#
# for frm, to in times:
#     g[frm][to] = 1
#     g[to][frm] = 1
#
#
# def calculate_distances(graph, v):
#     distances = {vertex: float("inf") for vertex in graph}
#     distances[v] = 0
#     pq = [(0, v)]
#
#     while len(pq) > 0:
#         current_distance, current_vertex = heapq.heappop(pq)
#
#         if current_distance > distances[current_vertex]:
#             continue
#
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#
#     return distances
#
#
# ans = [float('inf')] * (N+1)
# t = calculate_distances(g, V)
# te = calculate_distances(g, D)
# for i in c:
#     ans[i] = t[i] + te[i]
#
# print(min(ans))

# ccc Senior 2015 S4 in Java ShortestPath

import sys


# Function to read space-separated integers from input
# list(map(int, sys.stdin.readline().split()))


# Function to read a single integer from input
# int(sys.stdin.readline())

def main():
    N = int(sys.stdin.readline())
    frequency = [0] * 1001
    highest = []
    second_highest = []

    for _ in range(N):
        v = int(sys.stdin.readline())
        frequency[v] += 1

    max_freq = max(frequency)
    highest = [i for i, f in enumerate(frequency) if f == max_freq]

    if len(highest) >= 2:
        ans = max(highest) - min(highest)
        print(ans)
        return

    sec_max_freq = max(f for f in frequency if f != max_freq)
    second_highest = [i for i, f in enumerate(frequency) if f == sec_max_freq]

    ans = max(abs(h - sh) for h in highest for sh in second_highest)
    print(ans)


main()

