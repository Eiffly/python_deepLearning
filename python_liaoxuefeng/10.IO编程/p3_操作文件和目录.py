import os
# # 查看系统
# print(os.name) #nt表示的是win
# # print(os.uname())  #win10没有
# # 查看环境变量
# print(os.environ)
# # 要获取某个环境变量的值
# print(os.environ.get('PATH'))
# print(os.environ.get('x', 'default'))


# 操作文件和目录
# 显示绝对路径
# print(os.path.abspath('.'))
# # join来表示新目录的完整路径（这个时候还没有创建）
# print(os.path.join('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng', 'testdir'))
# # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# # 但是这里坑我！！！因为 \txxxxx 按照制表符处理了
# os.mkdir('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng\\testdir')
# os.rmdir('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng\\testdir')

#仅仅是处理字符串相关的内容罢了，不一定有文件
# print(os.path.split('/Users/michael/testdir/file.txt'))
# 得到文件扩展名
# print(os.path.splitext('/path/to/file.txt'))

# os.rename('test1.txt', 'test1.py')
# os.remove('test1.py')

# print([x for x in os.listdir('.') ])

#列出所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有文件
print([x for x in os.listdir('.') if os.path.isfile(x)])

#例题
#搜索关键字的文件、目录及其下面的子文件
# import os
# fname = input('please input file name:')
# def search(pwd):
#     flag = 0  #打印目录的控制条件
#     #遍历打印带关键字的文件
#     for x in os.listdir(pwd):
#         if fname in x and os.path.isfile(os.path.join(pwd,x)):
#             if flag == 0:   #打印一次目录
#                 print('\n%s' % pwd)
#                 flag = 1
#             print(x)
#     #记录所有的目录
#     dir_file = []
#     for x in os.listdir(pwd):
#         if os.path.isdir(os.path.join(pwd,x)):
#             dir_file.append(x)
#     #修改路径，进行新一轮查找
#     for x in dir_file:
#         new_fname = os.path.join(pwd,x)
#         search(new_fname)
# def main():
#     pwd = os.path.abspath('.')
#     search(pwd)
# if __name__ == '__main__':
#    main() 



#例题
# import os
# # 遍历目录: 深度遍历
# def search_dir(path):
#     # 1.获取目录下的所有文件名或目录名
#     file_list = os.listdir(path)
#     # 2.遍历每个子目录和子文件
#     for file in file_list:
#         # 3.获取子文件的绝对路径(完整路径)
#         file_path = os.path.join(path, file)
#         # 4.判断文件还是目录
#         if os.path.isfile(file_path):
#             print("文件名:", file)
#         else:
#             print("目录名:", file)
#             # 继续找字目录下的所有文件和目录
#             search_dir(file_path)
# search_dir("D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng")
