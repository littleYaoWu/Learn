# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn import naive_bayes


# 贝叶斯
iris = load_iris()
trainX = iris.data
trainY = iris.target
clf=naive_bayes.GaussianNB()  #高斯分布，没有参数
# clf=naive_bayes.MultinomialNB()  #多项式分布

clf.fit(trainX,trainY)
print "训练准确率:" + str(clf.score(trainX,trainY))
print "测试准确率:" + str(clf.score(trainX,trainY))


#二分类朴素贝克斯分类器训练函数
def trainNB0(trainMatrix,trainCategory):    #trainMatrix为输入参数的文档矩阵，trainCategory为class标签
    numTrainDocs = len(trainMatrix) #数据集中样本的数量
    numWords = len(trainMatrix[0])  #数据集中特征的数量
    pAbusive = sum(trainCategory) / float(numTrainDocs) #计算class为1的概率
    #初始化概率
    p0Num = zeros(numWords)     #初始化class为0的特征
    p1Num = zeros(numWords)     #初始化class为1的特征
    p0Denmo = 0.0
    p1Denmo = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denmo += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denmo += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denmo
    p0Vect = p0Num/p0Denmo
    return p0Vect,p1Vect,pAbusive	
 
 
#构建朴素贝叶斯分类函数
def classifyNB(vec2Classify,p0Vec,p1Vec,PClass1):
    p1 = sum(vec2Classify * p1Vec) + log(PClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - PClass1)
    if p1 > p0 :
        return 1
    else:
        return 0
