import numpy as np
import math
import random
import time

np.set_printoptions(threshold=np.inf)

# 问题规模定义
k, v = 4, 3  # k个参数,每个有v个候选值

# PSO定义
particles_size = 50  # 50个粒子
weight = 0.729  # 惯性权重
C = (1.49, 1.49)  # 学习因子
max_itera = 150  # 迭代次数
V_threshold = (-0.5, 1)  # 速度阈值

# pairwise testing内容定义
final_test_case = 15  # 最后要几条测试数据
rows = particles_size  # 行数 = 粒子数,即为粒子的种群集合
cols = final_test_case * k  # 列数 = 每一个粒子的所有测试参数集合 = 测试数据条数 * 每个测试条所含有的变量数

# 创建二维数组用于储存粒子数据
all_particles_in_pop = [[0 for col in range(cols)] for row in range(rows)]

# 初始化速度数组 每一个粒子具有一个速度参数,有多少个粒子,表示速度的数组就有多长
velocity = [np.random.random() for i in range(0, particles_size, 1)]

# 初始化pbest数组,行数等于粒子数,列数等于所有的位置数
pbest = [[0 for col in range(cols)] for row in range(rows)]  # 注意,最后的pbest在最开始计算时就是初始化的二维数组

# 初始化适应度数组,其个数等于粒子的个数,每一个粒子自身都需要一个适应度,用当前算出的适应度值去跟当前粒子的适应度去比较,二维数组,第一行记录当前的适应度,第二行记录上一次的适应度
fitnessvalue = [[0 for col in range(particles_size)] for row in range(2)]

# 初始化gbest,gbest是pbest里最好的一个  记录当前一个粒子的所有测试用例参数
gbest = [0 for col in range(cols)]
