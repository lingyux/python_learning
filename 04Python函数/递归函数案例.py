# 递归案例：模拟实现树形结构的遍历
import os  # 引用文件操作模块


def find_file(file_path):
    listRs = os.listdir(file_path)  # 得到该路径下所有的文件夹
    for fileItem in listRs:
        full_path = os.path.join(file_path, fileItem)  # 获取完整的文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            find_file(full_path)  # 如果是文件夹 再次递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass


# 调用搜索文件夹对象
find_file('D:\\00学习课件')
