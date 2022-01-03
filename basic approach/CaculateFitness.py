from initial_paramters import *


def calculatefitness(particle):  # 此处传入的是每一行,也就是每一个粒子
    fitness = 0
    # 初始化bool数组,大小等于k*v
    pairs_captured = np.full((k * v, k * v), False, dtype=bool)
    for testCase in range(0, final_test_case):  # 给出的测试用例集合中的用例个数
        shift = k * testCase  # 每次转移v * testcase 个数据
        for param1 in range(0, k):  # 从0开始到维度个，4 * 3里是4
            for param2 in range(param1 + 1, k):
                allele1 = particle[param1 + shift]  # 注意,此处获取的是基因的值。al1和al2匹配
                allele2 = particle[param2 + shift]
                if not pairs_captured[allele1][allele2]:  # 如果当前所捕获的没有出现过，就把他的值置为1并且适应度+1
                    pairs_captured[allele1][allele2] = True
                    fitness += 1

    return fitness
