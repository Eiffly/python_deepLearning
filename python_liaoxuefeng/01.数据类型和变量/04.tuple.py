
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
# classmates[0] = 'Adam'





#----------------------------对于某些内置的、地址存储的数据类型来说是检测不到的-----------------------------
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  #('a', 'b', ['X', 'Y'])
# t[0]='A'  #TypeError: 'tuple' object does not support item assignment

#--------------------------------例题-------------------------------
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

#------------------------------易错点：小括号---------------------------------
# tuple=()
# print(tuple)  #()

# # 
# tuple = (1,)
# print(tuple)  #(1,)
# # 
# tuple = (1)
# print(tuple)  #1

