#!/usr/bin/env python3
import re

def main():
    sum = 0
    # with open("test.txt") as f:
    with open("input.txt") as f:
        for i, l in enumerate(f):
            ok = True
            l = l[:-1].split(":")[1]
            ll = l.split(";")
            maxr = maxg = maxb = 0
            for m in ll:
                rr = gg = bb = 0
                for n in m.split(","):
                    if "red" in n:
                        rr = int(n.strip().split(" ")[0])
                        if rr > maxr:
                            maxr = rr
                    if "green" in n:
                        gg = int(n.strip().split(" ")[0])
                        if gg > maxg:
                            maxg = gg
                    if "blue" in n:
                        bb = int(n.strip().split(" ")[0])
                        if bb > maxb:
                            maxb = bb
            power = maxr * maxg * maxb
            sum += power
    print(sum)

if __name__ == '__main__':
    main()

