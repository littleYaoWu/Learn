# 时间
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

