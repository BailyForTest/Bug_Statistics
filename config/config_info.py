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
    Project = {"AC_AndroidPad_": ["马李鑫", "徐铁鹏", "尤灵刚", "黄文鸽"],
               "AC_AndroidPhone_": ["马李鑫", "徐铁鹏", "尤灵刚", "黄文鸽"],
               "AC_iPhone_": ["周松", "俞立荣"],
               "AC_iPad_": ["龚慧超", "张津铭"],
               "AC_Windows_": ["王财坡", "陈明泉"],
               "AC_Background_": ["郭栋梁", "黄章明"],
               "AC_H5_": ["曾杨平"]}
    return Project

if __name__ == "__main__":
    print(getFilePath("csv_data"))