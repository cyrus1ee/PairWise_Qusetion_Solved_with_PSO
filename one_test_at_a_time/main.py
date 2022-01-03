from PSO import *
from fitness import *

# 初始化种群
init_testcase = init_pop(all_particles_in_pop)

# 适应度更新,传入每一行进去,更新每一个粒子的适应度传入一维数组里
for i in range(particles_size):
    caculatefintess(init_testcase[i], i)  # 计算相应的每一个粒子的适应度

ind = fitness[0].index(max(fitness[0]))  # 将最大适应度所对应的粒子的下标获取出来
output_fitness.extend([fitness[0][ind]])  # 将该组最优的粒子适应度记录下来
final_test_array.extend(init_testcase[ind])  # 将其加入到最终的输出 set P中

change_matrix(init_testcase[ind])  # 更改全覆盖数组的适应度
reset_fitness_array(fitness)   # 重置适应度记录数组

# PSO
for i in range(max_itera):

    # 第二次计算适应度，并更新pbest，选出gbest
    for j in range(particles_size):
        caculatefintess(init_testcase[j], j)
        update_pbest(fitness, j, pbest)  # 传入的是当*前的适应度的计算位置,当前是哪一个粒子,还有pbest二维数组

    # 计算gbest
    if np.all(fitness[0]):
        pass
    else:
        index = fitness[1].index(max(fitness[1]))  # 历史适应度值中最好的一个的位置下标
        gbest = init_testcase[index]

    if max(fitness[0]) >= 1:
        ind = fitness[0].index(max(fitness[0]))
        output_fitness.extend([fitness[0][ind]])
        final_test_array.extend(init_testcase[ind])
        change_matrix(init_testcase[ind])
    else:
        pass

    for j in range(particles_size):  # 速度更新
        update_velocity(init_testcase)

    for j in range(particles_size):  # 位置更新
        update_location(init_testcase, velocity)  # 把速度和当前位置传进去,对位置进行更新

    reset_fitness_array(fitness)

print("final cover matrix is:\n", all_cover)
print("final test case is:", np.array(final_test_array).reshape(-1, k))
print("the fitness of these case is:", output_fitness)
print("there is :", int(np.size(np.array(final_test_array).reshape(-1, k)) / k), "number of testcase in this array")
