#!/usr/bin/env python3
from pprint import pprint
import numbers


input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
"""

r1 = {}
with open("rules", "r") as fp:
    for l in fp:
        a = l.split(":")
        r1[int(a[0])] = a[1].strip().split(" ")
        n = []
        for x in r1[int(a[0])]:
            try:
                t = int(x)
                n.append(t)
                continue
            except Exception as e:
                if x == "|":
                    n.append(x)
                elif x == '"a"':
                    n.append("a")
                elif x == '"b"':
                    n.append("b")
                else:
                    print("Error!")
            r1[int(a[0])] = n


def req(rules, num):
    v = rules[num]
    s = ""
    #    if num != 0:
    s = "("
    for n in v:
        print("{}".format(type(n)))
        try:
            x = int(n)
            s += req(rules, x)
        except Exception as e:
            print("{} is not an int".format(n))
            s += n
    #    if num != 0:
    s += ")"
    return s
    print("req: {}".format(s))


reg = req(r1, 0)
# reg = reg.replace("(a)", "a").replace("(b)", "b")
import re

print("asdf: {}".format(reg))
m = re.compile(reg)


lines = """ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

with open("ex", "r") as fp:
    for line in fp:
        if m.fullmatch(line):
            print("{} Matches".format(line))
        else:
            print("NO MATCH {}".format(line))
