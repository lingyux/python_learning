import os
import shutil
# # os.rename('test.txt', 'test-1.txt')
# os.remove('test01.txt')  # 前提是文件必须存在
# os.mkdir('test')#不允许级联创建文件夹
# os.rmdir('test')#只能删除空目录
# os.makedirs('d:/01Python/core')
# # 如果删除非空目录，需要引入shutil模块
# shutil.rmtree('d:/01Python/')  # 多级删除非空目录

# 获取当前目录
# print(os.getcwd())
# 路径的拼接
# print(os.path)
# os.path.join(os.getcwd())

# 获取目录列表
# listrs = os.listdir('d:/')
# for item in listrs:
#     print(item)
# scandir和with一起使用，上下文管理器会在迭代器遍历完成之后会自动的释放资源
# with os.scandir('d:/') as dir:
#     for item in dir:
#         print(item.name)
basepath = 'd:/'
for item in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, item)):
        print(item)
