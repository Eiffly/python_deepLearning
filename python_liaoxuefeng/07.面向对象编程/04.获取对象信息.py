class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Husky(Dog):
    def run(self):
        print('Husky is running...')

#使用type()
# print(type(123))
# print(type('str'))
# print(type(None))
# print(type(abs))
# print(type(Animal()))
# print(type(Dog()))

# import types
# def fn():
#     pass
# #判断函数数据类型
# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x: x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)



# #使用instanceof
# #总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。 
# a = Animal()
# d = Dog()
# h = Husky()
# print(isinstance(h, Husky))
# print(isinstance(h, Dog))
# print(isinstance(h, Animal))
# #type()判断的基本类型也可以用isinstance()判断：
# print(isinstance('a', str))
# print(isinstance(123, int))
# print(isinstance(b'a', bytes))
# #还可以判断一个变量是否是某些类型中的【一种】
# print(isinstance([1, 2, 3], (list, tuple)))
# print(isinstance((1, 2, 3), (list, tuple)))


#dir

class MyDog(object):
     def __len__(self):
         return 100
print(dir('ABC'))
#1.在Python中，如果你调用len()函数试图获取一个对象的长度
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的
print('ABC'.__len__()) #3

#2.可以重写某个方法
dog = MyDog()
print(len(dog))       #100
print(dog.__len__())  #100


#3. 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x')) #True
print(hasattr(obj, 'y')) #False
setattr(obj, 'y',19)     #设置一个属性'y'
print(hasattr(obj, 'y')) #True
print(getattr(obj, 'y')) #19
print(obj.y)             #19


#如果获取不存在的属性，会抛出AttributeError的错误：
# print(getattr(obj, 'z')) #AttributeError: 'MyObject' object has no attribute 'z'

#也可以获得对象的方法：
print(hasattr(obj, 'power')) #True
fn = getattr(obj, 'power')
print(fn())                   #81
