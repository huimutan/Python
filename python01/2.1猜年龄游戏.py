# 直接运行即可，随意修改可能会报错
age = 414//23
print (age)
number = input('猜一猜闻闻的年龄（1-30之间）')
times = 1

while True:
	if times > 2:
		break
	if number.isnumeric():
		if int(number) == age:
			break
		if int(number) > age:
			number = input('闻闻还没有这么大')
		else:
			number = input('猜小了')
	else:
		number = input('需要在下方输入数字')
	times += 1

if times > 2 and int(number) != age:
	print('三次机会用完了')
else:
	print('恭喜你猜中了')
print('闻闻的年龄是' + str(age))