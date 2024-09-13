import pygame
import csv

pygame.init()


def read_maze_from_csv(file_path):
    maze = []
    start = None
    end = None
    width = 0
    height = 0

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)

        width, height = map(int, next(reader))

        start = tuple(map(int, next(reader)))
        end = tuple(map(int, next(reader)))

        for row in reader:
            maze.append(list(map(int, row)))

    return maze, width * 20, height * 20, start, end


def draw_maze(screen, maze, path=None):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if path and (x, y) in path:
                pygame.draw.rect(screen, (0, 0, 255), (x * 20, y * 20, 20, 20))
            elif cell == 1:
                pygame.draw.rect(screen, (139, 69, 19), (x * 20, y * 20, 20, 20))
            elif cell == 0:
                pygame.draw.rect(screen, (255, 255, 153), (x * 20, y * 20, 20, 20))


def draw_runner(screen, x, y):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 20, 20))


def animate_bfs(screen, maze, start_pos, end_pos):
    global runner_x, runner_y
    queue = [start_pos]
    visited = set()
    parent = {}
    found = False
    while queue:
        current = queue.pop(0)
        print("Current position:", current)
        if current == end_pos:
            found = True
            break
        visited.add(current)
        x, y = current
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current
        draw_maze(screen, maze, visited)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for pos in visited:
            draw_runner(screen, pos[0] * 20, pos[1] * 20)
        pygame.display.flip()
        pygame.time.wait(100)
    if found:
        current = end_pos
        shortest_path = []
        while current != start_pos:
            shortest_path.append(current)
            current = parent[current]
        shortest_path.append(start_pos)
        print("Shortest path:", shortest_path)
        draw_maze(screen, maze, shortest_path[::-1])
        pygame.display.flip()
        pygame.time.wait(100)
    else:
        print("No path found from start to end.")


maze_file_path = "maze.csv"
maze, maze_width, maze_height, start_pos, end_pos = read_maze_from_csv(maze_file_path)

screen = pygame.display.set_mode((maze_width, maze_height))
pygame.display.set_caption("Maze Shortest Path")

animate_bfs(screen, maze, start_pos, end_pos)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

