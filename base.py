import pandas as pd

####################################### 数据描述
movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')
temp_pd = pd.read_excel('test.xlsx',index=None)
print(movie_pd.head()) # 前 5 行数据
# .tail(20) 表示显示后 20 行数据
print (movie_pd.info()) # 输出表结构数据类型
print(movie_pd.describe()) # 输出数值描述性统计分析
print(type(movie_pd)) # 数据类型

temp_dict = {
    'score': [8.9, 8.2, 9.3],
    'catagory': ['悬疑', '动作', '爱情']
}
temp_pd = pd.DataFrame(temp_dict) # 创建一个数据框
print(temp_pd)

print(len(temp_pd)) # 数据的长度
print(temp_pd.index) # 获取当前索引

###################################### 索引
# 设置行索引
temp_pd.index = ['movie_1', 'movie_2', 'movie_3']
# 重命名列名
temp_pd.columns = ['movie_score', 'movie_category']
print(temp_pd)
print(temp_pd.values)
# 重置索引
temp_pd = temp_pd.reset_index(drop=True)


########################################## 数据的筛选
print(movie_pd.loc[0])
print(movie_pd.loc[range(10)])
print(movie_pd.loc[[1, 3, 8]])
# .loc(索引值)，查询第一行，前10行，2 4 9行的数据

print(movie_pd['title'])
print(movie_pd[['title', 'score']])
# 按列筛选
print(movie_pd.loc[5, 'actors'])
print(movie_pd.loc[[1, 5, 8], ['title', 'actors']])


# 按条件筛选列
print(movie_pd[movie_pd['category'] == '剧情'][['title', 'score']])
# 筛选包含某字符
movie_pd[movie_pd['category'].str.contains('剧情')][['title', 'score']]
# 多条件筛选列
print(movie_pd[(movie_pd['rank'] <=5) & (movie_pd['score'] > 9.0)][['title']])
# 多条件筛选列
print(movie_pd[(movie_pd['release_date'] > '2010-01-01') | (movie_pd['vote_count'] > 500000)])

#########################################空值
# 筛选空值
print(movie_pd[movie_pd['url'].isnull()])  
# 筛选非空值
print(movie_pd[movie_pd['regions'].notnull()]) 
# 筛选某个字段的值在给定列表中
print(movie_pd[movie_pd['score'].isin([8.0, 9.0, 9.5])])  
# 空值填充
df.fillna(0)
# 用一个字符串代替缺失值
df.fillna('missing')
# 用前一个数据代替NaN：method='pad'
df.fillna(method='pad')

# 按某几列去重
temp_pd = temp_pd.drop_duplicates(['c1','c2','c3'])
temp_pd = temp_pd[temp_pd['C1'].notnull()][['C1']].drop_duplicates()

# 删除列
temp_pd = temp_pd.drop(['logtime','name'], axis=1)



#############################数据拼接
df['A'] = "11111__" + df['B'].apply(str).str.cat(df['C'].apply(str), sep='-').copy()



#数据框转化为列表
all_data = np.array(all_data)  # np.ndarray()
all_data = all_data.tolist()  # list
# 按指定顺序列排
cols = ['人', '名', '备注1', '备注2']
df_th = df_th.loc[:, cols]


