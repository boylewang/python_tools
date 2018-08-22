import os
import shutil
#标准库shutils提供了文件和目录管理接口
def newfile(path):
    path=path.strip()
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 不存在
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    #存在
    else:
        print(path+' 目录已存在')
        return False

# 定义要创建的目录
newpath="F:\\14"
# 调用函数
newfile(newpath)
src_files = "F:/ut/gtest"
dst_files = "F:/24"

#递归拷贝文件夹下的文件，不包含该文件夹
#shutil.copytree('F:/ut/gtest', 'F:/24')

#只copy文件内容：shutil.copyfile(src, dst)
#shutil.copyfile("test.txt","test_copyfile.txt")

#拷贝文件和权限：shutil.copy(src, dst) 
#shutil.copy("test.txt","test_copy.txt")

#拷贝文件和状态信息:shutil.copy2(src, dst)
#shutil.copy2("test.txt","test_cpoy2.txt")

#shutil.ignore_patterns(*patterns)　　（忽略哪个文件，有选择性的拷贝,用于拷贝时的ignore选项）
#shutil.ignore_patterns("test.txt","*.py")
#递归的去拷贝文件夹:shutil.copytree(src, dst, symlinks=False, ignore=None)
#shutil.copytree('E:\Git\git_tools\python_tools','E:\Git\git_tools\python_tools_new',symlinks=True, ignore=shutil.ignore_patterns('*.py'))

#shutil.rmtree(path[, ignore_errors[, onerror]])递归的去删除文件,文件夹内可以有文件加，但不能有文件
shutil.rmtree('E:\Git\git_tools\python_tools_new')