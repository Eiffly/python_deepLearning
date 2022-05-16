# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('2015-3-25')
# now()
# print(now.__name__) #wrapper 原来的名字被改变了

# #装饰器带参数
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# #使用
# @log('execute')
# def now():
#     print('2015-3-25')

# now()  #相当于执行了 now = log('execute')(now)
# #经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# print(now.__name__) #返回参数是'wrapper'


#不改变函数的name
#方法一：对于不带参数的
# functools.wraps 函数
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


#方法二：对于带参数的
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log('execute')
# # @log
# def now():
#     print('2015-3-25')
# now()
# print(now.__name__) #now

#练习题目:decorator，它可作用于任何函数上，并打印该函数的执行时间
# import time, functools
# def metric(fn):
#      start = time.time()
#      @functools.wraps(fn)
#      def wrapper(*args, **kw):
#         # print('call %s():' % fn.__name__)
#         print('%s executed in %s ms' % (fn.__name__, time.time()-start))
#         return fn(*args, **kw)
#      return wrapper
    


# def metric(func):
#     @functools.wraps(func)
#     def wrapper(*args):
#         # 开始时间
#         start = time.time()
#         # 中间执行时间
#         ans = func(*args)
#         # 结束时间
#         end = time.time()
#         print('%s executed in %s ms' % (func.__name__, end - start))
#         return ans
#     return wrapper

# #测试片段
# @metric
# def fast(x, y):
#     #中间的延迟时间
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     #中间的延迟时间
#     time.sleep(0.1234)
#     return x * y * z
# #这一步骤就相当于已经执行了
# f1 = fast(11, 22)
# s1 = slow(11, 22, 33)
# if f1 != 33:
#     print('测试失败!')
# elif s1 != 7986:
#     print('测试失败!')

# import  functools
# def log(func):
#     print(func)
#     if callable(func):
#         @functools.wraps(func)
#         def wrap(*args, **kw):
#             print('no args %s():' % (func.__name__))
#             print("begin call")
#             r = func(*args, **kw)
#             print("end call")
#             return r
#         return wrap
#     def decorator(func):
#         @functools.wraps(func)
#         def wrap(*args, **kw):
#             print('args  %s %s():' % (func, func.__name__))
#             print("begin call")
#             r = func(*args, **kw)
#             print("end call")
#             return r
#         return wrap
#     return decorator
  

# 在函数开始和结束前后打印句子
import  functools
def log(func):
    # 无参数版本 
    if callable(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("无参数版本 %s():begin call"% (func.__name__))
            f=func(*args, **kw)
            print("无参数版本 %s() :end call"% (func.__name__))
            # print('call %s():' % func.__name__)
            return f
        return wrapper
    #带参数版本
    else:
        # 这种情况下 func就是传入的参数，fn就是要执行的函数
        def decorator(fn):
            @functools.wraps(fn)
            def wrapper(*args, **kw):
                print("带参数版本 参数为%s %s() :begin call" % (func, fn.__name__))
                f=fn(*args, **kw)
                print("带参数版本 参数为%s %s() :end call" % (func, fn.__name__))
                # print('%s %s():' % (text, func.__name__))
                return f
            return wrapper
        return decorator

@log('execute')
def f():
    print("带参数版本:f()被调用了")

@log
def f():
    print("无参数版本:f()被调用了")

f()
