password = 'a123456'
trial = 3
while trial > 0:
	trial = trial - 1
	pwd = input('請輸入密碼： ')
	if password == pwd:
	    print('登入成功！')
	    break # 逃出迴圈
	else:
		print('密碼錯誤！')
		if trial > 0:
			print('還有', trial, '次機會')
		else:
			print('沒機會嘗試了！要鎖帳號了啦！')