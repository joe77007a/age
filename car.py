driving = input('請問你有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有／沒有') 
	raise SystemExit #raise (讓他觸發錯誤)

age = input('請問你的年齡？ ')
age = int(age) #注意
if driving == '有':
    if age >= 18:
        print('恭喜，你通過測驗了')
    else:
        print('登登，你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
	    print('你可以去考駕照了，怎麼不去考') 
	else:
		print('再過幾年就可以考駕照了')
else:
	print('只能輸入 有／沒有') 
