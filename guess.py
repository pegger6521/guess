# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小
# 這是進階版1 印出猜了幾次

# 這是進階版2 讓使用者決定數隨機數字範圍

import random
start = input ('請輸入隨機數字開始值: ')
end = input ('請輸入隨機數字結束值: ')
start = int(start)
end = int(end)
ans = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == ans:
		print('恭喜猜對了!')
		print ('你總共猜了', count, "次")
		break
	elif num > ans:
		print('比答案大')
	elif num < ans:
		print('比答案小')

	print ('這是你猜的第', count, "次")


