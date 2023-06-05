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
K = 8.988*10**9


def update_field(electrons):
    for e1 in electrons:
        for e2 in electrons:
            if e1 != e2:
                d = e1.dist(e2)
                e1.update_acceleration(K*(e1.x-e2.x)*Q**2/d/M, K*(e1.y-e2.y)*Q**2/d/M, K*(e1.z-e2.z)*Q**2/d/M)

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
        temp = []
        for e in electrons:
            temp.append((e.x, e.y, e.z))
        locations.append(temp)
    return locations

