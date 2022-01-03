from PSO_part import *
from CaculateFitness import *

t0 = time.time()

init_pop(all_particles_in_pop)  # 初始化种群

for i in range(max_itera):

    for j in range(particles_size):  # 速度更新
        update_velocity(all_particles_in_pop)

    for j in range(particles_size):  # 位置更新
        update_location(all_particles_in_pop, velocity)

    for j in range(particles_size):  # 适应度更新,传入每一行进去,更新每一个粒子的适应度传入一维数组里
        fitnessvalue[0][j] = calculatefitness(all_particles_in_pop[j])
        update_pbest(fitnessvalue, j, pbest)  # 传入的是当前的适应度的计算位置,当前是哪一个粒子,还有pbest二维数组

    index = fitnessvalue[1].index(max(fitnessvalue[1]))  # 历史适应度值中最好的一个的位置下标
    gbest = all_particles_in_pop[index]  # 取出当前的测试用例
    print("fitness is:", max(fitnessvalue[1]))  # 这里输出的是最好的pbest,即gbest

print("final test case is:", np.array(gbest).reshape(-1, k))
print("there is :", int(np.size(np.array(gbest).reshape(-1, k)) / k), "number of testcase in this array")
print("the optimal particle is:", index)
t1 = time.time()

print("用时：%.6fs" % (t1 - t0))
