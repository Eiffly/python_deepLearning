# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


#-----------------------------练习---------------------------


bmi = 80/(1.75*1.75)
print(bmi)
if bmi < 18.5:
    print('过轻')
elif bmi <25:
    print('正常')
elif  bmi<28:
    print('过重')
elif  bmi<32:
    print('肥胖')
else:
    print('严重肥胖')  