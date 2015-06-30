#!/usr/bin/python

from matplotlib import pyplot as plt


def show(filename):
    data = [tuple(map(int, x.split())) for x in file(filename).readlines()[1:]]
    times = []
    for c in data:
        if len(c) >= 2:
            times.append(c[1])
    plt.hist(times, bins=1000)
    #plt.plot(sorted(times))
    plt.show()


show("times_512_min.txt")
