from collections.abc import Iterable
# from functools import reduce
# print(isinstance(map(str,[1,5,3,5]), Iterable) )

# s="11546464"
# result1 = reduce(lambda x,y:y+x,s)
# result2 = reduce(lambda x,y:x+y,s)
# print(result1)
# print(result2)

# 下面的两个效果是一样的
# f1, f2, f3 = 1,23,5
# f1, f2, f3 = [1,23,5]
# print(f1)
# print(f2)
# print(f3)

# def calc1(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

dic={'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dic.keys()
values = dic.values()
items = dic.items()
for key,value in items:
    print(key,value)
    # print(i)       #挨个tuple形式的对象
    # print(list(i)) #挨个list形式的对象