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
def xiangxiantu():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure()
    x = data.boxplot() # 箱线
    z = data.hist() # 直方图
    plt.show()

xiangxiantu()
