#!/usr/bin/env python3

sum = 0
numbers = {"one":1, "two":2, "three":3, "four":4, "five":5,
        "six":6, "seven":7, "eight":8, "nine":9}


# with open("test2.txt") as f:
with open("input.txt") as f:
    for l in f:
        f1 = False
        l = l[:-1]
        v = 0
        for i in range(len(l)):
            for n in numbers:
                if l[i:i+len(n)] == n:
                    v = numbers[n]
                elif '0' <= l[i] <= '9':
                    v = int(l[i])
                if not f1 and v:
                    v1 = v
                    f1 = True
        sum += v1 * 10 + v
print(sum)
