# 可以使用isinstance()判断一个对象是否是Iterator对象
# 注意是Iterator！！！！不是Iterable！！！！


from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator)) #True
print(isinstance([], Iterator))                     #False
print(isinstance({}, Iterator))                     #False
print(isinstance('abc', Iterator))                  #False






