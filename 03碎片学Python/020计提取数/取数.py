

import clipboard
import os
import itertools

jf = input("收入计提(s)成本计提(c)费用(f)：")

if jf == "j":
    tiaozheng = 0.958*0.94
elif jf == "s":
    tiaozheng = 0.958
else:
    tiaozheng = 1

m = float(input("输入要算的数："))
p = [16.92461, 107.84779, 101.9435, 25.79245, 127.5, 64.66038, 155.33019,
     14.9717, 18.93396, 8.46226, 33.95283, 132.77358, 19.1712989]
print('单价', p)
a1 = a2 = a3 = a4 = a5 = a8 = a9 = a10 = a11 = a12 = a13 = [
    0, 1, -1, 2, -2]
print('可加减范围', a1)
a6 = a7 = [0, 0, 0, 0, 0]
for i in itertools.product(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13):
    mubiao = i[0]*p[0] + i[1]*p[1] + i[2]*p[2]+i[3]*p[3] + i[4]*p[4] + i[5]*p[5]+i[6]*p[6] + \
        i[7]*p[7] + i[8]*p[8]+i[9]*p[9] + i[10] * \
        p[10] + i[11]*p[11]+i[12]*p[12]

    # m = 113.53

    if m/1.06-0.003 <= mubiao*tiaozheng <= m/1.06+0.003:
        # print(i, mubiao)
        # for j in i:
        #     print(j)
        print(i)
        i_out = '\n'.join([str(j) for j in i])
        # print(i_out)
        break


clipboard.copy(i_out)  # now the clipboard content will be string "abc"
text = clipboard.paste()  # text will have the content of clipboard

os.system("pause")
