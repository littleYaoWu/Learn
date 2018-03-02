# -*- coding: utf-8 -*-

# 1、数据异常值检查
import pandas as pd
import matplotlib.pyplot as plt
# from __future__ import print_function

catering_sale = 'C:/Users/Administrator/Desktop/big data/chapter3/demo/data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列
# print(data.describe()) #查看数据基本分布情况
# print(len(data)) #打印行数看是否有空行值
# dd = data.dropna() #去掉空值的行，原来的data不会变化

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.figure()
p = data.boxplot() #画箱线图，直接使用DataFrame的方法
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort() #会改变原对象

for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy = (x[i], y[i]), xytext=(x[i]+0.05 - 0.8/(y[i]-y[i-1]), y[i])) #annotate添加注释,调整注释的位置
    else:
        plt.annotate(y[i], xy = (x[i], y[i]), xytext=(x[i]+0.08, y[i]))
plt.show()

#2、数据统计量分析
data = data[(data[u'销量'] > 400) & (data[u'销量'] < 5000)] #过滤异常数据
statistics = data.describe() #保存基本统计量

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位间距

print(statistics)


#做帕累托图2/8法则
dish_profit = 'C:/Users/Administrator/Desktop/big data/chapter3/demo/data/catering_dish_profit.xls'
profit_data = pd.read_excel(dish_profit, index_col = u'菜品名')
profit_data = profit_data[u'盈利'].copy()
profit_data.sort(ascending = False) #降序

plt.figure()
profit_data.plot(kind='bar')
plt.ylabel(u'盈利（元）')
p = 1.0*profit_data.cumsum()/profit_data.sum() #cumsum累加，从大到小逐个累加，计算百分比
#p.plot(color = 'r', secondary_y = True, style = '-o', linewidth = 2) #secondary_y = True运行出错？？？？
plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.ylabel(u'盈利（比例）')
plt.show()

#3、数据相关性分析
catering_sale_all = 'C:/Users/Administrator/Desktop/big data/chapter3/demo/data/catering_sale_all.xls'
sale_data = pd.read_excel(catering_sale_all,index_col = u'日期')

a = sale_data.corr() #相关系数矩阵，任意两个产品之间的相关系数
b = sale_data.corr()[u'百合酱蒸凤爪'] #显示某一个产品与其他产品的相关系数
c = sale_data[u'百合酱蒸凤爪'].corr(sale_data[u'翡翠蒸香茜饺']) #计算某两个产品之间的相关系数
print(c)



