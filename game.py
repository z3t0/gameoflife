"""
 Rules of Life
 - Death
    If there is no surrounding unit alive then die

"""
import random
import time
import sys
from colorama import Fore, Style

size = None
spawn = None


def usage():
    print("Usage: game.py size spawn")


def main():
    global size
    global spawn

    if len(sys.argv) < 3:
        usage()
        return
    else:
        try:
            size = int(sys.argv[1])
            spawn = int(sys.argv[2])
        except:
            usage()
            return

    print("My Game of Life")

    world = [[0] * size for _ in range(size)]

    for x in range(spawn):
        seed(world, 0, size, 0, size)

    pworld(world)

    time.sleep(2)

    rounds = 0

    while(True):
        if not loop(world):
            break

        rounds = rounds + 1
        pworld(world)

        time.sleep(1)

    print()
    print("Survived:", rounds)


def seed(world, minX, maxX, minY, maxY):
    x = random.randint(minX, maxX - 1)
    y = random.randint(minY, maxY - 1)

    world[x][y] = 1


def loop(world):
    living = False
    action = False

    for y in range(len(world)):
        for x in range(len(world[y])):
            if world[y][x]:
                # Alive
                living = True

            if act(world[y][x], world, x, y):
                action = True

    if living and action:
        return True
    else:
        return False


def act(unit, world, x, y):
    """
    Makes a decision for the unit based on surrounding units
    """
    resource = surrounding(unit, world, x, y)

    if unit:
        # Currently alive
        if resource < 2:
            die(unit, world, x, y)
            return True
        elif resource > 3:
            die(unit, world, x, y)
            return True
    else:
        if resource > 3:
            live(unit, world, x, y)
            return True
        # Currently Dead

    return False


def live(unit, world, x, y):
    # print("Born: ", x, y)
    world[y][x] = 1


def die(unit, world, x, y):
    # print("Killed: ", x, y)
    world[y][x] = 0


def isAlive(x, y, world):
    if x < 0 or x >= size or y < 0 or y >= size:
        return 0

    if world[y][x]:
        return 1
    else:
        return 0


def surrounding(unit, world, x, y):

    score = 0

    # Above
    score = score + isAlive(x, y - 1, world)

    # Below
    score = score + isAlive(x, y + 1, world)

    # Left
    score = score + isAlive(x - 1, y, world)

    # Right
    score = score + isAlive(x + 1, y, world)

    # Top right
    score = score + isAlive(x + 1, y - 1, world)

    # Top left
    score = score + isAlive(x - 1, y - 1, world)

    # Bottom right
    score = score + isAlive(x + 1, y + 1, world)

    # Bottom left
    score = score + isAlive(x - 1, y + 1, world)

    return score


def pworld(world):
    for row in world:
        for element in row:
            if element:
                print(Fore.GREEN + "o", end=" ")
            else:
                print(Fore.RED + "x", end=" ")
        print(Style.RESET_ALL)

    print()


main()
