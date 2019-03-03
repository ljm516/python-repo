import csv
import math
import operator
import sys
from random import random

'''
	实现 knn 算法：
	1. 数据处理： 打开 csv 文件获取数据，将原始数据分为测试数据和训练数据
	2. 相似性度量： 计算每两个数据实例之间的距离
	3. 近邻查找： 找到 k 个与当前数据最近的邻居
	4. 结果反馈： 从近邻实例反馈结果
	5. 精度评估： 统计预测精度
'''


# 从文件加载数据集
def load_data_set(data_file, split_rate):
    training_set = []
    test_set = []
    with open(data_file, 'r') as fr:
        lines = csv.reader(fr)
        data_set = list(lines)
        for x in range(len(data_set) - 1):
            iter_time = len(data_set[x]) - 1
            for y in range(iter_time):
                data_set[x][y] = float(data_set[x][y])

            # data = [float(d) for d in data_set[x]]
            if random() < split_rate:
                training_set.append(data_set[x])
                # training_set.append(data)
            else:
                test_set.append(data_set[x])
                # test_set.append(data)

    return training_set, test_set


# 获取两点间的欧氏距离
def euclidean_distance(instace_1, instace_2, length):
    distance = 0
    for x in range(length):
        distance += pow((instace_1[x] - instace_2[x]), 2)

    return math.sqrt(distance)


# 获取测试样本的k个最近邻居
def get_neighbors(training_set, test_instance, k):
    distance = []
    length = len(test_instance) - 1
    for x in range(len(training_set)):
        dist = euclidean_distance(instace_1=test_instance, instace_2=training_set[x], length=length)
        distance.append((training_set[x], dist))

    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])

    return neighbors


# 获取预测结果，从邻居点中提取数量最多的那个邻居
def get_response(neighbors):
    class_votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1

    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_votes[0][0]


# 准确度
def get_accuracy(test_set, predictions):
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1

    return (correct / float(len(test_set))) * 100.0


if __name__ == '__main__':
    data_file = sys.argv[1]
    split_rate = 0.8
    training_set, test_set = load_data_set(data_file=data_file, split_rate=split_rate)
    print('training set: {s}'.format(s=len(training_set)))
    print('test set: {s}'.format(s=len(test_set)))

    predictions = []
    k = 3
    for x in range(len(test_set)):
        neighbors = get_neighbors(training_set=training_set, test_instance=test_set[x], k=k)

        print('neighbors: {n}'.format(n=neighbors))
        result = get_response(neighbors=neighbors)
        print('result: {r}'.format(r=result))
        predictions.append(result)
        print('predict: {p}, actual: {a}'.format(p=int(float(result)), a=int(float(test_set[x][-1]))))

    print('predictions: {p}'.format(p=predictions))
    accuracy = get_accuracy(test_set=test_set, predictions=predictions)
    print('accuracy: {a}'.format(a=accuracy))

    print('+Done')
