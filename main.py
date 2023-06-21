from electron import K, Q
from part_A import simulate_A, draw_A, T
from part_B import simulate_B, draw_B, LENGTH_B, draw_potential_for_radius
from part_C import simulate_C, draw_C, LENGTH_C, draw_density_for_radius
from part_D import simulate_D, draw_D, LENGTH_D


def get_avg_dist(n):
    sum = 0
    for i in range(n):
        temp = simulate_A()
        sum += temp[len(temp)-1][0]
    print(str(sum/n / T))


if __name__ == '__main__':
    # locations1 = simulate_A()
    # print(str(locations1[len(locations1) - 1][0]/T))
    # draw_A(locations1)
    #
    # locations2 = simulate_B()
    # draw_potential_for_radius(locations2[LENGTH_B])
    # draw_B(locations2[0])
    # draw_B(locations2[LENGTH_B])
    #
    locations3 = simulate_C()
    draw_C(locations3[0])
    draw_density_for_radius(locations3[0])
    draw_C(locations3[LENGTH_C])
    draw_density_for_radius(locations3[LENGTH_C])
    locations4 = simulate_D()
    draw_D(locations4[0])
    draw_D(locations4[LENGTH_D//4])
    draw_D(locations4[2*LENGTH_D//4])
    draw_D(locations4[3*LENGTH_D//4])
    draw_D(locations4[LENGTH_D])




