import functools
def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))  #64

int2 = functools.partial(int, base=2)
print(int2('1000000')) #64


max2 = functools.partial(max, 10)
print(max2(5, 6, 7))  #10


int2 = functools.partial(int, base=2)
print(int2('10010')) #18


kw = { 'base': 2 }
print(int('10010', **kw)) #18

