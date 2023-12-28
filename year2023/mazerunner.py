def BFS(maze, maze_row, maze_col):
    start = (maze_row - 1, maze_col - 1)

    frontier = [start]
    explored = [start]
    bfspath = {}
    while len(frontier) > 0:
        currCell = frontier.pop(0)
        if currCell == (0, 0):
            break

        for i in 'ESNW':
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
    cell = (0, 0)
    while cell != start:
        path[bfspath[cell]] = cell
        cell = bfspath[cell]
    return path


maze = {}

the_maze = [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for k in range(len(the_maze)):
    for j in range(len(the_maze[k])):
        N, W, S, E = 0, 0, 0, 0
        if k != 0 and k != len(the_maze) - 1:
            if the_maze[k + 1][j] == 0:
                S = 1
            if the_maze[k - 1][j] == 0:
                N = 1
        if j != 0 and j != len(the_maze[0]) - 1:
            if the_maze[k][j + 1] == 0:
                E = 1
            if the_maze[k][j - 1] == 0:
                W = 1

        maze[(k, j)] = {'N': N, 'S': S, 'E': E, 'W': W}

print(BFS(maze, len(the_maze), len(the_maze[0])))
