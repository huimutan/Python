# 导入导出txt文件
import pandas as pd
import time
import os
import sys

path = os.path.abspath(os.path.dirname(__file__))  # 本文件路径----
print("当前工作目录为 %s" % path)
time0 = time.time()
# 文件名----------------------
file1 = ['\\7月单据号.xlsx', 'Sheet1']
file2 = ['\\7月凭证号.xlsx', 'sheet10']
if os.path.splitext(file1[0])[-1][1:] == 'csv':
    df1 = pd.read_csv(path + file1[0], encoding="gb18030", low_memory=False)
elif os.path.splitext(file1[0])[-1][1:] in ['xlsx', 'xls']:
    df1 = pd.read_excel(path + file1[0], sheet_name=file1[1])
else:
    df1 = pd.read_table(path + file1[0], encoding="gb2312")

if os.path.splitext(file2[0])[-1][1:] == 'csv':
    df2 = pd.read_csv(path + file2[0], encoding="gb18030", low_memory=False)
elif os.path.splitext(file2[0])[-1][1:] in ['xlsx', 'xls']:
    df2 = pd.read_excel(path + file2[0], sheet_name=file2[1])
else:
    df2 = pd.read_table(path + file2[0], encoding="gb2312")

time1 = time.time()
print('读取文件耗时：' + str(time1-time0))

# how是连接方式，left，right，outer，默认inner
df3 = pd.merge(df1, df2,
               how='left', left_on=['单据编号'], right_on=['外部单据编号'])
# df3 = pd.merge(df1, df2.loc[:, ['分光器名称', '创建时间']],how='left', left_on=['分光器名称'], right_on=['分光器名称'])
# df3 = pd.merge(df1, df2, how='left', left_on=['序号1', '列2'], right_on=['序号5', '列6']) # 文件一与文件二合并对应列-----------------
# df3 = pd.merge(df1.loc[:, ['序号1', '列2']], df2.loc[:, ['序号5', '列6']], how='left', left_on=['序号1', '列2'], right_on=['序号5', '列6']) # 文件一与文件二合并对应列-----------------
time2 = time.time()
print('完成合并两表耗时：' + str(time2-time1))

# df3.to_csv(path + "\结果表.csv", encoding="gb18030", index=False)  # 输出文件
df3.to_excel(path + "\单据号与凭证号匹配.xlsx", encoding="gb18030", index=False)  # 输出文件
time3 = time.time()
print('完成输出文件时间耗时：' + str(time3-time2))
print('Python+pandas总用时：' + str(time3 - time0))
