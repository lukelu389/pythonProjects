# N, K, X, Y = list(map(int, input().split()))
#
# if K >= N:
#     print(N*X)
#
# else:
#     print(K*X+(N-K)*Y)
#
# import sys
# N = int(input())
# Q = int(input())
# boxes = [[] for _ in range(N)]
# number_to_boxes = {}
#
# output = []
#
# for _ in range(Q):
#     q = list(map(int, input().split()))
#
#     if q[0] == 1:
#         num, box = q[1], q[2] - 1
#         boxes[box].append(num)
#         if num not in number_to_boxes:
#             number_to_boxes[num] = set()
#         number_to_boxes[num].add(box)
#
#     elif q[0] == 2:
#         box = q[1] - 1
#         output.append(' '.join(map(str, sorted(boxes[box]))))
#
#     elif q[0] == 3:
#         num = q[1]
#         if num in number_to_boxes:
#             output.append(' '.join(map(str, sorted([b + 1 for b in number_to_boxes[num]]))))
#         else:
#             output.append('')
#
# sys.stdout.write('\n'.join(output) + '\n')
from collections import deque


# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n + 1))
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#
#     def union(self, x, y):
#         self.parent[self.find(x)] = self.find(y)
#
#
# G, P = map(int, input().split())
# p = []
# for _ in range(P):
#     g, v = map(int, input().split())
#     p.append((g, v))
# p.sort(key=lambda x: -x[1])
# dsu = DSU(G)
# value = 0
# for g, v in p:
#     available = dsu.find(g)
#
#     if available == 0:
#         continue
#     value += v
#     dsu.union(available, available - 1)
# print(value)

#
# import heapq
#
# def minimize_reduction_cost(arr):
#
#     heap = []
#     n = len(arr)
#     for i in range(n - 1):
#         cost = max(arr[i], arr[i + 1])
#         heapq.heappush(heap, (cost, i))
#     total_cost = 0
#     while len(arr) > 1:
#
#         cost, idx = heapq.heappop(heap)
#         total_cost += cost
#         arr[idx] = max(arr[idx], arr[idx + 1])
#         arr.pop(idx + 1)
#         heap = []
#         for i in range(len(arr) - 1):
#             heapq.heappush(heap, (max(arr[i], arr[i + 1]), i))
#
#     return total_cost
#
#
# def main():
#
#     N = int(input())
#     arr = [int(input()) for _ in range(N)]
#     print(minimize_reduction_cost(arr))
#
#
# if __name__ == "__main__":
#     main()
