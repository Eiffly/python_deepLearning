print("********************传入一个dict *************************")
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)  #name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing')  #name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')  #name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}


print("******************传入一个dict***************************")
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
# 写法1
person('Jack', 24, city=extra['city'], job=extra['job'])
# 写法2
person('Jack', 24, **extra) 
