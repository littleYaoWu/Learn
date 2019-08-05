########## 时间
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


!pip install python-dateutil
from dateutil.parser import *
# parse()函数解析 字符串时间列incidentdatetime
robbery["year"] = robbery.incidentdatetime.apply(lambda x: parse(x).year)
robbery["month"] = robbery.incidentdatetime.apply(lambda x: parse(x).month)
robbery["hour"] = robbery.incidentdatetime.apply(lambda x: parse(x).hour)
robbery["month"] = robbery.incidentdatetime.apply(lambda x: parse(x).month)
robbery["hour"] = robbery.incidentdatetime.apply(lambda x: parse(x).hour)




robbery = robbery[~(robbery.year == 2019)]#删除year=2019记录


########## 聚合
# 统计数量并排序
robbery.groupby('street').size().sort_values(ascending=False).head(10)

robbery[robbery.year==2018].groupby(['month', 'hour']).size().unstack(0)
#DataFrame.unstack(level=-1, fill_value=None) level索引，默认为-1（最后一级） fill_value缺失值填充

robbery.sort_values(by="x1",ascending= False)  
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
