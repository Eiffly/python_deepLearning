# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# print(dir(Enum))
# #__members__是Enum自带的属性，items()是一个视图对象
# for name, member in Month.__members__.items():
#     #value属性则是自动赋给成员的int常量，默认从1开始计数。
#     print(name, '=>', member, ',', member.value) 

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
#读取属性名
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday(1))
print(day1 == Weekday(1))
#读取属性值
print(day1.value)
print(Weekday.Mon.value)
print(Weekday['Mon'].value)
print(Weekday(1).value)
#练习:把Student的gender属性改造为枚举类型，可以避免使用字符串：
# from enum import Enum, unique
# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')