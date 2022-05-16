#__str__
# class Student(object):
#      def __init__(self, name):
#          self.name = name
#      def __str__(self):
#          return f'Student object (name: {self.name})'  
#      __repr__ = __str__
# print(Student('Michael'))


#__iter__ + __getitem__
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1 # 初始化两个计数器a，b

#     def __iter__(self):
#         return self # 实例本身就是迭代对象，故返回自己

#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b # 计算下一个值
#         if self.a > 100000: # 退出循环的条件
#             raise StopIteration()
#         return self.a # 返回下一个值

#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L

# # for n in Fib():
# #      print(n)

# f = Fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[100])
# print(f[85:100])
# # print(f[85:100]) #但是没有对step参数作处理,也没有对负数作处理


# #__getattr__
# class Student(object):

#     def __init__(self):
#         self.name = 'Michael'

#     def __getattr__(self, attr):
#         if attr=='score':
#             return 99
#         if attr=='age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# s = Student()
# print(s.name)
# # 可以返回属性
# print(s.score)
# # 可以返回方法
# print(s.age) 
# print(s.age())
# # 对于不存在的属性或者方法，报错
# # print(s.abc)


# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#     def __str__(self):
#         return self._path
#     __repr__ = __str__
# print(Chain().status.user.timeline.list)

# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print('My name is %s.' % self.name)

# s = Student('Michael')
# s() 
class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
print(Chain().users('michael').repos)
#下面的都是true
print(callable(Chain()))
print(callable(Chain().users))
print(callable(Chain().users('michael')))
print(callable(Chain().users('michael').repos))
