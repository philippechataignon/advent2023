#!/usr/bin/env python3

sum = 0
# with open("test.txt") as f:
with open("input.txt") as f:
    for l in f:
        f1 = False
        l = l[:-1]
        for c in l:
            if not f1 and '0' <= c <= '9':
                v1 = int(c)
                f1 = True
            if '0' <= c <= '9':
                v2 = int(c)
        print(v1 * 10 + v2)
        sum += v1 * 10 + v2
print(sum)
