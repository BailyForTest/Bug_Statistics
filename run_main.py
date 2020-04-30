# -*-coding:utf-8-*
# @Time : 2020/4/28 10:11
# @Author : Baojie
# @Site : 
# @File : run_main.py
# @Software: PyCharm
from operation.save_data import save_Data
from operation.pyecharts_data import charts_Data
from operation.processing_data import processingData


if __name__ == "__main__":
    # # 文件保存
    # save_Data().save_data()
    #
    # # 获取保存数据，key值格式：xxxx_xx_xx
    # save_Data().get_json_data("2020_04_28")
    #
    # # 转化数据格式
    # charts_Data().BugStatistics()

    # 制表
    charts_Data().eveBugStatistics()

