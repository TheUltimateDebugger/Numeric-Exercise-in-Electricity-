# V/M
import math
import random

from matplotlib import pyplot as plt

from electron import Electron

E0 = 30
# m/s
V0 = 0.002
# s
T = 10 ** -15
# T times
LENGTH = 100
# colon
Q = -1.602176634 * 10 ** (-19)
# Kg
M = 9.10938356 * 10 ** (-31)


def simulate():
    result = [(0, 0, 0)]
    e = Electron(0, 0, 0, 0, 0, 0, (E0 * Q) / M)
    for i in range(LENGTH):
        print (e.location())
        e.update_location(T)
        theta = random.uniform(0, 2 * math.pi)
        e.coalition(math.cos(theta) * V0, math.sin(theta) * V0, 0)
        result.append(e.location())
    print(result[LENGTH-1][0])
    return result

def draw_graph(result):
    graph = plt.subplot()
    graph.scatter(list(zip(*result))[0], list(zip(*result))[1])
    graph.scatter(result[0][0], result[0][1], color="red")
    graph.scatter(result[len(result)-1][0], result[len(result)-1][1], color="red")
    for i in range(len(result)-1):
        graph.plot([result[i][0], result[i+1][0]], [result[i][1], result[i+1][1]], color="green", linestyle="--")
    plt.show()