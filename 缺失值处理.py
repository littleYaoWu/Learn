    
# 缺失值处理
data.isnull().any() # 判断哪些列是缺失
data[data.isnull().values==True] # 只显示存在缺失值行的数据

data.dropna() # 过滤掉缺失值
data.dropna(how='all') # 整行都是空的过滤掉

data.loc[(data.salary_change.isnull(data)), 'salary_change'] = 'No' # 填充为某个固定值
data.fillna(0) # NaN用 0 填充

data_train.fillna(data_train.mean())  # 将所有行用各自的均值填充 
data_train.fillna(data_train.mean()['browse_his', 'card_num'])  #指定某些行进行填充

data_train.fillna(method='pad')  # 用前一个数据代替NaN：method='pad'
data_train.fillna(method='bfill') # 与pad相反，bfill表示用后一个数据代替NaN

data_train.interpolate() # 插值法就是通过两点（x0，y0），（x1，y1）估计中间点的值 
