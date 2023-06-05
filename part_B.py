from electron import Electron

R = 1
N = 200
T = 10**-3

def simulate_B():
    electrons = []
    for i in range(N):
        e = Electron()
