# 文件的备份
def copyFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名')
    file_list = old_file.split('.')
    # 构造新的文件名 加上备份的后缀
    new_file = file_list[0]+'_backup.'+file_list[1]
    old_file = open(old_file, 'r', encoding='utf-8')
    new_file = open(new_file, 'w', encoding='utf-8')  # 以写的模式打开新文件
    content = old_file.read()  # 读取文件内容
    new_file.write(content)  # 将内容写入到备份文件
    new_file.close()
    old_file.close()
    pass

# 文件的备份


def BigcopyFile():
    # 接受用户输入的文件名
    old_file = input('请输入要备份的文件名\n')
    file_list = old_file.split('.')
    # 构造新的文件名 加上备份的后缀
    new_file = file_list[0]+'_backup.'+file_list[1]
    try:
        # 监视要处理的逻辑
        with open(old_file, 'r', encoding='utf-8') as old_f, open(new_file, 'w', encoding='utf-8') as new_f:  # noqa: E501
            while True:
                content = old_f.read(1024)  # 一次读取1024个字符
                new_f.write(content)
                if len(content) < 1024:
                    break
                    pass
                pass
            pass
    except Exception as msg:
        print(msg)
        pass
    pass


BigcopyFile()
