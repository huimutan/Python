import pandas as pd
p1 = pd.read_csv("拍照杆路.csv", encoding="gb18030", low_memory=False)
p2 = pd.read_csv("新下载杆路.csv", encoding="gb18030", low_memory=False)
p12 = pd.merge(p1, p2, how='left', on="ID")
p12.to_csv("1.csv", encoding="gb18030")
