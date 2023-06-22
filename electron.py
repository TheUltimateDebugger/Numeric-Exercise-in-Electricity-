# colon
Q = -1.602176634 * 10 ** (-19)
# Kg
M = 9.10938356 * 10 ** (-31)
# Coulomb's const
K = 8.988 * 10 ** 9


class Electron:
    def __init__(self, x=0, y=0, z=0, v_x=0, v_y=0, v_z=0, a_x=0, a_y=0, a_z=0):
        self.x = x
        self.y = y
        self.z = z
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        self.a_x = a_x
        self.a_y = a_y
        self.a_z = a_z

    def dist_from_zero(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

    def coalition(self, v_x=0, v_y=0, v_z=0):
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

    def location(self):
        return self.x, self.y, self.z

    def update_acceleration(self, ax, ay, az):
        self.a_x = ax
        self.a_y = ay
        self.a_z = az

    def update_velocity(self, vx, vy, vz):
        self.v_x = vx
        self.v_y = vy
        self.v_z = vz

    def reset_velocity(self):
        self.update_velocity(0, 0, 0)

    def reset_acceleration(self):
        self.update_acceleration(0, 0, 0)

    def return_to_sphere(self, r):
        d = self.dist_from_zero()
        self.x *= r / d
        self.y *= r / d
        self.z *= r / d

    def is_outside_square(self, r):
        return abs(self.x) >= r or abs(self.y) >= r or abs(self.z) >= r

    def keep_in_square(self, r):
        if abs(self.x) >= r:
            self.x = self.x / abs(self.x) * r
        if abs(self.y) >= r:
            self.y = self.y / abs(self.y) * r
        if abs(self.z) >= r:
            self.z = self.z / abs(self.z) * r

    def is_on_square(self, r):
        return abs(self.x) == r or abs(self.y) == r or abs(self.z) == r

    def update_location(self, t):
        self.x = self.x + self.v_x * t + 0.5 * self.a_x * t ** 2
        self.y = self.y + self.v_y * t + 0.5 * self.a_y * t ** 2
        self.z = self.z + self.v_z * t + 0.5 * self.a_z * t ** 2
        self.v_x = self.v_x + self.a_x * t
        self.v_y = self.v_y + self.a_y * t
        self.v_z = self.v_z + self.a_z * t

    def update_field(self, electrons):
        for e2 in electrons:
            if self != e2:
                d = self.dist(e2)
                self.update_acceleration(self.a_x + K * (self.x - e2.x) / d * Q ** 2 / d ** 2 / M,
                                         self.a_y + K * (self.y - e2.y) / d * Q ** 2 / d ** 2 / M,
                                         self.a_z + K * (self.z - e2.z) / d * Q ** 2 / d ** 2 / M)


def potential_at_point(point, electrons):
    result = 0
    for e in electrons:
        result += Q * K / (((point[0] - e[0]) ** 2 + (point[1] - e[1]) ** 2 + (point[2] - e[2]) ** 2) ** 0.5)
    return result


def dist(e):
    return (e[0] ** 2 + e[1] ** 2 + e[2] ** 2) ** 0.5


def electrons_in_radius(locations, r):
    count = 0
    for e in locations:
        if dist(e) <= r:
            count += 1
    return count


def electrons_in_ring(locations, r1, r2):
    count = 0
    for e in locations:
        if r1 <= dist(e) <= r2:
            count += 1
    return count


def update_field(electrons):
    for e1 in electrons:
        for e2 in electrons:
            if e1 != e2:
                d = e1.dist(e2)
                e1.update_acceleration(e1.a_x + K * (e1.x - e2.x) / d * Q ** 2 / d ** 2 / M,
                                       e1.a_y + K * (e1.y - e2.y) / d * Q ** 2 / d ** 2 / M,
                                       e1.a_z + K * (e1.z - e2.z) / d * Q ** 2 / d ** 2 / M)


def update_field_square_not_crush(electrons):
    for e1 in electrons:
        for e2 in electrons:
            if e1 != e2 and e1.dist(e2) > 0:
                d = e1.dist(e2)
                e1.update_acceleration(e1.a_x + K * (e1.x - e2.x) / d * Q ** 2 / d ** 2 / M,
                                       e1.a_y + K * (e1.y - e2.y) / d * Q ** 2 / d ** 2 / M,
                                       e1.a_z + K * (e1.z - e2.z) / d * Q ** 2 / d ** 2 / M)
