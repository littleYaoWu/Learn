# 读取报错的时候encoding='gbk',errors="ignore" 忽略错误
data = open("xxxx.log", encoding='gbk',errors="ignore").read()


#datan=pd.concat([data1,data2,data3,data4,data5],axis=1)    
data1.to_csv("train_innoraml.csv") 
# 保存数据报错
# UnicodeEncodeError: ‘ascii’ codec can’t encode characters in position 0-1: ordinal not in range(128)
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

