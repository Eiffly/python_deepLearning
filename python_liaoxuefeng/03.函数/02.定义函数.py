import math

#1.可以进行相应的类型检查
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 2.可以引入第三放的库，同时可以返回多个数值，注意接收的时候也要用多个数值接收
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# TypeError: bad operand type:
# my_abs('123')
print('*********自己写的函数***********')
def quadratic(a, b, c):
    gen=b*b-4*a*c
    if gen>=0:
       x1=(-b+ math.sqrt(gen))/(2*a)
       x2=(-b- math.sqrt(gen))/(2*a)
    else:
        print("没有解了")
    return x1,x2

x1,x2=quadratic(1, 3, -4) 
print(x1,x2)
