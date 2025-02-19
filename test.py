# partition/making groups that is irrelevant of order, simple group making: disjoint set union/kruskal
# frequency: prefix/suffix sum, dictionary
# partition with specific order: tree(N nodes N-1 edges), graph
# binary-lifting, fenwick/binary tree
# dijkstra, dijkstra twice?, spfa/floyd warshall for negative edges
# dfs and bfs + all of the above
# floodfill
# backtracking, dp, binary search
# math, groups: what about: all possible - groups that are invalid = groups that are valid
# sweep line + queue or sweep line + segment tree

# input case very big > 1e9: dp, binary search

# binary search: sorted input, maximizing the minimum might need

# dp/recursion + memoization, top-down approach if the base cases are very simple, bottom-up approach if transition can be easily found

# adhoc/constructive/implementation: edge cases, tracing, subtasks first

# recursion limits, important for dfs and certain dp approach:
# import sys
# sys.setrecursionlimit(300000)

# example of sweepline + queue
# from sortedcontainers import SortedDict
#
#
# def compute_union_area(rectangles):
#     events = []  # Stores all x-coordinate events (left and right edges)
#
#     for x1, y1, x2, y2 in rectangles:
#         events.append((x1, y1, y2, 1))  # Left edge (Add y-interval)
#         events.append((x2, y1, y2, -1))  # Right edge (Remove y-interval)
#
#     events.sort()  # Sweep line: Sort events by x
#
#     active_intervals = SortedDict()  # Active y-intervals with counts
#     last_x = 0
#     total_area = 0
#
#     def compute_covered_length():
#         """Compute the total covered y-length from active intervals."""
#         total = 0
#         prev_y, count = 0, 0
#         for y, freq in active_intervals.items():
#             if count > 0:
#                 total += y - prev_y
#             count += freq
#             prev_y = y
#         return total
#
#     for x, y1, y2, event_type in events:
#         # Calculate area before updating active intervals
#         if active_intervals:
#             covered_length = compute_covered_length()
#             total_area += covered_length * (x - last_x)
#
#         # Update active intervals
#         active_intervals[y1] = active_intervals.get(y1, 0) + event_type
#         active_intervals[y2] = active_intervals.get(y2, 0) - event_type
#
#         # Remove zero-count intervals
#         if active_intervals[y1] == 0:
#             del active_intervals[y1]
#         if active_intervals[y2] == 0:
#             del active_intervals[y2]
#
#         last_x = x  # Move the sweep line
#
#     return total_area
#
#
# # Example Usage
# n = int(input())  # Number of rectangles
# rectangles = [tuple(map(int, input().split())) for _ in range(n)]
# print(compute_union_area(rectangles))


# bfs, refer to dijkstra for modification or other variants
# from collections import deque
#
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()  # Dequeue a node
#         if node not in visited:
#             print(node, end=" ")  # Process the node
#             visited.add(node)
#
#             # Enqueue all unvisited neighbors
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#

# import heapq
#
# def dijkstra(graph, start):
#     pq = []
#     heapq.heappush(pq, (0, start))
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     while pq:
#         current_dist, current_node = heapq.heappop(pq)
#         if current_dist > distances[current_node]:
#             continue
#
#         for neighbor, weight in graph[current_node]:
#             distance = current_dist + weight
#
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#
#     return distances
#
# # adj list
# graph = {
#     0: [(1, 4), (2, 1)],
#     1: [(0, 4), (2, 2), (3, 5)],
#     2: [(0, 1), (1, 2), (3, 8)],
#     3: [(1, 5), (2, 8)]
# }
#
# def dijkstra_matrix(graph, start):
#     V = len(graph)  # Number of vertices
#     pq = [(0, start)]  # (distance, node)
#     distances = [float('inf')] * V
#     distances[start] = 0
#     visited = [False] * V
#
#     while pq:
#         current_dist, current_node = heapq.heappop(pq)
#
#         if visited[current_node]:
#             continue
#         visited[current_node] = True
#         for neighbor in range(V):
#             weight = graph[current_node][neighbor]
#             if weight != float('inf') and not visited[neighbor]:
#                 new_dist = current_dist + weight
#                 if new_dist < distances[neighbor]:
#                     distances[neighbor] = new_dist
#                     heapq.heappush(pq, (new_dist, neighbor))
#
#     return distances

# adj matrix
#
# INF = float('inf')
# graph = [
#     [0, 4, 1, INF],
#     [4, 0, 2, 5],
#     [1, 2, 0, 8],
#     [INF, 5, 8, 0]
# ]


# kruskal / dsu
# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
#
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])  # Path compression
#         return self.parent[x]
#
#     def union(self, x, y):
#         xr, yr = self.find(x), self.find(y)
#         if xr == yr: return
#         if self.rank[xr] < self.rank[yr]: self.parent[xr] = yr
#         else:
#             self.parent[yr] = xr
#             if self.rank[xr] == self.rank[yr]: self.rank[xr] += 1


# floodfill, grid is in form of adjacency matrix

# from collections import deque
#
# def flood_fill_bfs(grid, x, y, target_color, new_color):
#     rows, cols = len(grid), len(grid[0])
#     if grid[x][y] != target_color:
#         return
#
#     queue = deque([(x, y)])
#     grid[x][y] = new_color  # Change the color
#
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
#
#     while queue:
#         r, c = queue.popleft()
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target_color:
#                 grid[nr][nc] = new_color  # Change the color
#                 queue.append((nr, nc))  # Add to queue

# lowest common ancestor

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to find path from root to node
def findPath(root, path, k):
    # Base Case
    if root is None:
        return False

    # Store current node in path
    path.append(root)

    # If node value is equal to k, or
    # if node exist in left subtree or
    # if node exist in right subtree return true
    if (root.data == k or
            findPath(root.left, path, k)
            or findPath(root.right, path, k)):
        return True

    # else remove root from path and return false
    path.pop()
    return False

# Function to find lca of two nodes
def lca(root, n1, n2):
    # To store paths to n1 and n2 from the root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if not findPath(root, path1, n1) or not findPath(root, path2, n2):
        return None

    # Compare the paths to get the first different value
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


if __name__ == '__main__':

    # construct the binary tree
    #             1
    #           /   \
    #          2     3
    #         / \   / \
    #        4  5  6   7

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    ans = lca(root, 4, 5)
    if ans is None:
        print("No common ancestor found")
    else:
        print(ans.data)

# from collections import defaultdict
#
# # This class represents an undirected graph using adjacency list representation
#
#
# class Graph:
#
#     def __init__(self, vertices):
#         self.V = vertices  # No. of vertices
#         self.graph = defaultdict(list)  # default dictionary to store graph
#
#     # function to add an edge to graph
#     def addEdge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
#
#     # A function used by isConnected
#     def DFSUtil(self, v, visited):
#         # Mark the current node as visited
#         visited[v] = True
#
#         # Recur for all the vertices adjacent to this vertex
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.DFSUtil(i, visited)
#
#     '''Method to check if all non-zero degree vertices are
#     connected. It mainly does DFS traversal starting from
#     node with non-zero degree'''
#
#     def isConnected(self):
#
#         # Mark all the vertices as not visited
#         visited = [False]*(self.V)
#
#         #  Find a vertex with non-zero degree
#         for i in range(self.V):
#             if len(self.graph[i]) != 0:
#                 break
#
#         # If there are no edges in the graph, return true
#         if i == self.V-1:
#             return True
#
#         # Start DFS traversal from a vertex with non-zero degree
#         self.DFSUtil(i, visited)
#
#         # Check if all non-zero degree vertices are visited
#         for i in range(self.V):
#             if visited[i] == False and len(self.graph[i]) > 0:
#                 return False
#
#         return True
#
#     '''The function returns one of the following values
#        0 --> If graph is not Eulerian
#        1 --> If graph has an Euler path (Semi-Eulerian)
#        2 --> If graph has an Euler Circuit (Eulerian)  '''
#
#     def isEulerian(self):
#         # Check if all non-zero degree vertices are connected
#         if self.isConnected() == False:
#             return 0
#         else:
#             # Count vertices with odd degree
#             odd = 0
#             for i in range(self.V):
#                 if len(self.graph[i]) % 2 != 0:
#                     odd += 1
#
#             '''If odd count is 2, then semi-eulerian.
#             If odd count is 0, then eulerian
#             If count is more than 2, then graph is not Eulerian
#             Note that odd count can never be 1 for undirected graph'''
#             if odd == 0:
#                 return 2
#             elif odd == 2:
#                 return 1
#             elif odd > 2:
#                 return 0
#
#      # Function to run test cases
#
#     def test(self):
#         res = self.isEulerian()
#         if res == 0:
#             print("graph is not Eulerian")
#         elif res == 1:
#             print("graph has a Euler path")
#         else:
#             print("graph has a Euler cycle")