from part_A import simulate, draw_graph, T
from part_B import simulate_B, draw_b


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
    draw_b(locations2)
    for l in locations2:
        print(str(l[0]) + ", " + str(l[1]) + ", " + str(l[2]))

