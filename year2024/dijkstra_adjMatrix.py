# Python program for Dijkstra's single source the shortest path algorithm.
# The program is for adjacency matrix representation of the graph

# Library for INT_MAX
import sys


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        for node in range(self.V):
            if node == 0:
                continue
            elif dist[node] == sys.maxsize:
                print(-1)

            else:
                print(dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in the shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        global min_index
        mini = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < mini and not sptSet[u]:
                mini = dist[u]
                min_index = u

        return min_index

    # Function that implements Dijkstra's single source the shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for count in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        # return dist
        self.printSolution(dist) # --> line 15


# V = int(input())
# E = int(input())
# aGraph = [[0 for i in range(V + 1)] for i in range(V + 1)]
#
# for i in range(E):
#     temp = [int(j) for j in input().split()]
#     aGraph[temp[0]][temp[1]] = temp[2]
#     aGraph[temp[1]][temp[0]] = temp[2]
#
# source = int(input())
# price = [0] * (V + 1)
# for i in range(V):
#     temp = [int(j) for j in input().split()]
#     price[temp[0]] = temp[1]
#
# destination = int(input())
#
# g = Graph(V + 1)
# g.graph = aGraph
#
# print(g.dijkstra(source)[destination] + price[source])
