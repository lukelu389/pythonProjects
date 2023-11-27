from tank import Tank

tanks = {1: Tank("Player 1"), 2: Tank("Player 2"), 3: Tank("Player 3")}
alive_tanks = len(tanks)

while alive_tanks > 1:
    for player in sorted(tanks.keys()):
        print(player, tanks[player])
    first = int(input("Who fires? "))
    second = int(input("Aim to whom?"))

    try:
        first_tank = tanks[first]
        second_tank = tanks[second]
    except KeyError as name:
        print("No such tank", name)
        continue

    if not first_tank.alive or not second_tank.alive:
        print("One of the tanks is already exterminated!")

    print("*" * 30)
    first_tank.fire_at(second_tank)

    if not second_tank.alive:
        alive_tanks -= 1

    print("*" * 30)

for tank in tanks.values():
    if tank.alive:
        print(tank.name, " is the winner of the match!")
        break