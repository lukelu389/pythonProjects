import csv


def BFS(maze, start, end):
    possibleCell = (start)
    frontier = [start]
    explored = [start]
    bfspath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == end:
            break
        for i in 'ESNW':
            if maze[currCell][i] == 1:
                if i == 'E':
                    possibleCell = (currCell[0], currCell[1] + 1)

                elif i == 'W':
                    possibleCell = (currCell[0], currCell[1] - 1)

                elif i == 'N':
                    possibleCell = (currCell[0] - 1, currCell[1])

                elif i == 'S':
                    possibleCell = (currCell[0] + 1, currCell[1])

                if possibleCell in explored:
                    continue

                frontier.append(possibleCell)
                explored.append(possibleCell)
                bfspath[possibleCell] = currCell

    path = {}
    cell = end
    while cell != start:
        path[bfspath[cell]] = cell
        cell = bfspath[cell]
    return path


maze = {}
R, M = list(map(int, input("Input an N by M matrix").split()))
the_maze = [list(map(int, input("Input the setup of the maze where'0' represent an available path, whereas '1' "
                                "represents obstacles").split())) for _ in range(R)]
start_pos = tuple(map(int, input("Input the starting position, note that index start with '0'").split()))
end_pos = tuple(map(int, input("Input the ending position, note that index start with '0'").split()))

for k in range(R):
    for j in range(M):
        N, W, S, E = 1, 1, 1, 1
        if k == 0:
            N = 0
            if the_maze[k + 1][j] == 1:
                S = 0
        if k == R - 1:
            S = 0
            if the_maze[k - 1][j] == 1:
                N = 0
        if j == 0:
            W = 0
            if the_maze[k][j + 1] == 1:
                E = 0
        if j == M - 1:
            E = 0
            if the_maze[k][j - 1] == 1:
                W = 0

        if 0 < k < R - 1:
            if the_maze[k - 1][j] == 1:
                N = 0
            if the_maze[k + 1][j] == 1:
                S = 0
        if 0 < j < M - 1:
            if the_maze[k][j - 1] == 1:
                W = 0
            if the_maze[k][j + 1] == 1:
                E = 0

        maze[(k, j)] = {'N': N, 'S': S, 'E': E, 'W': W}

temp = BFS(maze, start_pos, end_pos)
keys = list(temp.keys())
path = [start_pos]
for i in range(len(keys)):
    path.append(temp[keys.pop()])
print(temp)

file_path = "/Users/lukelu/PycharmProjects/pythonProjects/year2024/data_maze.csv"

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    for i in path:
        writer.writerow(i)

