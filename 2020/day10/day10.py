#!/usr/bin/env python3

jolts = sorted([0, 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])

jolts = sorted(
    [
        0,
        52,
        28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,
    ]
)

jolts = sorted(
    [
        0,
        170,
        1,
        100,
        101,
        104,
        107,
        108,
        109,
        11,
        112,
        115,
        116,
        117,
        118,
        119,
        12,
        122,
        125,
        126,
        127,
        13,
        130,
        133,
        134,
        135,
        136,
        137,
        14,
        140,
        141,
        142,
        143,
        146,
        147,
        148,
        151,
        152,
        153,
        154,
        155,
        158,
        159,
        160,
        161,
        162,
        165,
        166,
        167,
        17,
        18,
        19,
        2,
        20,
        21,
        24,
        27,
        28,
        29,
        3,
        30,
        31,
        34,
        37,
        4,
        40,
        41,
        42,
        45,
        48,
        49,
        50,
        51,
        54,
        55,
        56,
        57,
        60,
        61,
        62,
        63,
        66,
        69,
        7,
        70,
        71,
        72,
        75,
        76,
        77,
        78,
        79,
        8,
        82,
        83,
        84,
        85,
        88,
        91,
        94,
        95,
        98,
        99,
    ]
)
print(jolts)

prev = 0
count1 = 0
count3 = 1
diffs = []
for curr in jolts:
    diff = curr - prev
    diffs.append(diff)
    if diff == 1:
        count1 += 1
    elif diff == 3:
        count3 += 1
    prev = curr

print(f"1s:{count1} , 3s:{count3}")
print("product is {}".format(count1 * count3))

print(diffs)
import math

run_length = 0
num_paths = 1
for n in diffs:
    if n == 1:
        run_length += 1
    if n == 3:
        if run_length > 0:
            k = 1
            if run_length == 2:
                k = 2
                num_paths *= k
            if run_length == 3:
                k = 4
                num_paths *= k
            if run_length == 4:
                k = 7
                num_paths *= k

            print("run_length: {} paths: {} total: {}".format(run_length, k, num_paths))
            run_length = 0
print("final run length: {}".format(run_length))
print("number of paths: {} ".format(num_paths))

# paths = 1
# for curr in jolts:
#     print("Checking {}".format(curr))
#     num = 0
#     if curr - 1 in jolts:
#         num += 1
#     if curr - 2 in jolts:
#         num += 1
#     if curr - 3 in jolts:
#         num += 1
#     if num > 0:
#         print("\t{} * {} = {}".format(paths, num, paths * num))
#         paths = paths * num
#     else:
#         print("\tno matches found for {}".format(curr))

# print(f"number of {paths}")


import networkx as nx

G = nx.DiGraph()


for curr in jolts:
    G.add_node(curr)
    if curr + 1 in jolts:
        G.add_node(curr + 1)
        G.add_edge(curr, curr + 1)
    if curr + 2 in jolts:
        G.add_node(curr + 2)
        G.add_edge(curr, curr + 2)
    if curr + 3 in jolts:
        G.add_node(curr + 3)
        G.add_edge(curr, curr + 3)

from networkx.drawing import nx_pydot

P = nx_pydot.to_pydot(G)
with open("jolts.dot", "w") as fp:
    fp.write(P.to_string())
# # print(G.nodes())
# # print(G.edges())
# num_paths = 0
# for path in nx.all_simple_paths(G, 0, 170):
#     #    print(path)
#     num_paths += 1
# print("number of paths {}".format(num_paths))


# 0 1 2 3 4 7
#  1 1 1 1 3

#  0 1 2 3 4
#  0 1   3 4
#  0 1 2   4
#  0 1     4
#  0 2   3 4
#  0 2     4
#  0     3 4  = 7
