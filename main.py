from electron import K, Q
from part_A import simulate_a, draw_a, T
from part_B import simulate_b, draw_b, LENGTH_B, draw_potential_for_radius
from part_C import simulate_c, draw_c, LENGTH_C, draw_density_for_radius
from part_D import simulate_d, draw_d, LENGTH_D

if __name__ == '__main__':
    locations1 = simulate_a()
    print("the speed is:" + str(locations1[len(locations1) - 1][0]/T))
    draw_a(locations1)

    locations2 = simulate_b()
    draw_potential_for_radius(locations2[LENGTH_B])
    draw_b(locations2[LENGTH_B])
    locations3 = simulate_c()
    draw_c(locations3[LENGTH_C])
    draw_density_for_radius(locations3[LENGTH_C])
    locations4 = simulate_d()
    draw_d(locations4[LENGTH_D])




