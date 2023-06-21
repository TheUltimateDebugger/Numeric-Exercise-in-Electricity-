import random

import numpy as np
from matplotlib import pyplot as plt

import math
import numpy as np
from matplotlib.pyplot import show

from electron import Electron, update_field, potential_at_point

R = 1
N = 200
# s
T = 10 ** -3
# T times
LENGTH_B = 5000
PROXIMITY = 0.9999


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
    how_many_on_the_sphere = []
    for i in range(LENGTH_B):
        update_field(electrons)
        for e in electrons:
            e.update_location(T)
            if not is_in(e):
                e.return_to_sphere(R)
            e.reset_velocity()
            e.reset_acceleration()
        temp = []
        for e in electrons:
            temp.append([e.x, e.y, e.z])
        locations.append(temp)
        how_many_on_the_sphere.append(count_in_the_sphere(temp))
        # print("iteration: " + str(i))
    draw_graph_of_density(how_many_on_the_sphere)
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


def is_on_the_sphere(e_location):
    if (e_location[0] ** 2 + e_location[1] ** 2 + e_location[2] ** 2) ** 0.5 >= R * PROXIMITY:
        return True
    else:
        return False


def draw_graph_of_density(how_many_not_on_sphere):
    count = 1
    temp1 = []
    temp2 = []
    for iteration in how_many_not_on_sphere:
        temp1.append(iteration)
        count += 1
        temp2.append(count)
    plt.xlabel('Time[10^-3s]')
    plt.ylabel('Proportion')
    plt.title('The Proportion of the Electrons Inside the Sphere'
              ' Depending on the Time')
    plt.plot(temp2, temp1)
    plt.show()


def count_in_the_sphere(result):
    count = 0
    for e in result:
        if not is_on_the_sphere(e):
            count += 1
    return count / N


def draw_potential_for_radius(locations):
    radii = np.arange(0, 10*R, 0.05)
    num_of_electrons = []
    for r in radii:
        num_of_electrons.append(potential_at_point([r, 0, 0], locations))
    plt.scatter(radii, num_of_electrons)
    plt.title("Potential in Relation to Radius")
    plt.xlabel("Radius[m]")
    plt.ylabel("Electric Potential[Volt]")
    plt.show()


def draw_B(result):
    ax = plt.axes(projection='3d')
    outside_e = []
    inside_e = []
    for e in result:
        if is_on_the_sphere(e):
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
    ax.set_xlabel("X[m]", fontsize=12)
    ax.set_ylabel("Y[m]", fontsize=12)
    ax.set_zlabel("Z[m]", fontsize=12)
    plt.title("Electrons Inside a Sphere")
    plt.show()
