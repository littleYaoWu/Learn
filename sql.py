def select_(values, idlist):
  db = pymysql.connect(host='192.',port=,user='',passwd='',db='',charset='utf8')
  cursor = db.cursor()
  in_p = ', '.join(list(map(lambda x: "'%s'" % x, idlist)))
  sql = "select ...from %s.biaoming where ... in (%s) group by ..."%(values, in_p)
  cursor.execute(sql)
  tmp_pd = cursor.fetchall()
  db.close()

tmp_pd = pd.DataFrame(list(tmp_pd), columns=['q', 'w' ,'e'])
s = [
    ('www', '111'),
    ('qqq', '222')]
    
for key,values in s:
  idlist = np.array(tmp_pd['1'][(md_date['w'] == key)].astype('int')).tolist()
  select_(values, idlist)
    
    
