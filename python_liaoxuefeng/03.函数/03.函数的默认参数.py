# 默认参数的使用
print("**********默认参数的使用1****************")
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))


print("**********默认参数的使用2****************")
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'M', "beijing")
enroll('Adam', 'M', city='Tianjin')


print("**********默认参数的使用3****************")
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())