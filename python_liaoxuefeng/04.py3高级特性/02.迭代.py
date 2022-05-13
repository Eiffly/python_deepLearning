from collections.abc import Iterable
# 
# 1.
# 之前我们讨论in后面可以有什么，我们进行了总结
# 但是通过collections.abc模块的Iterable类型就可以为我们进行判断
print(isinstance(123, Iterable))      # false
# 下面的都是true
print(isinstance('abc', Iterable) )
print(isinstance([1,2,3], Iterable))     
print(isinstance((1,2,3), Iterable))     
print(isinstance({15}, Iterable))              
print(isinstance({"15":15}, Iterable))              
print(isinstance({}.keys(), Iterable))    
print(isinstance({}.values(), Iterable)) 
print(isinstance({}.items(), Iterable))  


#2.Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
print("*******索引元素对*********")
for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)


#3.可以是多个变量
print("*******可以是多个变量*********")
for x, y,z in [(1, 2,3), (2,6, 4), (3,1, 9)]:
     print(x, y,z)

#4.练习
def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    else:
        return (min(L),max(L))
        # min=L[0]
        # max=L[0]
        # for x in L:
        #     if x>max:
        #         max=x
        #     if x<min:
        #         min=x  
        # return (min,max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

