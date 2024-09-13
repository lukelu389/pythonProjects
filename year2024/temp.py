# magnetic marble

number, action = [int(i) for i in input().split()]
configuration = [int(i) for i in input()]
d = []
strike = 0


def merge(arrange):
    i = 0
    while i < len(arrange) - 1:
        if arrange[i] == arrange[i + 1] == 1:
            arrange[i] = 0
            arrange[i + 1] = 1
        i += 1
    return arrange


configuration = merge(configuration)

if action == 0 and configuration.count(1) == 0:
    print(0)

elif configuration.count(1) == 0:
    print(0)

elif action == 0:
    print(configuration.count(1))

else:
    while configuration[0] == 0:
        configuration.pop(0)

    while configuration[len(configuration) - 1] == 0:
        configuration.pop()

    temp = 0
    for i in range(len(configuration)):
        if configuration[i] == 1:
            strike += 1

        if strike == 2:
            d.append(temp)
            strike, temp = 1, 0

        if configuration[i] == 0:
            temp += 1

    d.sort()
    temp = len(d)
    for i in d:
        if action - i < 0:
            break
        else:
            action -= i
            temp -= 1

    if not d and action > 0:
        print(configuration.count(1))
    elif temp == 1:
        print(2)
    elif temp % 2 == 1:
        print(temp)
    else:
        print(temp + 1)


# dijkstra
import collections
import heapq

V, E = [int(i) for i in input().split()]
times = []
for i in range(E):
    times.append([int(i) for i in input().split()])

g = collections.defaultdict(dict)
for frm, to, cost in times:
    g[frm][to] = cost

    g[to][frm] = cost


def calculate_distances(graph, v):
    distances = {vertex: float("inf") for vertex in graph}
    distances[v] = 0

    pq = [(0, v)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# calculate distance can be optimizes
if V == 2:
    print(times[0][2])
else:
    path = []
    for i in range(V):
        path.append(calculate_distances(g, 0)[i] + calculate_distances(g, i)[V - 1])
    print(max(path))

