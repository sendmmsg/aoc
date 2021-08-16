#!/usr/bin/env python3

gridA = {}


def plot_grid(g, mx, my):
    for y in range(my + 1):
        for x in range(mx + 1):
            print(g[(x, y)], end="")
        print("")


def get_adjecent(g, x, y):
    seats = []
    keys = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    for k in keys:
        if k in g:
            seats.append(g[k])
    occupied = 0
    for s in seats:
        if s == "#":
            occupied += 1

    return occupied


# recursivly look for # by applying kx,ky to x,y until leaving the field
# or finding a #
def find_occupied(g, x, y, kx, ky):
    x = x + kx
    y = y + ky

    if x < 0 or x > max_x:
        return 0
    if y < 0 or y > max_y:
        return 0
    if g[(x, y)] == "#":
        return 1
    if g[(x, y)] == "L":
        return 0

    return find_occupied(g, x, y, kx, ky)


def get_adjecent2(g, x, y):

    occupied = 0
    occupied += find_occupied(g, x, y, -1, -1)
    occupied += find_occupied(g, x, y, 0, -1)
    occupied += find_occupied(g, x, y, 1, -1)

    occupied += find_occupied(g, x, y, -1, 0)
    occupied += find_occupied(g, x, y, 1, 0)

    occupied += find_occupied(g, x, y, -1, 1)
    occupied += find_occupied(g, x, y, 0, 1)
    occupied += find_occupied(g, x, y, 1, 1)

    return occupied


def apply_rules(g, mx, my):
    newgrid = {}
    for y in range(my + 1):
        for x in range(mx + 1):
            seat = g[(x, y)]
            if seat == ".":
                newgrid[(x, y)] = "."
            elif seat == "L":
                occupied = get_adjecent(g, x, y)
                if occupied == 0:
                    newgrid[(x, y)] = "#"
                    continue
            elif seat == "#":
                occupied = get_adjecent(g, x, y)
                if occupied >= 4:
                    newgrid[(x, y)] = "L"
                    continue
            newgrid[(x, y)] = g[(x, y)]

    return newgrid


def apply_rules2(g, mx, my):
    newgrid = {}
    for y in range(my + 1):
        for x in range(mx + 1):
            seat = g[(x, y)]
            if seat == ".":
                newgrid[(x, y)] = "."
            elif seat == "L":
                occupied = get_adjecent2(g, x, y)
                #   print("{}: {},{} sees {}".format(seat, x, y, occupied))
                if occupied == 0:
                    newgrid[(x, y)] = "#"
                    continue
            elif seat == "#":
                occupied = get_adjecent2(g, x, y)
                # print("{}: {},{} sees {}".format(seat, x, y, occupied))
                if occupied >= 5:
                    newgrid[(x, y)] = "L"
                    continue
            newgrid[(x, y)] = g[(x, y)]

    return newgrid


y = 0
with open("input", "r") as fp:
    for line in fp:
        if len(line) < 2:
            continue
        for x in range(len(line) - 1):
            gridA[(x, y)] = line[x]
        y += 1
y -= 1
max_x = x
max_y = y
print(f"x: {x} y: {y}")
import time

while True:
    plot_grid(gridA, max_x, max_y)
    gridB = apply_rules2(gridA, max_x, max_y)
    if gridB == gridA:
        print("Steady state!")
        break
    gridA = gridB
    # time.sleep(1)
    # print("")
    print(chr(27) + "[2J")

occupied = 0
for n in gridA:
    if gridA[n] == "#":
        occupied += 1
print(f"{occupied} seats occupied")
