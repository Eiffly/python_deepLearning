# from module1 import greeting
import module1
print(module1.greeting('floye'))
print(module1.greeting('jh'))
# ????????这里为什么还是可以执行呢？留一个疑问
print(module1._private_1('jh'))
