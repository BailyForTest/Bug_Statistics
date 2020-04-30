# -*-coding:utf-8-*
# @Time : 2020/4/27 11:17
# @Author : Baojie
# @Site : 
# @File : save_data.py
# @Software: PyCharm
import json
import os
import time

from config import config_info

# 将获取到的数据按照日期进行保存到本地
class save_Data():

    def __init__(self, fileName=None):
        if fileName is None:
            self.file_path = config_info.getFilePath("save_data", "data.json")
        else:
            self.file_path = config_info.getFilePath("save_data", fileName)
        self.key = self.get_DateTime()
        self.read_data = self.read_data()

    # 获取当前的日期时间，作为key值
    @staticmethod
    def get_DateTime():
        nowTime = time.strftime("%Y_%m_%d")
        return nowTime

    # 读取json文件
    def read_data(self):
        # 判断是否存在路径   如果不存在断言找不到文件git
        assert os.path.exists(os.path.split(self.file_path)[0]), ['can not find filepath']
        try:
            with open(self.file_path, 'rb') as fp:
                read_Data = json.load(fp)
                return read_Data
        except Exception as e:
            print("file read fail：", e)
        # fp.close()

    # 保存data
    def save_data(self):
        if self.read_data:
            self.read_data = {}

        try:
            if not os.path.exists(os.path.split(self.file_path)[0]):
                # 目录不存在创建，makedirs可以创建多级目录
                print("file path not exist，create ......")
                os.makedirs(os.path.split(self.file_path)[0])
                print("file  is create success")
        except Exception as e:
            print("file is create fail：", e)

        try:
            # 保存数据到文件
            with open(self.file_path, 'wb') as fp:
                self.read_data[self.key] = devBugInfo().saveData()
                fp.write(json.dumps(self.read_data).encode('utf-8'))
        except Exception as e:
            print("file save fail：", e)
        # fp.close()

    def saveData(self, data):
        try:
            if not os.path.exists(os.path.split(self.file_path)[0]):
                # 目录不存在创建，makedirs可以创建多级目录
                print("file path not exist，create ......")
                os.makedirs(os.path.split(self.file_path)[0])
                print("file  is create success")
        except Exception as e:
            print("file is create fail：", e)

        try:
            # 保存数据到文件
            with open(self.file_path, 'wb') as fp:
                fp.write(json.dumps(data).encode('utf-8'))
        except Exception as e:
            print("file save fail：", e)
        # fp.close()

    # 获取data信息
    def get_json_data(self, key):
        return self.read_data[key]


if __name__ == "__main__":
    # print(save_Data())
    print(save_Data().save_data())
    print(save_Data().get_json_data("2020_04_28"))