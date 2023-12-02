#!/usr/bin/env python3
import re

def main():
    maxr = 12
    maxg = 13
    maxb = 14
    sum = 0
    # with open("test.txt") as f:
    with open("input.txt") as f:
        for i, l in enumerate(f):
            ok = True
            l = l[:-1].split(":")[1]
            ll = l.split(";")
            print(ll)
            for m in ll:
                rr = gg = bb = 0
                for n in m.split(","):
                    if "red" in n:
                        rr = int(n.strip().split(" ")[0])
                        if rr > maxr:
                            ok = False
                    if "green" in n:
                        gg = int(n.strip().split(" ")[0])
                        if gg > maxg:
                            ok = False
                    if "blue" in n:
                        bb = int(n.strip().split(" ")[0])
                        if bb > maxb:
                            ok = False
                print(rr, gg, bb, ok)
            if ok:
                sum += i + 1
    print(sum)

if __name__ == '__main__':
    main()

