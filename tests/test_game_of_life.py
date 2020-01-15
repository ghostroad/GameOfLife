from game_of_life import Universe


def test_show():
    universe = Universe((0, 0), (1, 0), (2, 0))
    assert universe.show((-1, -1), (3, 1)) == ("     \n"
                                               " ### \n"
                                               "     ")


def test_empty_universe():
    universe = Universe()
    assert universe.show((-1, -1), (3, 1)) == ("     \n"
                                               "     \n"
                                               "     ")
    universe.tick()
    assert universe.show((-1, -1), (3, 1)) == ("     \n"
                                               "     \n"
                                               "     ")


def test_tick():
    universe = Universe((0, 0), (1, 0), (2, 0))
    universe.tick()
    assert universe.show((-1, -1), (3, 1)) == ("  #  \n"
                                               "  #  \n"                                           
                                               "  #  ")
    universe.tick()
    assert universe.show((-1, -1), (3, 1)) == ("     \n"
                                               " ### \n"
                                               "     ")


def test_beacon():
    universe = Universe((0, 0), (0, 1), (1, 0), (3, 3), (2, 3), (3, 2))
    universe.tick()
    assert universe.show((-1, -1), (4, 4)) == ("      \n"
                                               "   ## \n"
                                               "   ## \n"
                                               " ##   \n"
                                               " ##   \n"
                                               "      ")

    universe.tick()
    assert universe.show((-1, -1), (4, 4)) == ("      \n"
                                               "   ## \n"
                                               "    # \n"
                                               " #    \n"
                                               " ##   \n"
                                               "      ")


def tests_glider():
    universe = Universe((0, 0), (1, 0), (1, 1), (2, 1), (0, 2))
    assert universe.show((-1, -1), (4, 4)) == ("      \n"
                                               "      \n"
                                               " #    \n"
                                               "  ##  \n"
                                               " ##   \n"
                                               "      ")
    universe.tick()
    assert universe.show((-1, -1), (4, 4)) == ("      \n"
                                               "      \n"
                                               "  #   \n"
                                               "   #  \n"
                                               " ###  \n"
                                               "      ")
    universe.tick()
    assert universe.show((-1, -2), (4, 4)) == ("      \n"
                                               "      \n"
                                               "      \n"
                                               " # #  \n"
                                               "  ##  \n"
                                               "  #   \n"
                                               "      ")


def test_r_pentomino():
    universe = Universe((1, 0), (0, 1), (1, 1), (1, 2), (2, 2))
    for i in range(100):
        universe.tick()
    assert universe.show((-1, -1), (4, 4)) == (" ###  \n"
                                               "# # ##\n"
                                               "#   # \n"
                                               "# #   \n"
                                               " ## # \n"
                                               "   ###")


