import sqlite3

import urllib.request as u
import re
con = sqlite3.connect('mydb.sqlite3')

# import otherdbMoudlue
# con = otherdbModule(user = "", password = "", host="", database="")

cur = con.cursor()
q = ''' CREATE TABLE IF NOT EXISTS LOGDATA (
 IP VARCHAR(100), 
  DATE VARCHAR(100),
  PICS VARCHAR(100),
  WEBSITE VARCHAR(100) )'''

cur.execute(q)

myurl = 'https://www.jafsoft.com/searchengines/log_sample.html'

f = u.urlopen(myurl)
for line in f:
    #print(line)
    line = line.decode()
    m = re.match('(\d{3}.\d{1,3}.\d{1,3}.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*GET\s+/(pics/(\w+\.\w+))?.*(http[s]?://[a-zA-Z0-9.]+).*' ,line)
    #print(type(line))
    if m != None:
        ip = m.group(1)
        dt = m.group(2)
        im = m.group(4)

        if im == None:
            im = 'No Image'
        wb = m.group(5)
        print(ip, dt, im, wb)
        q = f"INSERT INTO LOGDATA values('{ip}', '{dt}', '{im}', '{wb}')"
        cur.execute(q)
#print(f)

con.commit()
cur.execute('SELECT * from LOGDATA')
result = cur.fetchall()
print(result)

F = open('dbdump.csv', 'w', newline='')
import csv
wt = csv.writer(F)
wt.writerow(['IP', 'DATE', 'PICS', 'WEBSITE'])
for row in result:
    wt.writerow(row)

F.close()
con.close()

import pandas as pd

L = [[10,20,30], [50,60,70]]

df1 = pd.DataFrame(L, index=['row1', 'row2'], columns=['c1', 'c2', 'c3'])
print(df1)


df2 = pd.DataFrame(result)
df2.to_csv('out4.csv')
df2.to_excel('out5.xlsx')
df2.to_json('out6.json')
print(df2)