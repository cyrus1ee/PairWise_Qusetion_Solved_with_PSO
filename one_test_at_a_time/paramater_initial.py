import numpy as np
import math
import random

# 问题规模定义
k, v = 4, 3

# PSO定义
particles_size = 50  # 粒子个数50个
weight = 0.729  # 惯性权重
C = (1.49, 1.49)  # 学习因子
max_itera = 150  # 迭代次数
V_threshold = (-0.5, 1)  # 速度阈值

# particle_matrix 内容定义
cols = k
rows = particles_size  # 行数 = 粒子数,即为粒子的种群集合

# 先初始化粒子的二维种群,其大小为  粒子个数*k
all_particles_in_pop = np.zeros((particles_size, cols), dtype=int)

# 初始化pbest数组,行数等于粒子数,列数等于所有的位置数
pbest = [[0 for col in range(cols)] for row in range(rows)]  # 注意,最后的pbest在最开始计算时就是初始化的二维数组

# 初始化gbest,gbest是pbest里最好的一个  记录当前一个粒子的所有测试用例参数
gbest = [0 for col in range(cols)]

# 初始化pairwise列表
pairwise = [0 for col in range(2)]  # 4个k,里面有6组,每组成对2个,就是2*6=12个{[1+(k-1)](k-1)/2}*2个,这是一个粒子组内的数据

# 初始化适应度数组大小是  2行 particle_size 列
fitness = [[0 for col in range(particles_size)] for row in range(2)]

# 定义速度数组
velocity = [np.random.random() for i in range(0, particles_size, 1)]

# 初始化最终测试用例数组
final_test_array = [0 for row in range(0)]

# 定义一个数组来计算每一次输出的适应度
output_fitness = [0 for row in range(0)]

# 初始化全覆盖测试矩阵
all_cover = np.zeros((k * v, k * v), dtype=int)
for m in range(0, v):  # 有几组
    for i in range(m * v, (m + 1) * v):  # 每组开始的行和结束的行
        for j in range((m + 1) * v, k * v):  # 每一列开始的列和结束的列
            all_cover[i][j] = 1
