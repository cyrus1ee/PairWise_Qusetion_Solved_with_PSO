from initial_paramters import *


# 初始化种群二维数组
def init_pop(arrays):
    for i in range(0, rows, 1):  # 从第一个开始,一行一行往下走
        for j in range(0, cols, 1):  # 从第一列开始,每隔k个进行一次约束
            temp = j % k  # j从0开始,顺序数组也从1开始
            arrays[i][j] = random.randint(temp * v, (
                    (temp + 1) * v - 1))  # 给数组中的每一个元素赋值,每60个参数代表一个粒子,其中这60个参数为该粒子的位置,每次赋值的范围在(0~此处为12)
            # np.random.randint()方法的取值区间是前闭后开区间
    return arrays


# 更新速度
def update_velocity(arrays):
    for i in range(0, particles_size, 1):  # i 是每一个粒子,j 是每一个粒子的参数
        for j in range(cols):
            minus_of_pbest = pbest[i][j] - arrays[i][j]
            minus_of_gbest = gbest[j] - arrays[i][j]

        velocity[i] = velocity[i] * weight + C[0] * np.random.rand() * minus_of_pbest + C[
            1] * np.random.rand() * minus_of_gbest
        velocity[i] = V_threshold[0] if velocity[i] < V_threshold[0] else velocity[i]
        velocity[i] = V_threshold[1] if velocity[i] > V_threshold[0] else velocity[i]


# 更新位置
def update_location(arrays, velocity_arrays):
    for i in range(0, particles_size, 1):
        for j in range(0, cols, 1):  # 对每一个值都进行替换
            arrays[i][j] = arrays[i][j] + velocity_arrays[i]
            arrays[i][j] = position_threshold(arrays[i][j], j)


# 判断当前位置是否不满足约束条件,不满足则处理当前位置的上下限约束  这里可能有问题
def position_threshold(param, m):  # param 是当前位置的数值, m是当前的列
    tempt = m % k
    if (tempt * v) <= param < ((tempt + 1) * v):
        param = math.floor(param)
        return param
    else:
        param = random.randint(tempt * v, ((tempt + 1) * v - 1))
        return param


# 更新pbest 根据适应度值来确定pbest 其中fitness是适应度数组,n是当前是哪一个粒子
def update_pbest(fitness, n, pebst):
    if fitness[0][n] > fitness[1][n]:  # 第0行是当前的适应度, 第1行上次的适应度   如果当前的比上次的pbest大
        fitness[1][n] = fitness[0][n]  # 当前的变成上一次的,等待下一次适应度计算
        pebst[n] = all_particles_in_pop[n]  # 当前的pbest中的位置就等于当前粒子的位置
