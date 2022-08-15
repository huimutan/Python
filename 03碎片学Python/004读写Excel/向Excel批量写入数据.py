# pip install faker -i https://pypi.douban.com/simple
import xlwt
import faker
import random
wb = xlwt.Workbook()  # 创建一个workbook

# ws = wb.add_sheet('0001')# 创建一个worksheet
# ws.write(1, 1, "第一行第一列的值")  # (行,列,值)
# wb.save("向Excel批量写入的第1个文件.xls")

ws = wb.add_sheet('0002')
head = ['姓名', '年龄', '性别']
for h in head:
    ws.write(0, head.index(h), h)

for i in range(1, 101):
    ws.write(i, 0, faker.Faker(locale='zh_CN').name())
    ws.write(i, 1, random.randint(10, 60))
    ws.write(i, 2, random.choice(['男', '女']))
wb.save("向Excel批量写入的第2个文件.xls")
