# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000) #自变量，0-10,1000等分的数组
y = np.sin(x) + 1 #因变量
z = np.cos(x**2) + 1 #因变量

plt.figure(figsize=(8, 4)) #设置图像大小
plt.plot(x, y, label = '$\sin x+1$', color = 'red', linewidth = 2) #作图
plt.plot(x, z, 'b--', label = '$\cos x^2+1$')
plt.xlabel(u'时间', fontproperties = 'SimHei') #x轴标签,显示中文需设置字体
plt.ylabel('volt') #y轴标签
plt.title(u'一个例子', fontproperties = 'LiSu', fontsize = 20)
plt.ylim(0, 2.2)
plt.legend() #显示图例
plt.show() #显示结果

def bingtu():
    labels='frogs','hogs','dogs','logs'
    sizes=15,20,45,10
    colors='yellowgreen','gold','lightskyblue','lightcoral'
    explode=0,0.1,0,0
    plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
    plt.axis('equal')
    plt.show()


inputfile = 'BehaviorScore.xlsx'
data = pd.read_excel(inputfile, index_col='user_id')
# 简单箱线图
def xiangxiantu():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure()
    x = data.boxplot() # 箱线
    z = data.hist() # 直方图
    plt.show()


# 箱线图-标出异常值
def xiangxiantu(data):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(1, figsize=(13, 26))
    p = data.boxplot(return_type='dict')
    for i in range(0, 3):
        x = p['fliers'][i].get_xdata()
        y = p['fliers'][i].get_ydata()
        y.sort()
        for i in range(len(x)):
            if i > 0:
                plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
            else:
                plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
    plt.show()
    
    
    
# 密度分布曲线
def Density_distribution(x):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    mu = np.mean(x)
    sigma = np.std(x)  # 标准差δ
    num_bins = 100  # 直方图柱子的数量
    n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)
    # 直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，蓝方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
    y = mlab.normpdf(bins, mu, sigma)  # 拟合一条最佳正态分布曲线y
    plt.plot(bins, y, 'r--')  # 绘制y的曲线
    plt.xlabel(u'数值')  # 绘制x轴
    plt.ylabel('Probability')
    plt.title(u'一组数值的概率分布')
    plt.subplots_adjust(left=0.15)  # 左边距
    plt.show()

  
