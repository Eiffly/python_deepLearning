import os # 导入os模块，模块的概念后面讲到


#1.基本使用
#列表生成式
print([x * x for x in range(1, 11)])
#可以筛选
print([x * x for x in range(1, 11) if x % 2 == 0])
#还可以多层循环
print( [m + n for m in 'ABC' for n in 'XYZ'])
# os.listdir可以列出文件和目录
print([d for d in os.listdir('.')])  #['01.切片.py', '02.迭代.py', '03.列表生成式.py']
# print(dir(os))
# 同样，也可以用多个变量接收
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])


# 2.筛选与三元表达式的区别
#放在for后面是筛选，只能用if
print([x for x in range(1, 11) if x % 2 == 0])
#放在for前面是三元表达示，只能用if-else
print([x if x % 2 == 0 else -x for x in range(1, 11)])


#3.练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')