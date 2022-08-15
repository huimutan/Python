# from datetime import datetime
# import numpy as np
import pandas as pd
import time


path = '\\\\nas1-jf\homes\\移动(家客)资源工单\\gg\\'  # 文件路径D:\\-----------------------
# 读取文件1  , usecols=['ID', '地市']  .loc[:, ["区县", ]]
df1 = pd.read_csv(
    path + "家客业务端到端拓扑关联率-今天.csv", usecols=["区县", "已光调的二级分光器数",  '末端分光器总数', "末端分光器完整总数", "末端光路完整率"])  # 末端分光器总数
df1['末端光路完整率'] = df1['末端光路完整率'].str.strip('%').astype(float)/100
df1.sort_values(by=['末端光路完整率'], ascending=False,
                inplace=True)  # df1['全量'] = df1['末端分光器总数']
df1['末端光路完整率'] = df1['末端光路完整率'].apply(
    lambda x: format(x, '.2%'))

# 读取文件2
df2 = pd.read_csv(
    path + "家客业务端到端拓扑关联率-上月.csv", usecols=["区县", '末端分光器完整总数'])  # 末端分光器总数
df12 = pd.merge(df1.loc[df2['区县'] != '高新区'], df2, how='left', left_on=['区县'], right_on=[
    '区县'])  # 文件一与文件二合并对应列-----------------
df12['月度计划'] = df12['末端分光器总数']-df12['末端分光器完整总数_y']
# ts = datetime.today()
# df12['每日倒推计划'] = (df12['月度计划']/(pd.Timestamp(ts).daysinmonth-ts.day)).round(0)
df12['月度累计'] = df12['末端分光器完整总数_x']-df12['末端分光器完整总数_y']
df12['月完成进度累计'] = df12['月度累计']/df12['月度计划']
df12['月完成进度累计'] = df12['月完成进度累计'] .apply(lambda x: format(x, '.2%'))


# 读取文件3
df3 = pd.read_csv(
    path + "家客业务端到端拓扑关联率-昨天.csv", usecols=["区县", '末端分光器完整总数', '已光调的二级分光器数'])  # 末端分光器总数
df123 = pd.merge(df12, df3, how='left', left_on=['区县'], right_on=[
    '区县'])
df123['当日完成二级分光器光调'] = df123['已光调的二级分光器数_x']-df123['已光调的二级分光器数_y']
df123['当日末端分光器完整数量'] = df123['末端分光器完整总数_x']-df123['末端分光器完整总数']

# 删除列
df123.drop(columns=['末端分光器完整总数', '末端分光器完整总数_x', '末端分光器完整总数_y',
           '已光调的二级分光器数_x', '已光调的二级分光器数_y'], inplace=True)
# 排序
columns = ['区县', '末端分光器总数', '月度计划', '当日完成二级分光器光调',
           '当日末端分光器完整数量', '月度累计', '月完成进度累计', '末端光路完整率']
# 输出到文件
df123.to_csv(path + "结果表.csv", encoding="gb18030",
             index=False, columns=columns)
print('运行结束!')
time.sleep(2)

# 改列名
# students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)
