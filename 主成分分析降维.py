# -*- coding: utf-8 -*-
#主成分分析降维
import pandas as pd

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter4/demo/data/principal_component.xls'
outfile = 'C:/Users/Administrator/Desktop/big data/chapter4/demo/tmp/dimention.xls'

data = pd.read_excel(inputfile, header = None)

from sklearn.decomposition import PCA

pca = PCA()
pca.fit(data)
pca.components_ #返回模型各个特征向量
pca.explained_variance_ratio_ #返回各个成分各自的方差百分比
#前3个成分已达97%，选取前3个重新建模

pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data) #降低维度
pd.DataFrame(low_d).to_excel(outfile)
pca.inverse_transform(low_d) #恢复原数据
