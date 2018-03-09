# -*- coding: utf-8 -*-
#ID3决策树
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz #可视化决策树函数

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/sales_data.xls'
data = pd.read_excel(inputfile, index_col=u'序号')
#将标签数值化
data[data == u'是'] = 1
data[data == u'好'] = 1
data[data == u'高'] = 1
data[data != 1] = -1

x = data.iloc[:, :3].as_matrix().astype(int)
y = data.iloc[:, 3].as_matrix().astype(int)

dtc = DTC(criterion='entropy') #基于信息熵建立决策树模型
dtc.fit(x, y)

x = pd.DataFrame(x)
with open("tree.dot", 'w') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)

#生成的tree.dot 文件如下：
# digraph Tree {
# edge [fontname="SimHei"]; /*在生成的dot文件中添加语句设置中文字体*/
# node [fontname="SimHei"];
# 0 [label="是否周末 <= 0.0\nentropy = 0.998\nsamples = 34\nvalue = [16, 18]"] ;
# 1 [label="是否有促销 <= 0.0\nentropy = 0.934\nsamples = 20\nvalue = [13, 7]"] ;
# 0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="False"] ;
# ...}
#安装Graphviz在cdm中运行  dot -Tpdf C:\...\tree.dot -o tree.pdf
#https://www.cnblogs.com/hsydj/p/5853954.html
