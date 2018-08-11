# -*- coding: utf-8 -*-
#用拉格朗日进行异常值插补
import pandas as pd
from scipy.interpolate import lagrange #导入拉格朗日插值函数

inputfile = 'big data/chapter4/demo/data/catering_sale.xls'
outputfile = 'big data/chapter4/demo/tmp/sales1.xls'

data = pd.read_excel(inputfile)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None #将异常值设置为空

#s为列向量，n为被插值的位置，k为取前后的数据个数
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()] #剔除空值
    return lagrange(y.index, list(y))(n) #插值并返回结果

#逐个判断是否需要插值
for i in data.columns: #columns显示全部的列名
    for j in range(len(data)):
        if (data[i].isnull())[j]: #如果为空则插值
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile) #输出结果
