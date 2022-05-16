class Student(object):
     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

#给一个【类】【动态】添加属性和方法，类是不受影响的
score=66
Student.score = score

#但是实例是受影响的,比如下面的score
s = Student()      # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25         # 绑定属性'age'
#下面的是报错的 第一个只是已读的，第二个没有属性
# s.score = 99 # 绑定属性'score'  #AttributeError: 'Student' object attribute 'score' is read-only
# s.gender = '男' # 绑定属性'score'  #AttributeError: 'Student' object has no attribute 'gender'

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
     pass
# 子类是不受影响的
g = GraduateStudent()
g.gender = 9999
print(g.gender)