from matplotlib import pyplot as plt, patches

import math
import numpy as np
from electron import Electron, update_field, Q, electrons_in_ring

# radius of circle M
R = 1
# number of electrons
N = 200
# s
T = 10 ** -3
# T times
LENGTH_C = 500


def simulate_c():
    locations = []
    electrons = []
    for i in range(N):
        e = generate_electron_in_circle()
        electrons.append(e)
    temp = []
    for e in electrons:
        temp.append([e.x, e.y, e.z])
    locations.append(temp)
    for i in range(LENGTH_C):
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
        # print("iteration: " + str(i))
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


def generate_electron_in_circle():
    x = np.random.uniform(-R, R)
    y = np.random.uniform(-R, R)
    z = 0
    electron = Electron(x, y, z)
    while not is_in(electron):
        x = np.random.uniform(-R, R)
        y = np.random.uniform(-R, R)
        z = 0
        electron.x = x
        electron.y = y
        electron.z = z
    return electron


def draw_density_for_radius(locations):
    radii = np.arange(0, R+R/8, R/8)
    radii2 = np.arange(0, R, R/100)
    function = (Q*N)/(2*math.pi*R)/(R**2-radii2**2)**0.5
    density = []
    x_axis = []
    for i in range(8):
        density.append(Q * electrons_in_ring(locations, radii[i], radii[i+1]) /
                       (math.pi * radii[i+1]**2 - math.pi * radii[i]**2))
        x_axis.append((radii[i] + radii[i+1])/2)
    plt.scatter(x_axis, density)
    plt.title("Density of Charge in Relation to the Radius")
    plt.xlabel("Radius[m]")
    plt.ylabel("Charge Density[c/m^2]")
    plt.plot(radii2, function, color='green')
    plt.show()


def draw_c(result):
    plt.figure(3)
    ax = plt.subplot()
    circle1 = patches.Circle((0, 0), radius=R, color='orange', fill=False)
    ax.add_patch(circle1)
    outside_e = []
    inside_e = []
    for e in result:
        if (e[0] ** 2 + e[1] ** 2 + e[2] ** 2) ** 0.5 >= R * 0.999:
            outside_e.append(e)
        else:
            inside_e.append(e)
    if outside_e:
        plt.scatter(list(zip(*outside_e))[0], list(zip(*outside_e))[1], color='green')
    if inside_e:
        plt.scatter(list(zip(*inside_e))[0], list(zip(*inside_e))[1], color='red')
    plt.title("Electrons Inside a Conducting Disk")
    plt.xlabel("X[m]")
    plt.ylabel("Y[m]")
    plt.show()
