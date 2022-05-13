
#1.基本使用
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:])   #全部
print(L[:1])   #['Michael']
print(L[-1:])  #['Jack']
print(L[:-1])  #['Michael', 'Sarah', 'Tracy', 'Bob']
print(L[:-1:2])  #['Michael', 'Tracy']



#2.可以用来切片的数据类型:list tuple str
print((0, 1, 2, 3, 4, 5)[:3])  #(0, 1, 2)
print('ABCDEFG'[::2])          #ACEG


#3.应用题目:利用切片实现trim函数
print("*******利用切片实现trim函数*******")
def trim(s):
    # if len(s)==0:
    #     return s
    # elif s.isspace()==True:
    #     s='' 
    while s[:1]==" ":
        s=s[1:]
    while s[-1:]==" ":
        s=s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

#为什么要写s[:1]而不是str[0]
str=""
# print(str[0])   #报错
print(str[:1])  #输出为空
print(str[-1:]) #输出为空