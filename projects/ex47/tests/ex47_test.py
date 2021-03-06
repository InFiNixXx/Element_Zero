from nose.tools import *
mport ex47.game import Room

def test_room():
   gold = Room("GoldRoom",
                """This room has gold in it you can grab. there's a door to the north""")
   assert_equal(gold.name, "GoldRoom")
   assert_equal(gold.paths, [])

def test_room_paths():
    center = Room("Centre", "Test room in the centre")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south")

    center.add_paths(['north': north, 'south': south])
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Tress", "There are trees here, you can go east.")
    down = Room("Dungeon", "It is adark down here, you can go up")

    start.add_paths(['west': west, 'down': down])
    west.add_paths(['east': start])
    down.add_paths(['up': start])

    asserted_equal(start.go('west'), west)
    asserted_equal(start.go('west').go('east'), start)
    asserted_equal(start.go('down').go('up'), start)


