# -*- coding: utf-8 -*-
#神经网络
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/sales_data.xls'
data = pd.read_excel(inputfile, index_col=u'序号')

data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].as_matrix().astype(int)
y = data.iloc[:, 3].as_matrix().astype(int)

#导入keras出错，需修改keras.json，将其中的tensorflow改为theano
#解决方案https://zhuanlan.zhihu.com/p/26402501
from keras.models import Sequential
from keras.layers.core import Dense, Activation #activation是逐元素计算的激活函数，Dense分层

model = Sequential() #建立模型
model.add(Dense(input_dim=3, units=10)) #3个输入节点，10个隐藏节点
model.add(Activation('relu')) #用relu函数作为激活函数，提升准确度
model.add(Dense(input_dim=10, units=1))
model.add(Activation('sigmoid')) #由于是0-1输出，用sigmoid做激活函数

#修正神经网络
model.compile(loss='binary_crossentropy', optimizer='adam')
#编译模型，做的是二元分类所以指定损失函数binary_crossentropy，模式为binary
#adam求解的方法
model.fit(x, y, nb_epoch=1000, batch_size=10) #进行1000次的学习

yp = model.predict_classes(x).reshape(len(y)) #分类预测

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

cm_plot(y, yp).show()
