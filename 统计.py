from pandas import Series,DataFrame
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
ages = [20,22,25,27,21,23,37,31,61,45,41,32]
#将所有的ages进行分组
bins = [18,25,35,60,100]
#使用pandas中的cut对年龄数据进行分组
cats = pd.cut(ages,bins,right=False) #right=False,左边[1,2)
# print(cats)
#调用pd.value_counts方法统计每个区间的个数
number=pd.value_counts(cats)
print(pd.value_counts(cats))
# 按区间求和
result = pd.DataFrame(ages).groupby(pd.cut(ages, bins)).sum()
print(result)
#显示第几个区间index值
# index=pd.cut(ages,bins).codes
# print(index)
#为分类出来的每一组年龄加上标签
group_names = ["Youth","YouthAdult","MiddleAged","Senior"]
personType=pd.cut(ages,bins,labels=group_names)
print(personType)
plt.hist(personType)
plt.show()
#cut和qcut的用法
data=[1,2,3,4,5,6,7,8,9,10]
result=pd.qcut(data,4)
# print(' ',result)##qcut会将10个数据进行排序，然后再将data数据均分成四组
#统计落在每个区间的元素个数
# print('dasdasdasdasdas:     ',pd.value_counts(result))
#qcut : 跟cut一样也可以自定义分位数（0到1之间的数值，包括端点）
# results=pd.qcut(data,[0,0.1,0.5,0.9,1])
# print('results:      ',results)

# 按要求求值
ls_total = []
for j in bins:
    out = []
    for i in ages:
        if i > j:
            out.append(i)
    print(j,sum(out))
    ls_total.append(sum(out))

print(ls_total)
