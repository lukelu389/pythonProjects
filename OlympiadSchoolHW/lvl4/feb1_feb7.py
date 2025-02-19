from collections import defaultdict

graph = defaultdict(list)
parent = []
depth = []
distance = []

def add_edge(a, b, w):
    graph[a].append((b, w))
    graph[b].append((a, w))

def dfs(node, par, d, dist):
    parent[node] = par
    depth[node] = d
    distance[node] = dist

    for neighbor, weight in graph[node]:
        if neighbor != par:
            dfs(neighbor, node, d + 1, dist + weight)


def find_lca_and_distance(u, v):

    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]

    while u != v:
        u = parent[u]
        v = parent[v]

    return u

def main():
    # Read input


    n = int(input())
    global parent, depth, distance
    parent = [-1] * n
    depth = [0] * n
    distance = [0] * n
    for i in range(1, n):
        a, b, w = list(map(int, input().split()))
        add_edge(a, b, w)

    dfs(0, -1, 0, 0)


    q = int(input())
    result = []

    for i in range(q):
        u, v = list(map(int, input().split()))
        lca = find_lca_and_distance(u, v)
        total_distance = distance[u] + distance[v] - 2 * distance[lca]
        print(total_distance)


if __name__ == "__main__":
    main()
