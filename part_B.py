import random

import numpy as np
from matplotlib import pyplot as plt

import math
import numpy as np
from electron import Electron


R = 1
N = 200
# s
T = 10 ** -3
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
                e1.update_acceleration(e1.a_x + K * (e1.x - e2.x)/d * Q ** 2 / d**2 / M,
                                       e1.a_y + K * (e1.y - e2.y)/d * Q ** 2 / d**2 / M,
                                       e1.a_z + K * (e1.z - e2.z)/d * Q ** 2 / d**2 / M)


def simulate_B():
    count = 0
    locations = []
    electrons = []
    for i in range(N):
        e = generate_electron()
        electrons.append(e)
    temp = []
    for e in electrons:
        temp.append([e.x, e.y, e.z])
    locations.append(temp)
    for i in range(LENGTH):
        update_field(electrons)
        for e in electrons:
            e.update_location(T)
            if not is_in(e):
                count += 1
                e.return_to_sphere(R)
            e.reset_velocity()
            e.reset_acceleration()
        temp = []
        for e in electrons:
            temp.append([e.x, e.y, e.z])
        locations.append(temp)
        # print("iteration: " + str(i))
    print(count)
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


def generate_electron():
    x = np.random.uniform(-R, R)
    y = np.random.uniform(-R, R)
    z = np.random.uniform(-R, R)
    electron = Electron(x, y, z)
    while not is_in(electron):
        x = np.random.uniform(-R, R)
        y = np.random.uniform(-R, R)
        z = np.random.uniform(-R, R)
        electron.x = x
        electron.y = y
        electron.z = z
    return electron




def draw_b(result):
    ax = plt.axes(projection='3d')
    outside_e = []
    inside_e = []
    for e in result:
        if (e[0]**2 + e[1]**2 + e[2]**2)**0.5 >= R:
            outside_e.append(e)
        elif e != result[N-1]:
            inside_e.append(e)
    if outside_e:
        ax.scatter3D(list(zip(*outside_e))[0], list(zip(*outside_e))[1], list(zip(*outside_e))[2], color='green')
    if inside_e:
        ax.scatter3D(list(zip(*inside_e))[0], list(zip(*inside_e))[1], list(zip(*inside_e))[2], color='red')
    ax.scatter3D(result[N-1][0], result[N-1][1], result[N-1][2], color='cyan')

    u, v = np.mgrid[0:2 * np.pi:10j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v) * R
    y = np.sin(u) * np.sin(v) * R
    z = np.cos(v) * R
    ax.plot_wireframe(x, y, z, color="orange")

    plt.show()

