#回调函数str是我们内置的回调函数，将类型转变为字符串类型
# map

# def f(x):
#      return x * x

# m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# L1=list(m)
# L2=list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(L1)
# print(L2)



#reduce 
# from functools import reduce
# def add(x, y):
#      return x + y

# res=reduce(add, [1, 3, 5, 7, 9])
# print(res) #25

# 例题1：将字符串数字转换为真实的数字 reduce+map
# #第一种写法
# def fn(x, y):
#      return x * 10 + y
# def char2num(s):
#      digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#      return digits[s]
# # print(map(char2num, '13579')) #生成的是一个map类型的对象
# print(reduce(fn,list(map(char2num, '13579'))))

#第二种写法（封装在一个函数里）
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))
# print(str2int('13579'))

#第三种写法：借用lambda表达式


# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def char2num(s):
#     return DIGITS[s]

# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))



# 例题：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))