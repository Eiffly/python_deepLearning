# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1]) #Tracy
classmates.pop() 
print('classmates =', classmates)  #['Michael', 'Bob']

#-----------------------------相关的函数------------------------
classmates.append('Adam')
print(classmates)  #['Michael', 'Bob', 'Adam']

classmates.insert(1, 'Jack')
print(classmates)  #['Michael', 'Jack', 'Bob', 'Adam']

classmates.pop()
print(classmates)  #['Michael', 'Jack', 'Bob']

classmates.pop(1)  
print(classmates)  #['Michael', 'Bob'],同时这个函数的返回值是'Jack'

classmates[1] = 'Sarah'
print(classmates)  #['Michael', 'Sarah']


L = ['Apple', 123, True]
print(L)  #['Apple', 123, True]





