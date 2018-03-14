# -*- coding: utf-8 -*-
#k-means聚类

#修改编码格式
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

import pandas as pd
from sklearn.cluster import KMeans

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/consumption_data.xls'
outputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/tmp/data_type1.xls'
data = pd.read_excel(inputfile, index_col='Id')
data_zs = 1.0*(data - data.mean())/data.std() #数据标准化 零-均值规范法

k = 3 #聚类类别
iteration = 500 #聚类最大循环次数
model = KMeans(n_clusters=k, max_iter=iteration) #分k类
model.fit(data_zs)

#打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别数目
r2 = pd.DataFrame(model.cluster_centers_) #找聚类中心
r = pd.concat([r2, r1], axis=1) #横向连接
r.columns = list(data.columns) + [u'类别数目']
print(r)

#输出每个样本对应的类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + [u'聚类类别']
# r.to_excel(outputfile)

#绘制聚类后的概率密度图
def density_plot(data, k):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel(u'密度') for i in range(k)]
    plt.legend() #显示图例
    return plt

pic_output = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/tmp/pd1_'
for i in range(k):
    density_plot(data[r[u'聚类类别']==i], k).savefig(u'%s%s.png' %(pic_output, i))
