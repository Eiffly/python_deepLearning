#01.ord函数获取字符的整数表示
#  chr()函数把编码转换为对应的字符：
print(ord('A'))   #65
print(ord('中'))  #20013
print(chr(66))    #B
print(chr(25991)) #文
 

#02.如果知道字符的整数编码，还可以用十六进制
print( '\u4e2d\u6587')  #中文


#03
# encode()方法
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示 比如x = b'ABC'
print('ABC'.encode('ascii'))  #b'ABC'
print('中文'.encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii'))   #含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错


# decode()方法:
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print( b'ABC'.decode('ascii'))  #ABC
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  #中文
print(  b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  #中

# len()
# 函数计算的是str的字符数
print(len('ABC'))  #3
print(len(b'ABC'))  #3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  #6
print(len("中文"))  #2 
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
#conclusion：为了避免乱码问题，应当【始终坚持】使用【UTF-8】编码对str和bytes进行转换。

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#---------------------------------------格式化------------------------------------------------
# 
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))  # 'Hi, Michael, you have $1000000.'
print('%1d-%02d' % (3, 1))  #3-01
print('%2d-%02d' % (3, 1))  # 3-01  注意这里的这个空格
print('%.2f' % 3.1415926)   #3.14  表示保留两位小数

#format()
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
print('Hello, {0}, 成绩提升了 {1:.6f}%'.format('小明', 17.125))


#f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}') #The area of a circle with radius 2.5 is 19.62


#---------------------------------------练习------------------------------------------------
s1 = 72
s2 = 85
levelup=(s2-s1)/s2
print(f"小明的成绩提升了{levelup:.1%}") # 明的成绩提升了15.3%
