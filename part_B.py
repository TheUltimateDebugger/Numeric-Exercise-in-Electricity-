import random

import numpy as np
from matplotlib import pyplot as plt

import math
import numpy as np
from electron import Electron, update_field

R = 1
N = 200
# s
T = 10 ** -3
# T times
LENGTH_B = 500


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
    for i in range(LENGTH_B):
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
        if (e[0] ** 2 + e[1] ** 2 + e[2] ** 2) ** 0.5 >= R * 0.99:
            outside_e.append(e)
        else:
            inside_e.append(e)
    if outside_e:
        ax.scatter3D(list(zip(*outside_e))[0], list(zip(*outside_e))[1], list(zip(*outside_e))[2], color='green')
    if inside_e:
        ax.scatter3D(list(zip(*inside_e))[0], list(zip(*inside_e))[1], list(zip(*inside_e))[2], color='red')

    u, v = np.mgrid[0:2 * np.pi:10j, 0:np.pi:10j]
    x = np.cos(u) * np.sin(v) * R
    y = np.sin(u) * np.sin(v) * R
    z = np.cos(v) * R
    ax.plot_wireframe(x, y, z, color="orange")

    plt.show()
