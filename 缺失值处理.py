    
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

# 定义browse_his缺失值预测填充函数
def set_missing_browse_his(df): 
    # 把已有的数值型特征取出来输入到RandomForestRegressor中
    process_df = df[['browse_his', 'gender', 'job', 'edu', 'marriage', 'family_type']] 
    #分成已知该特征和未知该特征两部分 
    known = process_df[process_df.browse_his.notnull()].as_matrix()
    unknown = process_df[process_df.browse_his.isnull()].as_matrix() 
    X = known[:, 1:] # X为特征属性值
    y = known[:, 0] # y为结果标签值
    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)
    rfr.fit(X,y) 
    # 用得到的模型进行未知特征值预测
    predicted = rfr.predict(unknown[:, 1::]) 
    # 用得到的预测结果填补原缺失数据
    df.loc[(df.browse_his.isnull()), 'browse_his'] = predicted
    return df, rfr
data_train, rfr = set_missing_browse_his(data_train)
