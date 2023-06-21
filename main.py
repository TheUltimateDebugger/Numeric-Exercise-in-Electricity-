from part_A import simulate, draw_graph, T
from part_B import simulate_B, draw_b, LENGTH_B
from part_C import simulate_C, draw_c, LENGTH_C
from part_D import simulate_D, draw_D, LENGTH_D


def get_avg_dist(n):
    sum = 0
    for i in range(n):
        temp = simulate()
        sum += temp[len(temp)-1][0]
    print(str(sum/n / T))


if __name__ == '__main__':
    # locations = simulate()
    # print(str(locations[len(locations) - 1][0]/T))
    # draw_graph(locations)

    # locations2 = simulate_B()
    # draw_b(locations2[LENGTH_B])
    #
    # locations3 = simulate_C()
    # draw_c(locations3[LENGTH_C])

    locations4 = simulate_D()
    draw_D(locations4[LENGTH_D])




