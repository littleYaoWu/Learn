# -*- coding: utf-8 -*-
#逻辑回归建模
import pandas as pd

filename = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/bankloan.xls'
data = pd.read_excel(filename)

x = data.iloc[:, :8].as_matrix() #iloc选取自变量范围并转化为矩阵
y = data.iloc[:, 8].as_matrix()

from sklearn.linear_model import LogisticRegression as LR #导入逻辑回归函数
from sklearn.linear_model import RandomizedLogisticRegression as RLR #随机森林
rlr = RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y)
rlr_support = rlr.get_support() #获取特征筛选结果，.scores_可获取各个特征的分数
print(u'通过随机逻辑回归模型筛选特征结束')
support_col = data.drop(data.ix[:,[8]], 1).columns[rlr_support] #去掉最后一列，否则会报一个IndexError的维度错误
print(u'有效特征为： %s' % ','.join(support_col))
x = data[support_col].as_matrix()

lr = LR() #逻辑模型
lr.fit(x, y) #用筛选后的数据训练
print(u'训练结束。')
print(u'模型平均正确率：%s' % lr.score(x, y))
