import numpy as np
import pandas as pd
import time
from datetime import date

# 读取
path = ''  # 文件路径D:\\-----------------------
df1 = pd.read_csv(path + "新下载杆路.csv", encoding="gb18030", low_memory=False)
df2 = pd.read_csv(path + "拍照杆路.csv", encoding="gb18030", low_memory=False)

# 合并
df3 = pd.merge(df1, df2.loc[:, ['ID', '红线内光缆段数', '红线外光缆段数',
                                '是否红线内为空光缆段数', '报表生成时间', '比例']], how='left', on='ID').fillna(0)  # how是连接方式，left，right，outer，默认inner
df3.to_csv(path + "结果表.csv", encoding="gb18030",
           index=False)  # 输出文件-------------------#utf-8

print('Done!')
time.sleep(2)


