from part_A import simulate, draw_graph, T
from part_B import simulate_B, draw_b, LENGTH_B
from part_C import simulate_C, draw_c, LENGTH_C


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

    locations2 = simulate_C()
    # for t in locations2:
    #     for e in t:
    #         print(str(e[0]) + ", " + str(e[1]) + ", " + str(e[2]))
    #     print("-------------------------")
    draw_c(locations2[LENGTH_C])
    locations3 = simulate_B()
    draw_b(locations3[LENGTH_B])


