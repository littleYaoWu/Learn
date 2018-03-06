# -*- coding: utf-8 -*-
#数据离散化
import pandas as pd

datafile = 'C:/Users/Administrator/Desktop/big data/chapter4/demo/data/discretization_data.xls'
data = pd.read_excel(datafile)
data = data[u'肝气郁结证型系数'].copy()

#等宽离散化
k = 4 #分4类
d1 = pd.cut(data, k, labels=range(k)) #各类命名为0,1,2,3

#等频率离散化
w = [1.0*i/k for i in range(k+1)]
w = data.describe(percentiles=w)[4:4+k+1] #describe计算基本统计数据，然后提取分布情况的数据
w[0] *= 1 - 1e-10
d2 = pd.cut(data, w, labels=range(k))

#基于聚类
from sklearn.cluster import KMeans
kmodel = KMeans(n_clusters=k) #建立模型
kmodel.fit(data.reshape((len(data), 1))) #fit训练模型，reshape数据变成1列
c = pd.DataFrame(kmodel.cluster_centers_).sort(0) #输出聚类中心并排序
w = pd.rolling_mean(c, 2).iloc[1:] #相邻两项求中点，作为边界点
w = [0] + list(w[0]) + [data.max()] #加上首末位置的点
d3 = pd.cut(data, w, labels=range(k))

def cluster_plot(d, k):#显示聚类结果
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8, 3))
    for j in range(0, k):
        plt.plot(data[d == j], [j for i in d[d == j]], 'o')

    plt.ylim(-0.5, k-0.5)
    return plt

cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
cluster_plot(d3, k).show()
