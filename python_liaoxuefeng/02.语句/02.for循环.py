# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)




print("********************************")
list1=list(range(101))
sum=0
for x in list1:
    sum = sum + x
print(sum)






# ------------------range函数的使用---------------------------
# 打印数字 0 - 9
print("***************可以设置结束的点，默认开始为0*****************")
for x in range(10):
    print(x)

print("***************可以设置起始和结束的点，默认step为0*****************")
for i in range(5,9) :
    print(i)    #5 6 7 8
# 注意访问不到9 

print("*************可以设置step*******************")
for i in range(0, 10, 3) :
    print(i)    #0 3 6 9
# 注意访问不到9 

print("*************可以访问一个数组*******************")
strArr = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for str in strArr:
     print(str) 

print("**************可以访问一个数组索引以及元素******************")
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])


# ------------------in后面可以是什么---------------------------
# in后面可以是range，可以是字符串、list、tuple、视图对象
print("**************in后面是字符串******************")
for i in  "little vegetable cat":
    print(i)

print("**************in后面是list******************")
for i in [1,2,3,4]:
    print(i)

print("**************in后面是tuple******************")
for i in (1,2,3,4):
    print(i)

print("**************in后面是视图对象******************")
dic={'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dic.keys()
values = dic.values()
items = dic.items()
for i in items:
    print(i)       #挨个tuple形式的对象
    print(list(i)) #挨个list形式的对象