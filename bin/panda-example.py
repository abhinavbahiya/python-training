import pandas as pd

df1 = pd.read_csv('dbdump.csv')

df2 = df1.head(5)
#print(df2)
df3 = df1.tail(5)
#print(df3)
df4 = df1['IP']
#print(df4)
df5 = df1['ID'].describe()
#print(df5)
df6 = df1.describe()
#print(df6)
df7 = df1['ID'].mean()
#print(df7)

df8 = df1['PICS'].value_counts()

#print(df8)

import matplotlib.pyplot as plt

df8.plot()
#plt.show()
df8.plot.bar()
plt.savefig('graph.png')

writer = pd.ExcelWriter('report.xlsx', engine='xlsxwriter')
#print(writer)

df8.to_excel(writer, sheet_name='data')

wb = writer.book

ws = wb.add_worksheet('graph')

ws.insert_image('B1', 'graph.png')
writer.close()



#---------------------------

df9 = df1['PICS'].str.endswith('JPG')

df10 = df1[df1['ID'] > 10]

df11 = df1.groupby(['PICS']).count()
print(df11)
df12 = df1.iloc[1,1]
df13 = df1.iloc[1:3]
df14 = df1.iloc[1:3, 1]
df15 = df1.iloc[1:3, 1:3]
df16 = df1.iloc[[1, 3], [1, 2]]
print(df16)