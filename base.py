import pandas as pd

####################################### 数据描述
print(movie_pd.head()) # 前 5 行数据
# .tail(20) 表示显示后 20 行数据
print (movie_pd.info()) # 输出表结构数据类型
print(movie_pd.describe()) # 输出数值描述性统计分析
print(type(movie_pd)) # 数据类型

temp_dict = {
    'score': [8.9, 8.2, 9.3],
    'catagory': ['悬疑', '动作', '科幻']
}
temp_pd = pd.DataFrame(temp_dict) # 创建一个数据框
temp_pd = pd.DataFrame(temp_dict, columns=['catagory','score'], index=['one','two','three'])

tz_counts = frame['tz'].value_counts() # 某列得摘要视图
tz_counts[:10] # 打印前10得统计

print(len(temp_pd)) # 数据的长度
print(temp_pd.index) # 获取当前索引

###################################### 索引
# 设置行索引
temp_pd.index = ['movie_1', 'movie_2', 'movie_3']
# 重命名列名
temp_pd.columns = ['movie_score', 'movie_category']
# 只对第二列重命名为size
temp_pd.rename(columns = {temp_pd.columns[2]:'size'}, inplace=True)
temp_pd.rename(columns={'id': '条数'}, inplace=True)
# 列按指定顺序列排
cols = ['人', '名', '备注1', '备注2']
df_th = df_th.loc[:, cols]

print(temp_pd.values)
# 重置索引
temp_pd = temp_pd.reset_index(drop=True) 
df1.reindex(columns=df2.columns, fill_value=0) # 重置行索引和df2一样，不存在的值用0填充
# column 改为 index
df.set_index('date', inplace=True) 
# index 改为 column
df['index'] = df.index
df.reset_index(level=0, inplace=True) # （the first）index 改为 column

########################################## 数据的筛选
movie_pd.loc[0]
movie_pd.loc[range(10)]
movie_pd.loc[[1, 3, 8]]
movie_pd.ix[0]
movie_pd[:10]
# .loc(索引值)，查询第一行，前10行，2 4 9行的数据

movie_pd['title']
movie_pd[['title', 'score']]
movie_pd.title
# 按列筛选
print(movie_pd.loc[5, 'actors'])
print(movie_pd.loc[[1, 5, 8], ['title', 'actors']])
movie_pd.ix[0,['title', 'actors']]
movie_pd.ix[movie_pd.score > 5, :3]

# 按条件筛选列
print(movie_pd[movie_pd['category'] == '剧情'][['title', 'score']])
# 筛选包含某字符
movie_pd[movie_pd['category'].str.contains('剧情')][['title', 'score']]
y = dt_test[dt_test['path'].str.contains('吧|管|wb')]
# 不包含某些字符
y = dt_test[dt_test['path'].str.contains('吧|管|wb')]
ret = list(set(list(dt_test['path'])) ^ set(list(y['path']))) # 差集，排除包含的字段行
result = dt_test[dt_test['path'].isin(ret)]
# 多条件筛选列
print(movie_pd[(movie_pd['rank'] <=5) & (movie_pd['score'] > 9.0)][['title']])
# 多条件筛选列
print(movie_pd[(movie_pd['release_date'] > '2010-01-01') | (movie_pd['vote_count'] > 500000)])
# 绝对值大于3的所有行
data[(np.abs(data) > 3).any(1)]
# 筛选某个字段的值在给定列表中
movie_pd[movie_pd['score'].isin([8.0, 9.0, 9.5])]
# 筛选含有nan的行
df[df.isna().any(axis=1)]
# 筛选不包含nan的行
df[~df.isna().any(axis=1)]

# 按某几列去重
temp_pd = temp_pd.drop_duplicates(['c1','c2','c3'])
temp_pd = temp_pd[temp_pd['C1'].notnull()][['C1']].drop_duplicates(take_last=True) #take_last保留最后一个
# 取唯一值
temp_pd["name"].unique()
# 删除列
temp_pd = temp_pd.drop(['logtime','name'], axis=1)
del temp_pd['name']
robbery = robbery[~(robbery.year == 2019)]#删除year=2019记录
# 删除行
temp_pd.drop([3,4]) # 删除2，3行


#########################################空值
# 筛选空值
movie_pd[movie_pd['url'].isnull()]
# 筛选非空值
movie_pd[movie_pd['regions'].notnull()]
# 空值填充
df.fillna(0)
# 用一个字符串代替缺失值
df.fillna('missing')
# 用前一个数据代替NaN：method='pad'
df.fillna(method='pad') # method='bfill'向后填充
# 删除包含空值的所有行
df.dropna(axis=0, how='any') # 'all' 所有的都为空的行
df.dropna(subset=['列1', '列2'], inplace=True)

##############################数据替换
# 用“value”替换其中的“to_replace”
df.replace('old', 'new', inplace = True)
# 多值替换
df.replace(['A','29.54'],['B',100])
# 部分字符替换
df['A'] = df['A'].str.replace('aaa', 'bbb')  # .str时不可以inplace = True直接写入原表，要重新赋值


##############################赋值
# 对某列赋值
frame['debt'] = np.arange(5.)  # 赋值1-4得序列
frame['debt'] = Series([2,4,1], index=[1,2,4])
frame[frame < 5] = 0  # 对小于5的数赋值0

#############################数据拼接
df['A'] = "qq" + df['B'].apply(str).str.cat(df['C'].apply(str), sep='-').copy()



#数据框转化为列表
all_data = np.array(all_data)  # np.ndarray()
all_data = all_data.tolist()  # list
# 将 DataFrame 转换为 NumPy 数组
df.as_matrix()

#数据框转字典
>>> df
   col1  col2
0     1     3
1     2     4
>>> [df.to_dict(orient='index')]
[{0: {'col1': 1, 'col2': 3}, 1: {'col1': 2, 'col2': 4}}]
>>> df.to_dict(orient='records')
[{'col1': 1, 'col2': 3}, {'col1': 2, 'col2': 4}]

#########################数据计算
df1 + df2 # 返回对应行列索引得并集，若一个为空则返回NaN
df1.add(df2, fill_value=0) # 实际上的相加，空值则补0   sub剑法\div除法\mul乘法
# “height”列的所有值乘以2
df["height"].apply(lambda height: 2 * height)
# 取最小值的索引
df.idxmin()
# 列之间的关系
df.corr()
# 计算中位数
df["size"].median()
# 行求均值
df.mean(axis=1, skipna=False)  # skipna=False 不排除缺失值，
# 累计统计（每一行均为前几行的和）
df.cumsum()

# 函数映射
df.apply(lambda x: x.max() - x.min())  # 每列的极值的差
df.apply(lambda x: x.max() - x.min(), axis=1) # 每行极差
frame['e'].map(lambda x: '%.2f' % x) # 数值转浮点型
frame.applymap(lambda x: '%.2f' % x)

########################### 数值排序
frame.sort_index()
frame.sort_index(axis=1, ascending=False)  # 按列名索引倒序
# 按列中的值排序
frame.sort_index(by=['a','b'])
df.sort_values(ascending = False)
###############################读写
tmp = pd.read_csv("D:/桌面/aaaaa.csv",engine='python', encoding='utf_8_sig',sep=',')
pp = pd.read_excel('D:/bbb/fffff.xlsx', sheet_name='Sheet3')
pp.to_excel('D:/桌面/啊.xlsx', index=False) # 默认索引不输出
movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')
temp_pd = pd.read_excel('test.xlsx',index=None)
# nrows=5 前五行，skiprows 忽略前多少行，skip_footer 忽略行从尾部算起，encoding 编码，chunksize 分块读取
# 输出
data.to_csv('dd.csv', sep='|', na_rep='NULL', index=False, cols=['a','s'].)

##############################合并数据
# 按b1右连接
tmp = pd.merge(b1, b2, on=['name', 'id'], how='left',suffixes=('_left','_right'))  # suffixes对重复的列尾部追加
# 索引合并
left1.join(right1, how='outer')
left1.join([right1,right2], how='outer')
# 拼接
result = pd.concat([df1, df4], axis=1, sort=False)  # 横向
result = pd.concat([df1, df4], axis=1, join='inner') #交集
result = df1.append(df2)  #纵向
result = df1.append([df2, df3])
esult = pd.concat([df1, df4], ignore_index=True, sort=False)
result = pd.concat([b1,b2,b3], keys=['x', 'y'])
# 外连接 
pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
# 重叠数据合并（用df2补齐df1中缺失的部分）
df1.combine_first(df2)

# 
df['data1'].groupby(df['key1']).mean()
df.groupby(['key1','key2'], as_index=False)[['data2']].mean() # as_index=False 重置索引
df.groupby(['key1','key2'])['data2'].agg(['mean','std']) # agg分别做以下的聚合操作
# 统计数量并排序
robbery.groupby('street').size().sort_values(ascending=False).head(10)
tp = tp.groupby(['ID', 'lg'])['数量'].sum().reset_index(['ID', 'lg'])  # 等同于 select ID,lg,sum(数量) from tp group by ID,lg
tp = tp.groupby(['ID', 'lg'])['数量'].sum().reset_index(['ID', 'lg']).sort_values('数量', ascending=False)  # 降序
robbery.sort_values(by="x1",ascending= False)  
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

# 行列转置
robbery[robbery.year==2018].groupby(['month', 'hour']).size().unstack(0)
#DataFrame.unstack(level=-1, fill_value=None) level索引，默认为-1（最后一级） fill_value缺失值填充
df.stack() # 列转为行，得到的是series类型
# 列转行
df = df.set_index('列1')
df = df.stack()
df.index = df.index.rename('列2', level=1)
df.name = '新列'
df = df.reset_index()
# 行转列
df.pivot(index='lie1', columns='lie2', values='lie3').reset_index()

# 分组统计
age = [3,5,6,2,8,6]
bins = [0,5,10]
cats = pd.cut(age,bins) # (0,5],(5,10]对age分组  ,right=False 左闭右开
pd.value_counts(cats)
pd.cut(age,4,precision=2) # 按最大最小值均匀分4组，小数点后两位
pd.qcut(data, 4) #按4分位数分

# 统计非重复项
df.apply(pd.Series.nunique)
pt = pivot_table(df,
                 values=['b'],
                 index=['a'],
                 aggfunc=lambda x: len(x.unique())
######################################时间处理
from datetime import datetime, date, timedelta

today = datetime.now().strftime('%Y-%m-%d')
yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")

time2 = datetime.now().strftime("%Y%m%d" + '00')
time1 = (date.today() + timedelta(days=-1)).strftime("%Y%m%d" + '00')

# 时间格式
tmp['timestamp'] = tmp['timestamp'].astype('str')
tmp['timestamp'] = tmp['timestamp'].apply(lambda x:datetime.strptime(x,'%Y-%m-%d %H:%M:%S').strftime('%H:%M'))

# 转为秒
tmp['时间差'] = (tmp['time1'] - tmp['time2']).seconds
tmp_pd['距今'] = (today - tmp_pd['last_intime']).dt.days

today = datetime.date.today()
tmp_pd['距今'] = today - tmp_pd['last_intime']
tmp_pd['距今'] = (tmp_pd['距今'] / np.timedelta64(1, 'D')).astype(int)


#转时间戳函数
def time2stamp(cmnttime):   
    cmnttime = datetime.strptime(cmnttime,'%Y-%m-%d %H:%M:%S')
    stamp = int(datetime.timestamp(cmnttime)) * 1000
    return stamp

tmp['stamp'] = tmp['time'].astype(str).apply(time2stamp)

# 时间戳转date
def stamp2time(timeStamp):
    timeArray = time.localtime(int(int(timeStamp)/1000))
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
    return otherStyleTime

tmp['time'] = tmp['stamp'].apply(stamp2time)

# json
import json
# json字符串转字典
path = 'ccc/ccx.txt'
records = [json.loads(line) for line in open(path)]
records[0]['lm'] # 访问第0行，‘lm’key得内容






