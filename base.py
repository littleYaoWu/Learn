import pandas as pd

movie_pd = pd.read_csv('douban_movie.csv', header = 0, sep = '\t')
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
temp_pd.index = ['movie_1', 'movie_2', 'movie_3']
temp_pd.columns = ['movie_score', 'movie_category']
print(temp_pd)
print(temp_pd.values)
# 更改行列的索引

# 数据的筛选

print(movie_pd.loc[0])
print(movie_pd.loc[range(10)])
print(movie_pd.loc[[1, 3, 8]])
# .loc(索引值)，查询第一行，前10行，2 4 9行的数据

print(movie_pd['title'])
print(movie_pd[['title', 'score']])
# 按列筛选

print(movie_pd.loc[5, 'actors'])
print(movie_pd.loc[[1, 5, 8], ['title', 'actors']])
# 按一行一列或多行多列同时筛选

# 筛选电影类型是剧情的 title 和 score 两列
print(movie_pd[movie_pd['category'] == '剧情'][['title', 'score']])

# 筛选电影排名小于等于 5 且评分高于 9.0 的 title 一列
print(movie_pd[(movie_pd['rank'] <=5) & (movie_pd['score'] > 9.0)][['title']])

# 筛选电影发布日期大于 2010-01-01 或 评论数超过 50万 的所有列
print(movie_pd[(movie_pd['release_date'] > '2010-01-01') | (movie_pd['vote_count'] > 500000)])

print(movie_pd[movie_pd['url'].isnull()])  # 筛选空值
print(movie_pd[movie_pd['regions'].notnull()]) # 筛选非空值
print(movie_pd[movie_pd['score'].isin([8.0, 9.0, 9.5])])  # 筛选某个字段的值在给定列表中
