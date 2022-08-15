import numpy as np
import pandas as pd
df=pd.DataFrame(pd.read_Excel('name.xlsx'))
print (df)
# basestation ="E://05Code//02Python//learnPython//10其他//name.xlsx"
df = pd.read_excel(basestation)
data=df.ix[0].values#0
print (data)