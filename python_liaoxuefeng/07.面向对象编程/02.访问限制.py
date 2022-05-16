#1.
# __单独封装
# class Student(object):

#     def __init__(self, name, score):
#         self._name = name
#         self._score = score

#     def print_score(self):
#         print('%s: %s' % (self._name, self._score))
    

# bart = Student('Bart Simpson', 59)
# print(bart)
# print(bart._name)  #AttributeError: 'Student' object has no attribute '__name'
#AttributeError: 'Student' object has no attribute '__print_score'
# print(bart.__print_score())
# print(bart._Student__name)

#2.getter和setter
# class Student(object):
   
#     def __init__(self, name, score):
#             self.__name = name
#             self.__score = score
#     #getter
#     def get_name(self):
#         return self.__name

#     def get_score(self):
#         return self.__score
    
#     #setter
#     def set_name(self, name):
#         self.__name = name

#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')

# bart = Student('Bart Simpson', 59)
# # #访问
# # print(bart.get_name())
# # #修改
# # bart.set_name("Lilian")
# # print(bart.get_name())

# bart.set_score(101)



#例题
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        self.__gender = gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')