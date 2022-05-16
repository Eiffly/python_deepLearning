#
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print(f(5))         


#同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
print(build(2,3))   #<function build.<locals>.<lambda> at 0x0000015973742AF0>
print(build(2,3)()) #13

#练习
# def is_odd(n):
#     return n % 2 == 1

L = list(filter(lambda x:x % 2 == 1, range(1, 20)))
print(L)  #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]