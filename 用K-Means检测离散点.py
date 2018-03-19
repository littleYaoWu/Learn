# -*- coding: utf-8 -*-
# 用K-Means检测离散点

import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/consumption_data.xls'
data = pd.read_excel(inputfile, index_col='Id')
data_zs = 1.0*(data - data.mean())/data.std()

k = 3 #聚类类别
iteration = 500 #聚类最大循环次数
model = KMeans(n_clusters=k, max_iter=iteration)
model.fit(data_zs)

r = pd.concat([data_zs, pd.Series(model.labels_, index=data.index)], axis=1) #每个样本对应的类别
r.columns = list(data.columns) + [u'聚类类别']

norm = []
for i in range(k):
    norm_tmp = r[['R', 'F', 'M']][r[u'聚类类别'] == i]-model.cluster_centers_[i]
    norm_tmp = norm_tmp.apply(np.linalg.norm, axis = 1) #求绝对距离
    norm.append(norm_tmp/norm_tmp.median()) #求相对距离并添加

norm = pd.concat(norm)

#画图显示离群点
threshold = 2 #离散点阈值
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

norm[norm <= threshold].plot(style = 'go') #正常点
discrete_points = norm[norm > threshold] #离群点
discrete_points.plot(style = 'ro')

for i in range(len(discrete_points)): #离群点做标记
    _id = discrete_points.index[i]
    n = discrete_points.iloc[i]
    plt.annotate('(%s, %0.2f)' % (_id, n), xy=(_id, n), xytext=(_id, n))

plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
plt.show()
