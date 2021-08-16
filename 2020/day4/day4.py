#!/usr/bin/env python3


def validate_pass(pa):
    d = {}
    l = sorted(pa.split(" "))
    del l[0]
    for n in l:
        k = n.split(":")
        d[k[0]] = k[1]

    a = set(d.keys())
    b = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    missing = list(b.difference(a))

    if len(missing) > 0:
        return False

    return True


valid = 0
invalid = 0
with open("input", "r") as fp:
    passport = ""
    for line in fp:
        if len(line) == 1:
            if validate_pass(passport):
                valid += 1
            else:
                invalid += 1
            passport = ""
            continue
        passport += line.strip() + " "

    if len(passport) > 0:
        if validate_pass(passport):
            valid += 1
        else:
            invalid += 1

print("Number of valid passports {}, invalid {}".format(valid, invalid))
