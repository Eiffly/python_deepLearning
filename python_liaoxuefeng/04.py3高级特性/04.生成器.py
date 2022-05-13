
#1.
#创建生成器的【第一种方式】
g = (x * x for x in range(5))  #这一句是创建了一个生成器
print(g)        
print(next(g))  #0
print(next(g))  #1
print(next(g))  #4
print(next(g))  #9
print(next(g))  #16
# print(next(g))  #报错 StopIteration


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         # 下面也是可以写成  a, b = b, a + b的，就像上面的n, a, b = 0, 0, 1进行了解构一样
#         (a, b) = (b, a + b)
#         n = n + 1
#     return 'done'

# fib(6)

#2.
#创建生成器的【第二种方式】
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数
# 而是一个generator函数，调用一个generator函数将返回一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f=fib(6)
for n in f:
     print(n)
# print(next(f)) #报错



#3.捕获错误
print("******捕获错误***********")
g = fib(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break




# 4.杨辉三角
def triangles():
    L = [1]
    while True:
      yield L
      L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
      n=len(L)-1
      if n == 10:
        break



n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')











# n = 0
# 下面的两种效果是等效的
list1=[1]
list2=[2]
print(list1+list2)
print([1]+[2])

