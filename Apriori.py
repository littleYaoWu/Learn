# -*- coding: utf-8 -*-
# Apriori挖掘菜单关联关系

import pandas as pd
from apriori import *

inputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/data/menu_orders.xls'
outputfile = 'C:/Users/Administrator/Desktop/big data/chapter5/demo/tmp/apriori_rule.xls'
data = pd.read_excel(inputfile, header=None)

print(u'\n转换原始数据至0-1矩阵')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 自定一个函数将非空的都置1
b = map(ct, data.as_matrix())  # map() 会根据提供的函数对指定序列做映射
data = pd.DataFrame(list(b)).fillna(0)  # 转化为数据框，空的置0

# 自定义寻找规则
def connect_string(x, ms):
    x = list(map(lambda i: sorted(i.split(ms)), x))
    l = len(x[0])
    r = []
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i][:l - 1] == x[j][:l - 1] and x[i][l - 1] != x[j][l - 1]:
                r.append(x[i][:l - 1] + sorted([x[j][l - 1], x[i][l - 1]]))
    return r


def find_rule(d, support, confidence, ms):
    result = pd.DataFrame(index=['support', 'confidence'])  # 输出结果
    support_series = 1.0 * d.sum() / len(d)  # 支持度序列
    column = list(support_series[support_series > support].index)  # 初步根据支持度筛选
    k = 0

    while len(column) > 1:
        k += 1
        print(u'\n正在进行第%s次搜索' % k)
        column = connect_string(column, ms)
        print(u'数目：%s' % len(column))

        # 新一批支持度的计算
        def sf(i):
            return d[i].prod(axis=1, numericz_only=True)

        # 创建连接函数
        d_2 = pd.DataFrame(
            list(map(sf, column)), index=[ms.join(i) for i in column]).T

        # 计算连接后的支持度
        support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum() / len(d)
        column = list(support_series_2[support_series_2 > support].index)  # 新一轮支持度筛选
        support_series = support_series.append(support_series_2)
        column2 = []

        for i in column:  # 遍历可能的推理，如{A,B,C}究竟是A+B-->C还是B+C-->A还是C+A-->B？
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        confidence_series = pd.Series(index=[ms.join(i) for i in column2])  # 定义置信度序列

        # 计算置信度序列
        for i in column2:
            confidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[ms.join(i[:len(i) - 1])]

        # 置信度筛选
        for i in confidence_series[confidence_series > confidence].index:
            result[i] = 0.0
            result[i]['confidence'] = confidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    result = result.T.sort(['confidence', 'support'], ascending=False)  # 整理结果
    print(u'\n结果为：')
    print(result)

    return result

support = 0.2  # 最小支持度
confidence = 0.5  # 最小置信度
ms = '---'  # 连接符

find_rule(data, support, confidence, ms).to_excel(outputfile)
