#!/usr/bin/env python3
from pprint import pprint

# key = (x,y) val = . / #
grid = {}


def get_grid_val(x, y):
    x = x % 31
    return grid[(x, y)]


def read_input():

    y = 0
    with open("input", "r") as fp:
        for line in fp:
            for x in range(31):
                grid[(x, y)] = line[x]
            y = y + 1


def traverse(xadd, yadd):
    x = 0
    y = 0
    trees = 0
    try:
        while True:
            t = get_grid_val(x, y)
            if t == ".":
                pass
            elif t == "#":
                trees += 1
            x += xadd
            y += yadd
    except:
        pass

    return trees


def task1():
    print("Found {} trees".format(traverse(3, 1)))


def task2():
    t = traverse(1, 1)
    t *= traverse(3, 1)
    t *= traverse(5, 1)
    t *= traverse(7, 1)
    t *= traverse(1, 2)
    print("Product {}".format(t))


read_input()
task1()
task2()
