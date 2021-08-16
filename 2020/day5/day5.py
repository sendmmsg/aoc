#!/usr/bin/env python3


def task1():
    max_seat = 0
    with open("input", "r") as fp:
        for line in fp:
            row = int(line[0:7].replace("F", "0").replace("B", "1"), base=2)
            column = int(line[7:].replace("L", "0").replace("R", "1"), base=2)
            seat_id = row * 8 + column
            print("ID {} (row {} column {})".format(seat_id, row, column))
            if seat_id > max_seat:
                max_seat = seat_id
    print("max seat id: {}".format(max_seat))


def task2():
    seats = list(range(80, 873))
    with open("input", "r") as fp:
        for line in fp:
            row = int(line[0:7].replace("F", "0").replace("B", "1"), base=2)
            column = int(line[7:].replace("L", "0").replace("R", "1"), base=2)
            seats.remove(row * 8 + column)

    for seat_id in seats:
        column = seat_id % 8
        row = (seat_id - column) / 8
        print("Row {} Column {}".format(row, column))


task2()
