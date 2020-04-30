# -*-coding:utf-8-*
# @Time : 2020/4/27 10:31
# @Author : Baojie
# @Site : 
# @File : config_info.py
# @Software: PyCharm
import os


# 获取文件的相对路径
def getFilePath(dir_name=None, file_name=None):
    filePath = None
    if dir_name is None and file_name is None:
        filePath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    elif dir_name is not None and file_name is None:
        filePath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), dir_name)
    elif dir_name is not None and file_name is not None:
        filePath = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), dir_name), file_name)
    else:
        print("异常情况，请检查逻辑")
    return filePath


def get_Version():
    Version = "3.6.0"
    return Version


def get_Project():
    Project = {"AC_AndroidPad_": [""],
               "AC_AndroidPhone_": [""],
               "AC_iPhone_": [""],
               "AC_iPad_": [""],
               "AC_Windows_": [""],
               "AC_Background_": [""],
               "AC_H5_": [""]}
    return Project

if __name__ == "__main__":
    print(getFilePath("csv_data"))
