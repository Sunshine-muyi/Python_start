# 遍历文件返回文件目录和文件名
import os
from typing import List

allPath = []  # 路径结果
allName = []  # 文件名结果


def file_discover(path: str) -> List[str]:
    allFileRoot = os.listdir(path)  # 获取根目录
    for item in allFileRoot:  # 遍历根目录
        filePath = os.path.join(path, item)
        if os.path.isdir(filePath):  # 如果是目录，循环调用
            file_discover(filePath)
        elif os.path.isfile(filePath):  # 如果是文件，存储结果
            allPath.append(filePath)
            allName.append(item)
    return allPath, allName


if __name__ == '__main__':
    dirRoot = "F:/root"
    files, names = file_discover(dirRoot)
    for file in files:
        print(file)
        with open(file, 'r', encoding='utf-8')as rfile:
            print(rfile.read())
