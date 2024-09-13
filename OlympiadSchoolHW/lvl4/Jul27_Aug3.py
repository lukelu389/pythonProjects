# works on java, exact same code
# N, Q = list(map(int, input().split()))
# query = list(map(int, input().split()))
#
# p_sum = [0] * (N+1)
# for i in range(1, N):
#     p_sum[i] = p_sum[i-1] + query[i-1]
# p_sum[-1] = p_sum[-2] + query[-1]
#
# for i in range(Q):
#     l, r = list(map(int, input().split()))
#     print((p_sum[r] - p_sum[l-1]) // (r-l+1))


# works in c++
# import sys
# input = sys.stdin.read
# data = input().split()
#
# N = int(data[0])
# K = int(data[1])
#
# values = list(map(int, data[2:2+N]))
#
# prefix_sum = 0
# remainder_map = {0: -1}
# max_length = -1
#
# for i in range(N):
#     prefix_sum += values[i]
#     remainder = prefix_sum % K
#
#     if remainder < 0:
#         remainder += K
#
#     if remainder in remainder_map:
#         max_length = max(max_length, i - remainder_map[remainder])
#     else:
#         remainder_map[remainder] = i
#
# print(max_length)

# def find_cycle(start, graph):
#     visited = {}
#     order = []
#     pos = start
#     while pos not in visited:
#         visited[pos] = len(order)
#         order.append(pos)
#         pos = graph[pos] - 1
#
#     cycle_start = visited[pos]
#     cycle_length = len(order) - cycle_start
#     return order, cycle_start, cycle_length
#
#
# N, K = list(map(int, input().split()))
# lst = list(map(int, input().split()))
# graph = lst
# order, cycle_start, cycle_length = find_cycle(0, graph)
# if K < cycle_start:
#     final_pos = order[K]
# else:
#     final_pos = order[cycle_start + (K - cycle_start) % cycle_length]
# print(final_pos + 1)

# N, M, K = list(map(int, input().split()))
# lst = [int(_) for _ in range(1, N+1)]
# due = [list(map(int, input().split())) for _ in range(M)]
#
#
#
# print(lst)

s = "daddaabaccbbacbddcddbdcbddd"
for i in range(len(s)):
    print(i+1, s[i])
    