# 1.创建类和实例
# class Student(object):
#     pass

# bart = Student()
# print(bart)
# print(Student)

# 2.初始化的方法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
# 传入的参数不全会报下面的错误 
# missing 1 required positional argument: 'score'
# bart = Student(59) 
bart = Student('Bart Simpson', 59)
print(bart.name) #Bart Simpson