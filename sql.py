# 多条件遍历查询
def select_(values, idlist):
  db = pymysql.connect(host='1.1.1.1',port=,user='',passwd='',db='',charset='utf8')
  cursor = db.cursor()
  in_p = ', '.join(list(map(lambda x: "'%s'" % x, idlist))) # 查询的条件组合一起
  sql = "select A,B from %s.table where C in (%s) group by A"%(values, in_p)
  cursor.execute(sql)
  tmp_pd = cursor.fetchall()
  db.close()
  return tmp_pd

tmp_pd = pd.DataFrame(list(tmp_pd), columns=['s', 'w' ,'e']) # tmp_pd转换为DataFrame

s = [
    ('www', '111'),
    ('qqq', '222')] 
for key,values in s: # 遍历查询列表
  idlist = np.array(tmp_pd['S'][(tmp_pd['w'] == key)].astype('int')).tolist() # 查询条件转换为队列
  select_(values, idlist)

  
  

