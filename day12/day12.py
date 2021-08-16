#!/usr/bin/env python3
from parse import parse


def abs(x):
    if x >= 0:
        return x
    return -x


class Test:
    def __init__(self):
        self.direction = [1, 0]
        self.pos_x = 0
        self.pos_y = 0

    # x W  -inf <--  0  --> inf E
    # y N
    #   +
    #
    #   -
    #   S
    def turn_right(self):
        print("turning right")
        if self.direction == [1, 0]:
            self.direction = [0, -1]
        elif self.direction == [0, -1]:
            self.direction = [-1, 0]
        elif self.direction == [-1, 0]:
            self.direction = [0, 1]
        elif self.direction == [0, 1]:
            self.direction = [1, 0]
        else:
            print("Something wrong with the steering")

    def turn_left(self):
        print(f"\n turning left from {self.direction}")

        if self.direction == [1, 0]:
            self.direction = [0, 1]
        elif self.direction == [0, 1]:
            self.direction = [-1, 0]
        elif self.direction == [-1, 0]:
            self.direction = [0, -1]
        elif self.direction == [0, -1]:
            self.direction = [1, 0]
        else:
            print("Something wrong with the steering")
        print(f" to  {self.direction}")

    def change_dir(self, cmd, val):
        turn = 0
        if val == 90:
            turn = 1
        elif val == 180:
            turn = 2
        elif val == 270:
            turn = 3
        elif val == 360:
            turn = 4

        for n in range(turn):
            if cmd == "L":
                self.turn_left()
            elif cmd == "R":
                self.turn_right()
            else:
                print("Something wrong with the wheel")

    def move_forward(self, val):
        self.pos_x += val * self.direction[0]
        self.pos_y += val * self.direction[1]

    def main(self):
        with open("input", "r") as fp:
            for line in fp:
                (command, value) = parse("{}{:d}", line)
                print(
                    f"Start [{self.pos_x}, {self.pos_y}]  dir {self.direction}  ->  {command}{value}",
                    end="",
                )
                if "L" in command or "R" in command:
                    self.change_dir(command, value)
                elif "F" in command:
                    self.move_forward(value)
                elif "N" in command:
                    self.pos_y += value
                elif "S" in command:
                    self.pos_y -= value
                elif "E" in command:
                    self.pos_x += value
                elif "W" in command:
                    self.pos_x -= value
                else:
                    print("Unknown command!")
                print(f"  -> [{self.pos_x}, {self.pos_y}]  dir {self.direction}")
            print("manhattan {}".format(abs(self.pos_x) + abs(self.pos_y)))


if __name__ == "__main__":
    t = Test()
    t.main()
