from matplotlib import pyplot as plt
import numpy as np
from electron import Electron

# radius of square M
R = 1
# number of electrons
N = 200
# s
T = 10 ** -3
# T times
LENGTH_D = 500

# how much we move the corner counter
MOV = 1.1
# how much we zoom out of the graph
LIM = 2


def simulate_d():
    locations = []
    electrons = []
    for i in range(N):
        e = generate_electron_in_square()
        electrons.append(e)
    temp = []
    for e in electrons:
        temp.append([e.x, e.y, e.z])
    locations.append(temp)
    for i in range(LENGTH_D):
        for e in electrons:
            e.update_field(electrons)
            e.update_location(T)
            e.keep_in_square(R)
            e.reset_velocity()
            e.reset_acceleration()
        temp = []
        for e in electrons:
            temp.append([e.x, e.y, e.z])
        locations.append(temp)
        # print("iteration: " + str(i))
    return locations


def is_in_square(electron):
    """
    :param electron: tuple of the location
    :return: true if in else false
    """
    radius = electron.dist_from_zero()
    if radius <= R:
        return True
    else:
        return False


def generate_electron_in_square():
    x = np.random.uniform(-R, R)
    y = np.random.uniform(-R, R)
    z = 0
    electron = Electron(x, y, z)
    return electron


def is_on_square(x, y, z, r):
    return abs(x) == r or abs(y) == r or abs(z) == r


def draw_d(result):
    plt.figure(4)
    plt.plot([R, R], [-R, R], color='orange')
    plt.plot([-R, -R], [-R, R], color='orange')
    plt.plot([-R, R], [-R, -R], color='orange')
    plt.plot([-R, R], [R, R], color='orange')
    outside_e = []
    inside_e = []
    corners = [0] * 4
    for e in result:
        if is_on_square(e[0], e[1], e[2], R):
            outside_e.append(e)
            if e[0] == R and e[1] == R:
                corners[0] += 1
            if e[0] == -R and e[1] == R:
                corners[1] += 1
            if e[0] == -R and e[1] == -R:
                corners[2] += 1
            if e[0] == R and e[1] == -R:
                corners[3] += 1
        else:
            inside_e.append(e)
    if outside_e:
        plt.scatter(list(zip(*outside_e))[0], list(zip(*outside_e))[1], color='green')
        print(outside_e)
    if inside_e:
        plt.scatter(list(zip(*inside_e))[0], list(zip(*inside_e))[1], color='red')
    plt.title("Electrons Inside a Conducting Square")
    plt.xlabel("X[m]")
    plt.ylabel("Y[m]")
    plt.axis([-LIM, LIM, -LIM, LIM])
    plt.text(MOV * R, 0, "Electrons in (1, 1): " + str(corners[0]) + "\nElectrons in (-1, 1): " + str(
        corners[1]) + "\nElectrons in (-1, -1): " + str(corners[2]) +
             "\nElectrons in (1, -1): " + str(corners[3]), color='blue', bbox=dict(facecolor='red', alpha=0.5))
    plt.show()
