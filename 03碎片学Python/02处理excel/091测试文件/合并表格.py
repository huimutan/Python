# 导入导出txt文件
import pandas as pd
import time
time0 = time.time()

path = ''  # 文件路径D:\\-----------------------
df1 = pd.read_csv(path + "新下载杆路.csv", encoding="gb18030",
                  low_memory=False, usecols=['ID', '地市'])
df2 = pd.read_csv(path + "拍照杆路.csv", encoding="gb18030", low_memory=False)

time1 = time.time()
print('读取文件耗时：' + str(time1-time0))

# how是连接方式，left，right，outer，默认inner
df3 = pd.merge(df1, df2.loc[:, ['ID', '红线内光缆段数', '红线外光缆段数',
                                '是否红线内为空光缆段数', '报表生成时间', '比例']], how='inner', on='ID')
# df3 = pd.merge(df1, df2, how='left', left_on=['序号1', '列2'], right_on=['序号5', '列6'])  # 文件一与文件二合并对应列-----------------
# df3 = pd.merge(df1.loc[:, ['序号1', '列2']], df2.loc[:, ['序号5', '列6']], how='left', left_on=['序号1', '列2'], right_on=['序号5', '列6'])  # 文件一与文件二合并对应列-----------------
time2 = time.time()
print('完成合并两表耗时：' + str(time2-time1))

df3.to_csv(path + "结果表.csv", encoding="gb18030",
           index=False)  # 输出文件-------------------#utf-8
time3 = time.time()
print('完成输出文件时间耗时：' + str(time3-time2))
print('Python+pandas总用时：' + str(time3 - time0))
