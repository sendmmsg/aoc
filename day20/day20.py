#!/usr/bin/env python3
from parse import parse
from networkx.drawing.nx_agraph import write_dot
import matplotlib.pyplot as plt
import networkx as nx


def v2str(v):
    s = format(v, "b").zfill(10)
    return s.replace("1", "#").replace("0", ".")


class Tile:
    def __init__(self, id):
        self.id = id
        self.pic = []

    def addline(self, line):
        self.pic.append(line)

    def top(self):
        return self.pic[0]

    def top_flip(self):
        return self.top()[::-1]

    def bottom(self):
        return self.pic[9]

    def bottom_flip(self):
        return self.bottom()[::-1]

    def left(self):
        s = ""
        for p in self.pic:
            s += p[0]
        return s

    def left_flip(self):
        return self.left()[::-1]

    def right(self):
        s = ""
        for p in self.pic:
            s += p[9]
        return s

    def right_flip(self):
        return self.right()[::-1]

    def __repr__(self):
        s = ""
        #        s += f"Tile {self.id}\n"
        for n in self.pic:
            s += n + "\n"

        return s

    def drawborder(self, vers):
        v = self.versions[vers]
        print(self.versions[vers])
        top = v[0]
        right = v[1]
        bottom = v[2]
        left = v[3]
        top_s = v2str(top)
        right_s = v2str(right)
        left_s = v2str(left)
        bottom_s = v2str(bottom)
        if top_s[0] != left_s[0]:
            print("drawborder, mismatch topleft")
            exit()
        if top_s[9] != right_s[0]:
            print("drawborder, mismatch topright")
            exit()
        if bottom_s[0] != left_s[9]:
            print("drawborder, mismatch botleft")
            exit()
        if bottom_s[9] != right_s[9]:
            print("drawborder, mismatch botright")
            exit()
        # s = top_s + "\n"
        # for i in range(1, 9):
        #     s += "{}        {}\n".format(left_s[i], right_s[i])
        # s += bottom_s

        s = " ".join(top_s) + "\n"
        for i in range(1, 9):
            s += "{}                 {}\n".format(left_s[i], right_s[i])
        s += " ".join(bottom_s)

        print(s)

    def tonum(self):
        top = self.top()
        right = self.right()
        bottom = self.bottom()
        left = self.left()

        snum = []

        # Rotate 4
        sides = [top, right, bottom, left]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)
        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        sides = [sides[3][::-1], sides[0], sides[1][::-1], sides[2]]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)
        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        sides = [sides[3][::-1], sides[0], sides[1][::-1], sides[2]]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)
        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        sides = [sides[3][::-1], sides[0], sides[1][::-1], sides[2]]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)

        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        # Mirror image, and rotate
        # Rotate 4
        sides = [top[::-1], left, bottom[::-1], right]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)
        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        sides = [sides[3][::-1], sides[0], sides[1][::-1], sides[2]]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)
        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        sides = [sides[3][::-1], sides[0], sides[1][::-1], sides[2]]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)
        # print("sides: {}".format(sides))
        # print("num: {}".format(s))

        sides = [sides[3][::-1], sides[0], sides[1][::-1], sides[2]]
        s = []
        for val in sides:
            x = val.replace(".", "0").replace("#", "1")
            # print(x)
            x = int(x, 2)
            s.append(x)
        snum.append(s)

        self.versions = snum

        for n in self.versions:
            print(n)

        # print("All sides: {}".format(snum))


tt = {}
tiles = []
with open("input", "r") as fp:
    t = None
    for line in fp:
        if "Tile" in line:
            res = parse("Tile {}:", line)
            if t:
                t.tonum()
                tiles.append(t)
                tt[int(t.id)] = t
            t = Tile(res[0])
        elif len(line) > 3:
            t.addline(line.strip())
        else:
            print("next tile")
    t.tonum()
    tiles.append(t)
    tt[int(t.id)] = t


def drawline():
    print(
        "     {}                  {}                  {}".format(
            tt[1951].versions[0][0], tt[2311].versions[0][0], tt[3079].versions[0][0]
        )
    )
    print(
        "   {}  {}              {}  {}              {}  {} ".format(
            tt[1951].versions[0][3],
            tt[1951].versions[0][1],
            tt[2311].versions[0][3],
            tt[2311].versions[0][1],
            tt[3079].versions[0][3],
            tt[3079].versions[0][1],
        )
    )
    print(
        "     {}                  {}                  {}".format(
            tt[1951].versions[0][2], tt[2311].versions[0][2], tt[3079].versions[0][2]
        )
    )


# drawline()
# # exit()
# print("tile 2311")
# print("")
# print("")
# t = tiles[0]
# print(t)
# print("2311 top    {} , flipped {}".format(t.top(), t.top_flip()))
# print("2311 bottom {} , flipped {}".format(t.bottom(), t.bottom_flip()))
# print("2311 left   {} , flipped {}".format(t.left(), t.left_flip()))
# print("2311 right  {} , flipped {}".format(t.right(), t.right_flip()))
# # t.tonum()
# import time
# (* 3313 2551 1697 1129)

# while True:
#     for i in range(4, 8):
#         print(chr(27) + "[2J")
#         t.drawborder(i)
#         time.sleep(1)
# exit()

freq = {}
for t in tiles:
    print("Tile: ", t.id)
    for vers in t.versions:
        for v in vers:
            if v in freq:
                if t.id not in freq[v]:
                    freq[v].append(t.id)
            else:
                freq[v] = [t.id]
from pprint import pprint

pprint(freq)
print("")
count = {}
for n in freq:
    if len(freq[n]) > 1:
        continue
    if freq[n][0] in count:
        count[freq[n][0]] += 1
    else:
        count[freq[n][0]] = 1

pprint(count)


G = nx.Graph()

# for n in tt:
#     for i in range(8):
#         G.add_node("{}_{}".format(n, i))

for n in freq:
    for x in freq[n]:
        for y in freq[n]:
            if y == x:
                pass
            else:
                G.add_edge(x, y)
write_dot(G, "grid.dot")
grid = {}
grid[(0, 0)] = tt[3313]

node = grid[(0, 0)]

print(tiles)
print(node)
print(dir(node))


print(list(G.neighbors("3313")))
start_node = "3313"
end_node = "2551"
rows = []
prev_row = nx.shortest_path(G, "3313", "2551")
rows.append(nx.shortest_path(G, "3313", "2551"))


def next_row(rows):
    prev_row = rows[-1]
    start_node = prev_row[0]
    end_node = prev_row[-1]
    #   print("previous row: {}".format(prev_row))
    #   print("start: {} end: {}".format(start_node, end_node))
    new_start = [x for x in list(G.neighbors(start_node)) if x not in prev_row]
    try:
        new_start = [x for x in new_start if x not in rows[-2]]
    except Exception as e:
        pass
    new_end = [x for x in list(G.neighbors(end_node)) if x not in prev_row]
    try:
        new_end = [x for x in new_end if x not in rows[-2]]
    except Exception as e:
        pass

    #    print("new start: {}  new end: {}".format(new_start, new_end))
    new_row = nx.shortest_path(G, new_start[0], new_end[0])
    #    print("new row: {}".format(new_row))
    rows.append(new_row)


next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
next_row(rows)
grid = {}
for y in range(len(rows)):
    for x in range(len(rows[y])):
        grid[(x, y)] = tt[int(rows[y][x])]

pprint(grid)

# [3313, 2357, 3301, 3037, 2677, 2897, 2549, 2267, 1063, 3169, 1087, 2551],
# [1607, 3209, 1217, 2689, 3943, 2207, 1993, 3803, 1823, 1367, 3823, 3617],
