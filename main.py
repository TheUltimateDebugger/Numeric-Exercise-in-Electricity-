from part_A import simulate_A, draw_A, T
from part_B import simulate_B, draw_B, LENGTH_B
from part_C import simulate_C, draw_c, LENGTH_C
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

    locations2 = simulate_B()
    draw_B(locations2[0])
    draw_B(locations2[LENGTH_B])
    #
    # locations3 = simulate_C()
    # draw_c(locations3[LENGTH_C])

    locations4 = simulate_D()
    draw_D(locations4[LENGTH_D])




