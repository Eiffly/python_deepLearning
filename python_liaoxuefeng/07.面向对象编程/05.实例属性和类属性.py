class Student(object):
    name = 'Student'
    #这里没有写__init__函数哦

# s = Student('Bob')
s = Student()
print(s.name)       #Student
print(Student.name) #Student
s.name = 'Michael'
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)       #Michael
print(Student.name) #Student
del s.name
print(s.name)       #Student


# 例题
# class Student(object):
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
