a = 'ABC'
b = a
a = 'XYZ'
print(a) #XYZ
print(b) #ABC
print(a==b) #False
print("*****************") #False

# /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
# //，称为地板除，两个整数的除法仍然是整数

print(10//3)  #3
print(10/3)   #3.3333333333333335
 

print("*****************") #False
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
