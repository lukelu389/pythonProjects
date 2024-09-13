# Python3 implementation of SPFA
from collections import deque

# Graph is stored as vector of vector of pairs
# first element of pair store vertex
# second element of pair store weight
graph = [[] for _ in range(100000)]


# Function to add edges in the graph
# connecting a pair of vertex(frm) and weight
# to another vertex(to) in graph
def addEdge(frm, to, weight):
    graph[frm].append([to, weight])


# Function to print shortest distance from source
def print_distance(d, V):
    print("Vertex", "\t", "Distance from source")

    for i in range(1, V + 1):
        print(i, "\t", d[i])


# Function to compute the SPF algorithm
def shortestPathFaster(S, V):
    # Create array d to store shortest distance
    d = [10 ** 9] * (V + 1)

    # Boolean array to check if vertex
    # is present in queue or not
    inQueue = [False] * (V + 1)
    d[S] = 0
    q = deque()
    q.append(S)
    inQueue[S] = True

    while len(q) > 0:
        # Take the front vertex from Queue
        u = q.popleft()
        inQueue[u] = False

        # Relaxing all the adjacent edges of
        # vertex taken from the Queue
        for i in range(len(graph[u])):

            v = graph[u][i][0]
            weight = graph[u][i][1]

            if d[v] > d[u] + weight:
                d[v] = d[u] + weight

                # Check if vertex v is in Queue or not
                # if not then append it into the Queue
                if not inQueue[v]:
                    q.append(v)
                    inQueue[v] = True

    # Print the result
    print_distance(d, V)


# Driver code
if __name__ == '__main__':
    V = 5
    S = 1

    # Connect vertex a to b with weight w
    # addEdge(a, b, w)

    addEdge(1, 2, 1)
    addEdge(2, 3, 7)
    addEdge(2, 4, -2)
    addEdge(1, 3, 8)
    addEdge(1, 4, 9)
    addEdge(3, 4, 3)
    addEdge(2, 5, 3)
    addEdge(4, 5, -3)

    # Calling shortestPathFaster function
    shortestPathFaster(S, V)

# floyd warshall: intermediate, start, end
# adj matrix


# Number of vertices in the graph
V = 4

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999


# Solves all pair shortest path
# via Floyd Warshall Algorithm


def floydWarshall(graph):
    """ dist[][] will be the output matrix that will finally have the shortest distances between every pair of vertices
initializing the solution matrix same as input graph matrix OR we can say that the initial values of shortest distances
are based on shortest paths considering no intermediate vertices """

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    """ Add all vertices one by one to the set of intermediate vertices. ---> Before start of an iteration, 
we have shortest distances between all pairs of vertices such that the shortest distances consider only the 
vertices in the set {0, 1, 2, .. k-1} as intermediate vertices. ----> After the end of a iteration, vertex no. k is
added to the set of intermediate vertices and the set becomes {0, 1, 2, .. k} """
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances\
between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % "INF", end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V - 1:
                print()


# Driver's code
if __name__ == "__main__":
    """
                    10
               (0)------->(3)
                |         /|\
              5 |          |
                |          | 1
               \|/         |
               (1)------->(2)
                    3           """

    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    # Function call
    floydWarshall(graph)


