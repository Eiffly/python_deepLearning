# 返回函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f1())
# print(f1==f2) #False f1()和f2()的调用结果互不影响。


#闭包
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs


# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
# print(f1()) #9
# print(f2()) #9
# print(f3()) #9





#nonlocal
# def inc():
#     x = 0
#     def fn():
#         nonlocal x
#         x = x + 1
#         return x
#     return fn

# f = inc()
# print(f()) # 1
# print(f()) # 2



#练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    x=0
    def counter():
         nonlocal x
         x = x + 1
         return x
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')