from part_A import simulate, draw_graph, T
from part_B import simulate_B, draw_b, LENGTH


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

    locations2 = simulate_B()
    # for t in locations2:
    #     for e in t:
    #         print(str(e[0]) + ", " + str(e[1]) + ", " + str(e[2]))
    #     print("-------------------------")
    draw_b(locations2[0])
    draw_b(locations2[LENGTH])


