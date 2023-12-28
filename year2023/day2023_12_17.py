N = int(input())

# adjacent list
graph = {}
visited = [False for i in range(N+1)]

# Djikstra
distance = [N+1 for j in range(N+1)]
distance_min = N + 1

for i in range(N):
    line = input().split()
    if int(len(line)) == 0:
        graph[i + 1] = []
        continue

    connected = [int(line[j]) for j in range(1, len(line))]
    graph[i+1] = connected


# dfs
stack = [1]
visited[1] = True
distance[1] = 1


while len(stack) > 0:

    current = stack.pop()
    current_distance = distance[current]

    for connected in graph[current]:
        if len(graph[connected]) == 0:
            visited[connected] = True
            if distance_min > current_distance:
                distance_min = current_distance

        else:
            if current_distance + 1 > distance[connected]:
                distance[connected] = current_distance + 1
                visited[connected] = False

            if not visited[connected]:
                stack.append(connected)
                visited[connected] = True

all_visited = True
for i in range(1, len(visited)):
    if not visited[i]:
        all_visited = False

if all_visited:
    print("Y")
else:
    print("N")

print(distance_min)
