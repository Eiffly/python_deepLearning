class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
#添加的‘父类’
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

#重新编写继承关系
class Dog(Mammal, RunnableMixIn):
    pass


#实例是可以调用后面的MixIn的（注意这里写的不是Dog.run()）
Dog().run()