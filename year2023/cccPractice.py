rows = int(input())
cols = int(input())

rooms = []

for i in range(rows):
    rooms.append([int(i) for i in input().split()])

tree = {rooms[0][0]: []}



