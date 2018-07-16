from urllib.request import *
#导入正则库(从页面代码中提取信息)
import re
#导入requests库(请求和页面抓取)
import requests
#导入time库(设置抓取Sleep时间)
import time
#导入random库(生成乱序随机数)
import random
#导入数值计算库(常规计算)
import numpy as np
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#导入绘制图表库(数据可视化)
import matplotlib.pyplot as plt
#导入结巴分词库(分词)
# import jieba as jb
# #导入结巴分词(关键词提取)
# import jieba.analyse

# 抓取百度图片并下载保存
# url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=detail&fr=&hs=0&xthttps=111111&sf=1&fmq=1519544466750_R&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%99%9A%E9%9C%9E&oq=wanxia&rsp=0'
# html = urlopen(url)
# #打开网站
# obj = html.read().decode()
# #获取代码并解码，网页是二进制解码为字符串
# urls = re.findall(r'"objURL":"(.*?)"', obj)
# #链接一个一个的拿出来,重命名并保存
# index = 0
# for url in urls:
#     try:
#         urlretrieve(url, 'pic' + str(index) + '.jpg')
#         index += 1
#     except Exception:
#         print('download error...%d'%index)
#     else:
#         print('download complete...')
# #用try-except避免下载出错情况

# 对天猫商品评论做分析
# 抓取信息
def spiders_TM():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
               'Accept':'*/*',
               'Connection':'keep-alive',
               'Referer':'https://detail.tmall.com/item.htm?spm=a211oj.11506480/N.5888725090.1.7ac34b5aAi2KuU&acm=ak-zebra-9862-15974.1003.1.2501257&id=17302099374&scm=1003.1.ak-zebra-9862-15974.ITEM_17302099374_2501257'
               }
    cookies = {'tk_trace':'1',
              'isg':'BLi421qqFwG0iXuFMUIEjXHoimWKiRzDTupZTPIps_PrDVn3mjBzO9JPwYW9RtSD',
              'cna':'OYXrEhyCzAACAX1NQ6jvUuHX',
              't':'e7e85477fae24d683f537f984cb839d5',
              '_tb_token_':'eb1be3f1e77de',
              'cookie2':'157f37aaa45e1496341c74ff203e7398',
              '_m_h5_tk':'dbf986fa9313ef9fc1729ec76c4a5801_1528470927949',
              '_m_h5_tk_enc':'26cace2d0080ee228dd18953f3384738',
              'hng':'CN|zh-CN|CNY|156',
              'um':'486B7B12C6AA95F25A961CAB368AA6BD775658E52C0B0F33428C50B0BF3C60E6D66AD7510F9CEE7BCD43AD3E795C914C05605BC91791096541CAAA807D44ACE3',
              'JSESSIONID':'36AC9DE6659B38D91953CC62160A769C'
              }
    url1 = 'https://rate.tmall.com/list_detail_rate.htm?itemId=17302099374&spuId=227984099&sellerId=101450072&order=3&currentPage='
    url2 = '&append=0&content=1&tagId=&posi=&picture=&ua=098'
    ran_num = random.sample(range(10), 10)

    for i in ran_num:
        a = ran_num[0]
        if i == a:
            i = str(i)
            url = (url1+i+url2)
            r = requests.get(url=url, headers=headers, cookies=cookies)
            html = r.content
        else:
            i = str(i)
            url = (url1+i+url2)
            r = requests.get(url=url, headers=headers, cookies=cookies)
            html2 = r.content
            html = html + html2
        time.sleep(5)
        print("当前抓取页面：", url, "状态：", r)

    html = str(html, encoding = "GBK")
    file = open("C:\\Users\\wuyao\\Documents\\python\\demo\\page.txt", "w")
    file.write(html)
    file.close()

# 清洗数据
def TM_clear():
    html = open("C:\\Users\\wuyao\\Documents\\python\\demo\\page.txt", "r").read()
    UserNick = re.findall(r'"displayUserNick":"(.*?)",', html)
    UserId = re.findall(r'"headExtraPic".*?,"id":([0-9]{13}),', html)
    rateDate = re.findall(r'"rateContent".*?,"rateDate":"(.*?)",', html)
    content = re.findall(r'"rateContent":"(.*?)"', html)

    hour = []
    for h in rateDate:
        date = h[11:13]
        hour.append(date)

    table = pd.DataFrame({'rateDate': rateDate, 'hour': hour, 'UserId': UserId, 'UserNick': UserNick, 'content': content})
    table['rateDate'] = pd.to_datetime(table['rateDate'])
    table = table.set_index('rateDate')
    table.to_csv('tm_table.csv')

# 分析数据
html = open("C:\\Users\\wuyao\\Documents\\python\\demo\\page.txt", "r").read()
UserNick = re.findall(r'"displayUserNick":"(.*?)",', html)
UserId = re.findall(r'"headExtraPic".*?,"id":([0-9]{13}),', html)
rateDate = re.findall(r'"rateContent".*?,"rateDate":"(.*?)",', html)
content = re.findall(r'"rateContent":"(.*?)"', html)

hour = []
for h in rateDate:
    date = h[11:13]
    hour.append(date)

table = pd.DataFrame({'rateDate': rateDate, 'hour': hour, 'UserId': UserId, 'UserNick': UserNick, 'content': content})
table['rateDate'] = pd.to_datetime(table['rateDate'])
table = table.set_index('rateDate')
# table = pd.read_csv("tm_table.csv")
table_month = table.resample('M', how=len)



