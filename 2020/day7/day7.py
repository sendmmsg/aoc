#!/usr/bin/env python3.8
input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
from pprint import pprint


def with_input1():
    with open("input", "r") as fp:
        i = 0
        for l in fp:
            l = l.replace("bags", "").replace("bag", "")
            a = l.replace("contain", ":").split(":")
            left = a[0].strip()
            right = a[1]
            right = right.replace(".", "").strip()
            right = right.split(",")
            newright = []
            for n in right:
                newright.append(n.strip())
            right = newright
            print(i, "{} => {}".format(left, right))
            i += 1
            for x in right:
                y = x[2:].strip()
                if "other" in y:
                    continue
                print("{} -> {}".format(y, left))
                add_link(y, left)
                G.add_node(y)
                G.add_node(left)
                G.add_edge(left, y)


def with_input2():
    with open("input", "r") as fp:
        i = 0
        for l in fp:
            l = l.replace("bags", "").replace("bag", "")
            a = l.replace("contain", ":").split(":")
            left = a[0].strip()
            right = a[1]
            right = right.replace(".", "").strip()
            right = right.split(",")
            newright = []
            for n in right:
                newright.append(n.strip())
            right = newright
            print(i, "{} => {}".format(left, right))
            i += 1
            for x in right:
                y = x[2:].strip()
                if "other" in y:
                    continue
                cost = int(x[:2])
                print(cost)

                print("{} -> {}".format(left, y))
                add_link(left, y, cost=cost)


links = {}


def add_link(src, dst, cost=None):
    if src not in links:
        links[src] = []
    if dst not in links:
        links[dst] = []

    if dst not in links[src]:
        if cost:
            links[src].append((cost, dst))
        else:
            links[src].append(dst)


def with_example():
    i = 0
    bags = {}
    for l in input.splitlines():
        l = l.replace("bags", "").replace("bag", "")
        a = l.replace("contain", ":").split(":")
        left = a[0].strip()
        right = a[1]
        right = right.replace(".", "").strip()
        right = right.split(",")
        newright = []
        for n in right:
            newright.append(n.strip())
        right = newright
        print(i, "{} => {}".format(left, right))
        i += 1
        for x in right:
            y = x[2:].strip()
            if "other" in y:
                continue
            print("{} -> {}".format(y, left))
            add_link(y, left)
            G.add_node(y)
            G.add_node(left)
            G.add_edge(left, y)


def with_example2():
    i = 0
    bags = {}
    for l in input.splitlines():
        l = l.replace("bags", "").replace("bag", "")
        a = l.replace("contain", ":").split(":")
        left = a[0].strip()
        right = a[1]
        right = right.replace(".", "").strip()
        right = right.split(",")
        newright = []
        for n in right:
            newright.append(n.strip())
        right = newright
        print(i, "{} => {}".format(left, right))
        i += 1
        for x in right:
            y = x[2:].strip()
            if "other" in y:
                continue
            cost = int(x[:2])
            print(cost)

            print("{} -> {}".format(left, y))
            add_link(left, y, cost=cost)


with_input2()
# with_example2()
pprint(links)


def find_path(loc):
    print(loc)
    if loc not in links:
        return "1"
    if len(links[loc]) == 0:
        return "1"
    lisp = "(+ "
    for n in links[loc]:
        print("{} of {}".format(n[0], n[1]))
        lisp += "(* {} {}) ".format(n[0], find_path(n[1]))
    lisp += " 1 )"
    return lisp


res = find_path("shiny gold")
print("(- {} 1)".format(res))
res = list(dict.fromkeys(res[1:]))

print(len(res))


exit()
from networkx.drawing.nx_pydot import write_dot

pos = nx.nx_agraph.graphviz_layout(G)

nx.draw(G, pos=pos)

write_dot(G, "file.dot")
exit()


pprint(bags)


def recurse(current):
    state = []
    for n in bags[current]:
        state.append(n)
        if n in bags:
            state.append(recurse(n))
    return state


for start in bags:
    paths = recurse(start)
    print(paths)
