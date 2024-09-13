# No class

import collections


def validPath(n, edges, source, destination):
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, visited):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True
        return False

    visited = set()
    return dfs(source, visited)


def maxAreaOfIsland(grid):
    def flood(i, j):
        nonlocal area
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        area += 1
        grid[i][j] = -1
        flood(i + 1, j)
        flood(i - 1, j)
        flood(i, j + 1)
        flood(i, j - 1)

    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                area = 0
                flood(i, j)
                max_area = max(max_area, area)
    return max_area

