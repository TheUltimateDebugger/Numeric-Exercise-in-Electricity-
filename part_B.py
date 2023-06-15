import random

import numpy as np
from matplotlib import pyplot as plt

import math
import numpy as np
from electron import Electron


R = 1
N = 200
# s
T = 10 ** -15
# T times
LENGTH = 100
# colon
Q = -1.602176634 * 10 ** (-19)
# Kg
M = 9.10938356 * 10 ** (-31)
# Coulomb's const
K = 8.988 * 10 ** 9


def update_field(electrons):
    for e1 in electrons:
        for e2 in electrons:
            if e1 != e2 and e1.dist(e2) > 0:
                d = e1.dist(e2)
                e1.update_acceleration(K * (e1.x - e2.x) * Q ** 2 / d / M, K * (e1.y - e2.y) * Q ** 2 / d / M,
                                       K * (e1.z - e2.z) * Q ** 2 / d / M)


def fix_locations(electrons):
    for e in electrons:
        if electron_is_outside(e):
            e.return_to_sphere()


def simulate_B():
    locations = []
    electrons = []
    for i in range(N):
        e = Electron()
        electrons.append(e)
    for i in range(LENGTH):
        update_field(electrons)
        for e in electrons:
            e.update_location(T)
            e.reset_velocity()
        temp = []
        for e in electrons:
            temp.append((e.x, e.y, e.z))
        locations.append(temp)
    return locations


def is_in(electron):
    """
    :param electron: tuple of the location
    :return: true if in else false
    """
    radius = electron.dist_from_zero()
    if radius <= R:
        return True
    else:
        return False


def generate_sphire():
    x = np.random.uniform(-R, R)
    y = np.random.uniform(-R, R)
    z = np.random.uniform(-R, R)
    electron = Electron(x, y, z)
    while not is_in(electron):
        x = np.random.uniform(-R, R)
        y = np.random.uniform(-R, R)
        z = np.random.uniform(-R, R)
        electron = Electron(x, y, z)
    return electron






def draw_b(result):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(list(zip(*result))[0], list(zip(*result))[1], list(zip(*result))[2], cmap='Greens')
    u, v = np.mgrid[0:2 * np.pi:25j, 0:np.pi:25j]
    x = np.cos(u) * np.sin(v) * R
    y = np.sin(u) * np.sin(v) * R
    z = np.cos(v) * R
    ax.plot_wireframe(x, y, z, color="orange")

    plt.show()
