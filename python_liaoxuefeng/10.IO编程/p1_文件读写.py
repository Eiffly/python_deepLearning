import os
# 如果不知道绝对路径，可以先用下面的这句查着
# print(os.path.abspath('.'))



# try:
#     f=open('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng\\test.txt', 'r',encoding="utf_8")
#     print(f.read())
# finally:
#     if f:
#         f.close()
####上面的内容等效于下面的这句###########
# with open('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng\\test.txt', 'r',encoding="utf_8") as f:
#     for line in f.readlines():
#         print(line.strip()) # 把末尾的'\n'删掉


# 读取二进制文件
# f = open('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng\伏黑惠.png', 'rb')
# print(f.read())
# f.close()

#写文件
with open('D:\李菲\研究生\课程\课题\python_deepLearning\python_liaoxuefeng\\test.txt', 'a',encoding="utf_8") as f:
    f.write('Hello, world!')


