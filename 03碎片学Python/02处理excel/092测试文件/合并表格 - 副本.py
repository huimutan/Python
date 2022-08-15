import numpy as np
import pandas as pd
import time
from datetime import date

# 读取
path = ''  # 文件路径D:\\-----------------------
df1 = pd.read_csv(path + "新下载杆路.csv", encoding="gb18030", low_memory=False)
df2 = pd.read_csv(path + "拍照杆路.csv", encoding="gb18030", low_memory=False)
# 略看
print(df1.head(2))
print(df2.head(2))
# 赋值
# df1['ID'].at[df1.index]=100
# 排序
# products.sort_values(by=['Worthy', 'Price'], ascending=[True, False], inplace=True)
# 筛选
# students = students.loc[students.Age.apply(    lambda a:18 <= a <= 30)].loc[students.Score.apply(lambda s:60 <= s < 90)]

# 合并
df3 = pd.merge(df1, df2.loc[:, ['ID', '红线内光缆段数', '红线外光缆段数',
                                '是否红线内为空光缆段数', '报表生成时间', '比例']], how='left', on='ID').fillna(0)  # how是连接方式，left，right，outer，默认inner
# df3 = pd.merge(df1, df2, how='left', left_on=['序号1', '列2'], right_on=['序号5', '列6'])  # 文件一与文件二合并对应列-----------------
# df3 = pd.merge(df1.loc[:, ['序号1', '列2']], df2.loc[:, ['序号5', '列6']], how='left', left_on=['序号1', '列2'], right_on=['序号5', '列6'])  # 文件一与文件二合并对应列-----------------
df3.to_csv(path + "结果表.csv", encoding="gb18030",
           index=False)  # 输出文件-------------------#utf-8

print('Done!')
time.sleep(2)


# 分割
'''split(" ",n=3,expand=True)分列出的数据保留3列 #series.str.split()
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]'''
# 合并2
# table = students.join(scores, how='left').fillna(0)
# 行列方向统计
'''row_sum = students[['Test_1', 'Test_2', 'Test_3']].sum(axis=1)  # 在列方向统计
# https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
row_mean = students[['Test_1', 'Test_2', 'Test_3']].mean(axis=1)
students['Total'] = row_sum
students['Average'] = row_mean  # 把结果放回去
col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)  # 加了一行
'''
# 数据分组
'''orders = pd.read_excel('Orders.xlsx', dtype={'Date': date})
orders['Year'] = pd.DatetimeIndex(orders.Date).year
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt1 = pd.DataFrame({'Sum': s, 'Count': c})
print(pt1)'''
# 透视表
# pt2 = orders.pivot_table(index='Category', columns='Year',values='Total', aggfunc=np.sum) #index=[u'主客场',u'对手'] ,,values=[u'得分',u'助攻',u'篮板'],aggfunc=[np.sum,np.mean]
# 透视表比分组更强大,以下两句话等价
# pd.pivot_table(df,index=[字段1],values=[字段2],aggfunc=[函数],fill_value=0)
# df.groupby([字段1])[字段2].agg(函数).fillna(0)

# 行操作
'''
# 追加已有
students = page_001.append(page_002).reset_index(drop=True)

# 追加新建
stu = pd.Series({'ID': 41, 'Name': 'Abel', 'Score': 90})
students = students.append(stu, ignore_index=True)

# 删除（可切片）
students = students.drop(index=[39, 40])

# 插入
stu = pd.Series({'ID': 100, 'Name': 'Bailey', 'Score': 100})
part1 = students[:21]  # .iloc[] is the same
part2 = students[21:]
students = part1.append(stu, ignore_index=True).append(
    part2).reset_index(drop=True)

# 更改
stu = pd.Series({'ID': 101, 'Name': 'Danni', 'Score': 101})
students.iloc[39] = stu

# 设置空值
for i in range(5, 15):
    students['Name'].at[i] = ''

# 去掉空值
missing = students.loc[students['Name'] == '']
students.drop(missing.index, inplace=True)
'''
# 列操作
'''
# 追加列
students['Age'] = 25

# 删除列
students.drop(columns=['Score', 'Age'], inplace=True)

# 插入列
students.insert(1, column='Foo', value=np.repeat('foo', len(students)))

# 改列名
students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)

# 设置空值
students['ID'] = students['ID'].astype(float)
for i in range(5, 15):
    students['ID'].at[i] = np.nan

# 去掉空值
students.dropna(inplace=True)
students.drop
'''
