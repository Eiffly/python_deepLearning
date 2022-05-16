# class Student(object):

#     def get_score(self):
#          return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# #1.通过getter和setter
# s = Student()
# s.set_score(60)
# print(s.get_score()) #60
# # s.set_score(9999) #这里会报错ValueError: score must between 0 ~ 100!


# #2.通过原始方式
# #如果我们不采用上面的getter和setter，下面的还是显示9999
# s._score = 9999
# print(s._score) #9999


# #3.通过装饰器
# #3.1 定义读写属性
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value

# s = Student()
# s.score=60
# print(s.score)
# # s.score=9999 #ValueError: score must between 0 ~ 100!


# #3.2 定义只读属性
# class Student(object):

#     @property
#     def birth(self):
#         return self._birth

#     @birth.setter
#     def birth(self, value):
#         self._birth = value

#     @property
#     def age(self):
#         return 2015 - self._birth

# s = Student()
# s.birth=1998
# print(s.birth)  #1998
# print(s.age)    #17
# s.age=16      #AttributeError: can't set attribute


# #例题：
# class Screen(object):
#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value 

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height= value 

#     @property
#     def resolution(self):
#         return self._height*self._width

# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')