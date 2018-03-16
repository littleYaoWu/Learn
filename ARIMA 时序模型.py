# -*- coding: utf-8 -*-
# ARIMA 时序模型

"""
调用了多次plt.show()
解决方案，使用plt.subplot()
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf  # 自相关图,偏自相关图
from statsmodels.tsa.stattools import adfuller as ADF #平稳性检测
from statsmodels.sandbox.stats.diagnostic import acorr_ljungbox #白噪声检验
from statsmodels.tsa.arima_model import ARIMA

discfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/arima_data.xls'
data = pd.read_excel(discfile, index_col=u'日期')
forecastnum = 5 #预测天数

#时序图——结果递增判断为非平稳序列
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data.plot()

#第一张自相关图——系数长期大于0，有很强的长期相关性
fig = plt.figure(figsize=(8, 6))
ax1 = plt.subplot(411)
fig = plot_acf(data, ax=ax1)

#平稳性检测
print(u'原始序列的ADF检验结果为：', ADF(data[u'销量']))
# 返回值依次为adf(原始序列的单位根)、pvalue、usedlag、nobs、critical values、icbest、regresults、resstore
#p值0.99显著大于0.05，该序列为非平稳序列

#进行差分
D_data = data.diff().dropna() #diff沿着指定轴计算第N维的离散差值，即矩阵后一个元素减去前一个元素
D_data.columns = [u'销量差分']
D_data.plot() #差分后的时序图
plot_acf(D_data) #自相关图
plot_pacf(D_data) #偏自相关图
# plt.show()
print(u'差分序列的ADF检验结果为：', ADF(D_data[u'销量差分']))
#一阶差分后时序图在均值附近波动，自相关图有很强的短期相关性，p值0.02小于0.05，说明序列是平稳序列

#对一阶差分后的序列做白噪声检验
print(u'差分序列的白噪声检验结果为：', acorr_ljungbox(D_data, lags=1))
#输出为stat、p值，0.00077远小于0.05，所以是平稳白噪声序列
data[u'销量'] = data[u'销量'].astype(float)

#对平稳白噪声序列拟合ARMA模型
#1、先定级确定p,q
pmax = int(len(D_data)/10) #一般阶数不超过length/10
qmax = int(len(D_data)/10)
bic_matrix = [] #bic矩阵
data.dropna(inplace=True)

import warnings
warnings.filterwarnings('error')
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try: #用try跳过报错
            tmp.append(ARIMA(data, (p,1,q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)

#2、找最小值
bic_matrix = pd.DataFrame(bic_matrix)
p, q = bic_matrix.stack().idxmin() #用stack展开，然后找出最小值位置
print(u'BIC最小的p值和q值为：%s、 %s' % (p, q))

#3、建模
model = ARIMA(data, (p, 1, q)).fit() #自相关图一阶截尾，偏自相关图拖尾，考虑用MA(1)拟合
#下面有个编码报错，修改编码为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print(model.summary2()) #模型报告
print(model.forecast(forecastnum) )#预测5天，返回预测结果、标准误差、置信区间
