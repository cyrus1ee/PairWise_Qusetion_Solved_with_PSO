from paramater_initial import *


# 初始化每一个pairwise，并计算适应度。计算适应度的方法：每一个当前被选中的粒子与二维数组中的位置进行匹配
def caculatefintess(particle, count):
    i = 0
    for p1 in range(0, k):
        for p2 in range(p1 + 1, k):
            pairwise[i] = particle[p1]
            pairwise[i + 1] = particle[p2]
            if all_cover[pairwise[i]][pairwise[i + 1]]:  # 只把最大的一个标0,剩下的先不标
                fitness[0][count] += 1


# 计算完之后对全覆盖测试矩阵进行更改
def change_matrix(particle):
    i = 0
    for p1 in range(0, k):
        for p2 in range(p1 + 1, k):
            pairwise[i] = particle[p1]
            pairwise[i + 1] = particle[p2]
            if all_cover[pairwise[i]][pairwise[i + 1]]:  # 只把最大的一个标0,剩下的先不标
                all_cover[pairwise[i]][pairwise[i + 1]] = False


# 将适应度数组的第一行置0
def reset_fitness_array(array):
    for j in range(particles_size):
        array[0][j] = 0
