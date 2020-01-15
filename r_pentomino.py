from game_of_life import Universe

universe = Universe((1, 0), (0, 1), (1, 1), (1, 2), (2, 2))
while True:
    print(universe.show((-20, -20), (80, 20)))
    input("Press Enter to continue...")
    universe.tick()
