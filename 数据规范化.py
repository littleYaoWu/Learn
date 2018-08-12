# -*- coding: utf-8 -*-
# 数据规范化
import pandas as pd
import numpy as np

datafile = 'C:/Users/Administrator/Desktop/big data/chapter4/demo/data/normalization_data.xls'
data = pd.read_excel(datafile, header = None) #数据无名称

# 归一化
min_max = (data - data.min())/(data.max() - data.min()) #最小最大规范法
zero_mean = (data - data.mean())/data.std() #零-均值规范法
dec_ = data/10**np.ceil(np.log10(data.abs().max())) #小数定标法

outdata = [data, min_max, zero_mean, dec_]
for var in outdata:
    print(var)

  
