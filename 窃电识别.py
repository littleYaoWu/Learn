# -*- coding: utf-8 -*-
#
"""
def interpolation() 拉格朗日插值
LM神经网络
"""

import pandas as pd
from scipy.interpolate import lagrange
from random import shuffle #随机函数
from keras.models import Sequential #神经网络初始化函数
from  keras.layers.core import Dense, Activation #神经网络层函数、激活函数
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib #模型持久化
from sklearn.metrics import roc_curve #roc曲线函数

#1、预处理-插值
def interpolation():
    inputfile = 'C:/Users/Administrator/Desktop/big data/chapter6/demo/data/missing_data.xls'
    outputfile = 'C:/Users/Administrator/Desktop/big data/chapter6/demo/tmp/missing_data_processed.xls'
    data = pd.read_excel(inputfile, header=None)

    def ployinterp_column(s, n, k=3):
        y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
        y = y[y.notnull()]
        return lagrange(y.index, list(y))(n)

    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:
                data[i][j] = ployinterp_column(data[i], j)

    data.to_excel(outputfile, header=None, index=False)

#2、建模
datafile = 'C:/Users/Administrator/Desktop/big data/chapter6/demo/data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix() #转化为矩阵
shuffle(data) #随机打乱数据

# 划分数据集
p = 0.8
train = data[:int(len(data) * p), :]
test = data[int(len(data) * p):, :]

def cm_plot(y, yp):
    cm = confusion_matrix(y, yp)

    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()

    for x in range(len(cm)):
        for y in range(len(cm)):
            plt.annotate(
                cm[x, y],
                xy=(x, y),
                horizontalalignment='center',
                verticalalignment='center'
            )
    plt.ylabel('True label')
    plt.xlabel('predicted label')
    return plt

#构建LM神经网络模型
def LM_net():
    netfile = 'C:/Users/Administrator/Desktop/big data/chapter6/demo/tmp/net1.model' #模型存储路径

    net = Sequential() #建立神经网络
    net.add(Dense(input_dim=3, units=10)) #输入层3节点，隐藏层10节点
    net.add(Activation('relu')) #隐藏层激活
    net.add(Dense(input_dim=10, units=1))
    net.add(Activation('sigmoid'))
    net.compile(loss='binary_crossentropy', optimizer='adam')

    net.fit(train[:, :3], train[:, 3], nb_epoch=100, batch_size=1)
    net.save_weights(netfile)

    predict_result = net.predict_classes(train[:, :3]).reshape(len(train)) # 预测结果变形
    #keras用predict给出预测概率，predict_classes才是给出预测类别，而且两者的预测结果都是n x 1维数组，而不是通常的 1 x n
    cm_plot(train[:, 3], predict_result).show()

    # 3、模型评价
    # 对神经网络和决策树评价性能，采用ROC曲线，优秀分类器曲线尽量靠近左上角
    predict_result = net.predict(test[:, :3]).reshape(len(test))
    fpr, tpr, thresholds = roc_curve(test[:, 3], predict_result, pos_label=1)
    plt.plot(fpr, tpr, linewidth=2, label='ROC of CART')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.ylim(0, 1.05)
    plt.xlim(0, 1.05)
    plt.legend(loc=4)
    plt.show()
    print(thresholds)

#构建决策树模型
def cart_tree_model():
    treefile = 'C:/Users/Administrator/Desktop/big data/chapter6/demo/tmp/tree3.pkl'
    tree = DecisionTreeClassifier()
    tree.fit(train[:, :3], train[:, 3])
    joblib.dump(tree, treefile)
    cm_plot(train[:, 3], tree.predict(train[:, :3])).show()

    #3、模型评价
    #对神经网络和决策树评价性能，采用ROC曲线，优秀分类器曲线尽量靠近左上角
    predict_result = tree.predict_proba(test[:, :3])[:, 1]
    fpr, tpr, thresholds = roc_curve(test[:, 3], predict_result, pos_label=1)
    plt.plot(fpr, tpr, linewidth=2, label='ROC of CART', color='green')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.ylim(0, 1.05)
    plt.xlim(0, 1.05)
    plt.legend(loc=4)
    plt.show()
    print(thresholds)
