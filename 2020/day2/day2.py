#!/usr/bin/env python3
from parse import parse


def task1():
    good = 0
    with open("input", "r") as fp:
        for n in fp:
            a = parse("{}-{} {}: {}", n)
            nmin = int(a[0])
            nmax = int(a[1])
            char = a[2]
            passwd = a[3]
            count = passwd.count(char)

            if nmin <= count and count <= nmax:
                print("GOOD {} <= {} <= {}".format(nmin, count, nmax))
                good = good + 1
            else:
                print("BAD {}  {}  {}".format(nmin, count, nmax))
    print("Valid passwords: {}".format(good))


def task2():
    good = 0
    with open("input", "r") as fp:
        for n in fp:
            a = parse("{}-{} {}: {}", n)
            nmin = int(a[0])
            nmax = int(a[1])
            char = a[2]
            passwd = a[3]

            char1 = passwd[nmin - 1]
            char2 = passwd[nmax - 1]
            valid = False
            if char1 == char and not char2 == char:
                valid = True
            elif char2 == char and not char1 == char:
                valid = True
            else:
                print(
                    "BAD passwd {} char {} pos {}({})-{}({})".format(
                        passwd, char, nmin - 1, char1, nmax - 1, char2
                    )
                )
            if valid:
                good = good + 1

                print(
                    "GOOD passwd {} char {} pos {}({})-{}({})".format(
                        passwd, char, nmin - 1, char1, nmax - 1, char2
                    )
                )

    print("Valid passwords: {}".format(good))


task2()
