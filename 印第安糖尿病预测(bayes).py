# !/usr/bin/env python3
# -*-coding: utf-8-*-


import numpy
import pandas as pd

def loadData():  # 加载csv文件
    dataSet = pd.read_csv('indians-diabetes.csv', header=None)
    return dataSet


# 数据预处理，将属性与标签分开，同时以中值填充缺少数据，将数据转化为矩阵格式
def dataPrepreocess(dataSet):
    dataSet[[0, 1, 2, 3, 4, 5, 6, 7]] = dataSet[[0, 1, 2, 3, 4, 5, 6, 7]].replace(0, numpy.NaN)
    data = dataSet[[0, 1, 2, 3, 4, 5, 6, 7]] # 特征属性列
    data.fillna(data.median(), inplace=True)  # 以中值填充空白
    label = dataSet[8] # 类别列

    data = numpy.matrix(data.as_matrix(columns=None))  # 转化为举证
    label = numpy.matrix(label.as_matrix(columns=None))

    return data, label.T


def dataSplit(data, label):  # 分训练集和测试集
    mid = int(len(data) * 0.6)
    trainData = data[0:mid]  # stop 60% as train data
    testData = data[mid:]

    trainLabel = label[0:mid, 0]
    testLabel = label[mid:, 0]

    return trainData, trainLabel, testData, testLabel


def featureIterator(Data):  # 输入数据矩阵属性的迭代器，即每次返回矩阵的一列
    sampleNumbers, featureNumbers = Data.shape
    for i in range(featureNumbers):
        yield trainData[:, i]


def itemIterator(Data):  # 输入数据矩阵例子的迭代器，即每次返回矩阵的一行
    for i in range(len(Data)):
        yield numpy.ravel(Data[i, :])


def average(feature, i, trainLabel):  # 求一种类下某种属性的平均值
    sum_, count = 0, 0
    for j in range(len(feature)):
        if trainLabel[j] == i:
            sum_ += feature[j]
            count += 1
    return float(sum_ / count)


def variance(feature, i, trainLabel):  # 求一种类下某种属性的方差
    ave = average(feature, i, trainLabel)
    sum_, count = 0, 0
    for j in range(len(feature)):
        if trainLabel[j] == i:
            sum_ += (feature[j] - ave) ** 2
            count += 1
    return float(sum_ / count)


def gaussDistribute(x, average, variance):  # 计算连续属性的高斯分布函数
    part1 = 1 / ((2 * numpy.pi) ** 0.5 * (variance ** 0.5))
    part2 = numpy.exp(-(x - average) ** 2 / (2 * variance ** 2))
    return part1 / part2


def assess(result, label):  # 评估预测结果与实际结果是否相同的函数
    count = 0
    for i in range(len(result)):
        if result[i] == label[i][0]:
            count += 1
    return count / len(label)


class naive_bayes_classifier():  # 贝叶斯分类
    def __init__(self):
        self._classnumber = 0  # 记录分类标签数
        self._featurenumber = 0  # 记录属性数
        self._samplenumber = 0  # 记录测试集样本数
        self._priorProbility = []  # 先验分布查询表
        self._unionProbility = {}  # 使用字典建立的联合分布表

    def get_priorProbility(self, Label):  # 计算先验分布，使用了拉普拉斯修正
        priorProbility = [0] * self._classnumber
        for i in range(len(Label)):  # 统计每个种类的样本数
            priorProbility[int(Label[i])] += 1
        for i in range(self._classnumber):  # 计算先验分布
            priorProbility[i] = (priorProbility[i] + 1) / (len(Label) + self._classnumber)
        self._priorProbility = priorProbility
        print('先验概率：%s' %priorProbility)

    def get_unionProbility(self, trainData, trainLabel):  # 计算联合分布，使用了拉普拉斯修正
        unionProbility = {}
        classgroup = [0] * self._classnumber  # 用于存储每组样本数

        for i in range(len(trainLabel)):
            classgroup[int(trainLabel[i])] += 1  # 统计每个种类的样本数
        print('测试集类别样本数：%s' %classgroup)

        for i in range(self._classnumber):  # 先建立一个联合分布二重循环嵌套存储字典，第三重在下一个循环建立
            unionProbility[i] = {}
            for j in range(self._featurenumber):
                unionProbility[i][j] = {}

        for i in range(self._classnumber):  # 核心循环，建立联合分布概率查询字典
            for feature, j in zip(featureIterator(trainData), range(self._featurenumber)):
                if j == 0:  # 第0个属性为离散变量，单独处理
                    low = int(min(feature.tolist())[0])
                    high = int(max(feature.tolist())[0])
                    k = low
                    while k <= high:
                        if k not in unionProbility[i][j]:
                            unionProbility[i][j][k] = 1
                        for p in range(self._samplenumber):
                            if int(feature[p]) == k:
                                unionProbility[i][j][k] += 1
                        unionProbility[i][j][k] /= float(classgroup[i] + high - low + 1)
                        k += 1
                else:
                    unionProbility[i][j][average] = average(feature, i, trainLabel)  # 连续属性只需要存储均值和方差
                    unionProbility[i][j][variance] = variance(feature, i, trainLabel)

        self._unionProbility = unionProbility
        print(unionProbility)

    def fit(self, trainData, trainLabel):  # 拟合函数
        self._classnumber = max(numpy.ravel(trainLabel.tolist())) + 1
        self._samplenumber, self._featurenumber = trainData.shape
        self.get_priorProbility(trainLabel)
        self.get_unionProbility(trainData, trainLabel)

    def predict(self, testData):  # 预测函数
        predictResult = []
        res = [1] * self._classnumber
        for item in itemIterator(testData):  # 计算每个样本对应不同分类的可能性概率
            for i in range(self._classnumber):
                res[i] = self._priorProbility[i]
                for j in range(self._featurenumber):
                    if j == 0:
                        res[i] *= self._unionProbility[i][j][item[j]]
                    else:
                        res[i] *= gaussDistribute(item[j], self._unionProbility[i][j][average],
                                                  self._unionProbility[i][j][variance])
            maxp = max(res)
            for i in range(self._classnumber):  # 判定为概率最大的种类
                if maxp == res[i]:
                    kind = i
                    predictResult.append(kind)
        return predictResult


if __name__ == '__main__':
    dataSet = loadData()
    data, label = dataPrepreocess(dataSet)
    trainData, trainLabel, testData, testLabel = dataSplit(data, label)

    nbc = naive_bayes_classifier()
    nbc.fit(trainData, trainLabel)
    res = nbc.predict(testData)

    testLabel = testLabel.tolist()
    success = assess(res, testLabel)

    print(success)

