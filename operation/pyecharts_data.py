# -*-coding:utf-8-*
# @Time : 2020/4/27 13:45
# @Author : Baojie
# @Site : 
# @File : pyechars_data.py
# @Software: PyCharm
import time


from pyecharts.charts import Line, Page, Bar
from pyecharts import options as opts
from config import config_info
from operation.processing_data import processingData


# 处理获取的数据信息  并进行图形化显示
class charts_Data:
    # 获取时间当前时间（计算到当前的秒）
    @staticmethod
    def getNowTime():
        nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
        return nowTime

    # 每日bug数量统计
    @staticmethod
    def eveBugStatistics():
        # 时间列表作为X轴
        columns = processingData().createTimeList()
        # processingData().BugSum() + "[" + columns[0] + "-" + columns[len(columns) - 1] + "]"
        page = Page("------客户端BUG统计情况------")

        # 制表：先获取保存的信息
        DataInfo = processingData().countClientBug()

        # 获取数据信息列表
        dict = {}
        for client in config_info.get_Project().keys():
            for devName in config_info.get_Project()[client]:
                namelist = devName+"_List"
                namelist = []
                for dateTime in columns:
                    if devName not in DataInfo[dateTime][client]:
                        namelist.append(0)
                    else:
                        namelist.append(DataInfo[dateTime][client][devName])
                # print(client, devName, namelist)
                key = client + devName
                dict[key] = namelist
        print(dict)

        # android开发名字
        android_List = []
        for value in processingData().getProjectInfo()[1][0]:
            for keys in dict.keys():
                if value in keys:
                    # print(value, dict[keys])
                    android_List.append(dict[keys])

        # android需要整合pad和android手机端的数据
        bar_Android = Bar(init_opts = opts.InitOpts(width="1500px"))
        bar_Android.add_xaxis(columns)
        index, all= 0, 0
        android_dict = {}
        for value in processingData().getProjectInfo()[1][0]:
            data = [android_List[index][i] + android_List[index+1][i] for i in range(0, len(android_List[index]))]

            # 获取每个开发的bug数
            sum = 0
            for k in range(0, len(data)):
                sum = sum + data[k]
            android_dict[value] = sum

            bar_Android.add_yaxis(value, data, is_selected=True)
            index = index+2

        # 获取BUG
        for number in android_dict.values():
            all = all + number

        bar_Android.set_global_opts(
            title_opts=opts.TitleOpts(
                # 标题文本使用 \n 换行
                title='Android客户端BUG统计图',
                subtitle="共计：" + str(all) + str(android_dict),)
        )
        # bar_Android.set_global_opts(
        #     xaxis_opts=opts.AxisOpts(
        #         axislabel_opts={"interval": "0"},
        #         # 分割线配置，显示 y 轴每个刻度的分割线
        #         splitline_opts=opts.SplitLineOpts(is_show=True),
        #     )
        # )

        # ios客户端
        ios_dict = {}
        bar_IOS = Bar(init_opts = opts.InitOpts(width="1500px"))
        bar_IOS.add_xaxis(processingData().createTimeList())
        for value in processingData().getProjectInfo()[1][2]:
            for keys in dict.keys():
                if value in keys:
                    bar_IOS.add_yaxis(value, dict[keys], is_selected=True)

                    # 获取每个开发的bug数
                    sum = 0
                    for k in range(0, len( dict[keys])):
                        sum = sum + dict[keys][k]
                    ios_dict[value] = sum

        # 获取BUG总数
        all = 0
        for number in ios_dict.values():
            all = all + number

        bar_IOS.set_global_opts(
            title_opts=opts.TitleOpts(
                # 标题文本使用 \n 换行
                title='IOS客户端BUG统计图',
                subtitle="共计：" + str(all) + str(ios_dict),
            ))
        # bar_IOS.set_global_opts(
        #     xaxis_opts=opts.AxisOpts(
        #         axislabel_opts={"interval": "0"},
        #         # 分割线配置，显示 y 轴每个刻度的分割线
        #         splitline_opts=opts.SplitLineOpts(is_show=True),
        #     )
        # )

        # ipad客户端
        ipad_dict = {}
        bar_IPad = Bar(init_opts = opts.InitOpts(width="1500px"))
        bar_IPad.add_xaxis(processingData().createTimeList())
        for value in processingData().getProjectInfo()[1][3]:
            for keys in dict.keys():
                if value in keys:
                    bar_IPad.add_yaxis(value, dict[keys], is_selected=True)

                    # 获取每个开发的bug数
                    sum = 0
                    for k in range(0, len( dict[keys])):
                        sum = sum + dict[keys][k]
                    ipad_dict[value] = sum

        # 获取BUG总数
        all = 0
        for number in ipad_dict.values():
            all = all + number

        bar_IPad.set_global_opts(
            title_opts=opts.TitleOpts(
                # 标题文本使用 \n 换行
                title='IPad客户端BUG统计图',
                subtitle="共计：" + str(all) + str(ipad_dict),
            ))
        # bar_IPad.set_global_opts(
        #     xaxis_opts=opts.AxisOpts(
        #         axislabel_opts={"interval": "0"},
        #         # 分割线配置，显示 y 轴每个刻度的分割线
        #         splitline_opts=opts.SplitLineOpts(is_show=True),
        #     )
        # )

        # windows客户端
        windows_dict = {}
        bar_Windows = Bar(init_opts = opts.InitOpts(width="1500px"))
        bar_Windows.add_xaxis(processingData().createTimeList())
        for value in processingData().getProjectInfo()[1][4]:
            for keys in dict.keys():
                if value in keys:
                    bar_Windows.add_yaxis(value, dict[keys], is_selected=True)

                    # 获取每个开发的bug数
                    sum = 0
                    for k in range(0, len( dict[keys])):
                        sum = sum + dict[keys][k]
                    windows_dict[value] = sum

        # 获取BUG总数
        all = 0
        for number in windows_dict.values():
            all = all + number

        bar_Windows.set_global_opts(
            title_opts=opts.TitleOpts(

                # 标题文本使用 \n 换行
                title='PC客户端BUG统计图',
                subtitle="共计：" + str(all) + str(windows_dict),
            ))

        page.add(bar_Android, bar_IOS, bar_IPad, bar_Windows)
        page.render(config_info.getFilePath("report", config_info.get_Version() + "_客户端_" + charts_Data().getNowTime() + "_bar_report.html"))

    # 每日bug数量统计
    # @staticmethod
    # def BugStatistics():
    #     global bar, bar1, bar3, bar4
    #     page = Page("------客户端BUG统计情况------")
    #
    #     columns = config_info.get_DateTime()
    #
    #     # 获取相应的开发
    #     ProjectValue = []
    #     for key, value in config_info.get_Project().items():
    #         ProjectValue.append(value)
    #     print(ProjectValue)
    #
    #     for sumbar in range(0, 6):
    #         if sumbar is 0:
    #             data1, data2, data3, data4 = [], [], [], []
    #             for key in columns:
    #                 if ProjectValue[sumbar][0] in save_Data().get_json_data(key)[0]:
    #                     data1.append(save_Data().get_json_data(key)[0][ProjectValue[sumbar][0]])
    #             for key in columns:
    #                 if ProjectValue[sumbar][1] in save_Data().get_json_data(key)[0]:
    #                     data2.append(save_Data().get_json_data(key)[0][ProjectValue[sumbar][1]])
    #             for key in columns:
    #                 if ProjectValue[sumbar][2] in save_Data().get_json_data(key)[0]:
    #                     data3.append(save_Data().get_json_data(key)[0][ProjectValue[sumbar][2]])
    #             for key in columns:
    #                 if ProjectValue[sumbar][3] in save_Data().get_json_data(key)[0]:
    #                     data4.append(save_Data().get_json_data(key)[0][ProjectValue[sumbar][3]])
    #             print(data1, data2, data3, data4)
    #             bar = Bar()
    #             bar.set_global_opts(
    #                 title_opts=opts.TitleOpts(
    #
    #                     # 标题文本使用 \n 换行
    #                     title='Android客户端BUG统计图',
    #                     subtitle=columns[0] + "-" + columns[len(columns)-1],
    #
    #                     # # 标题左右位置：pos_left,pos_right，距离图表左侧/右侧距离
    #                     # # 值可以是像素值如20，也可以是相对值'20%'，或者'left'、'center'、'right'
    #                     # pos_left='20%',
    #                     #
    #                     # # 标题上下位置：pos_top,pos_bottom，距离图表左侧/右侧距离
    #                     # # 值可以是像素值、相对值，或者'top'、'middle'、'bottom'
    #                     # pos_top="middle",
    #                     # # 主副标题间距，默认10
    #                     # item_gap=20,
    #                     #
    #                     # # 主副标题文字样式，调用TextStyleOpts方法设置
    #                     # # 主要配置项：
    #                     # # color,font_style,font_weight,font_family,font_size等
    #                     # title_textstyle_opts=(opts.TextStyleOpts(color='red')),
    #                     # subtitle_textstyle_opts=(opts.TextStyleOpts(font_weight='bolder')),
    #
    #                     # # 主副标题超链接：title_link/subtitle_link
    #                     # title_link='http://www.baidu.com',
    #                     #
    #                     # # 跳转方式:title_target/subtitle_target,'blank'(默认)/'self'
    #                     # title_target='blank'
    #                 ))
    #
    #             # is_label_show是设置上方数据是否显示
    #             bar.add_xaxis(columns)
    #             bar.add_yaxis(ProjectValue[sumbar][0], data1, is_selected=True)
    #             bar.add_yaxis(ProjectValue[sumbar][1], data2, is_selected=True)
    #             bar.add_yaxis(ProjectValue[sumbar][2], data3, is_selected=True)
    #             bar.add_yaxis(ProjectValue[sumbar][3], data4, is_selected=True)
    #
    #         if sumbar is 2:
    #             data1, data2 = [], []
    #             for key in columns:
    #                 if ProjectValue[sumbar][0] in save_Data().get_json_data(key)[sumbar-1]:
    #                     print(ProjectValue[sumbar][0])
    #                     data1.append(save_Data().get_json_data(key)[sumbar-1][ProjectValue[sumbar][0]])
    #             for key in columns:
    #                 if ProjectValue[sumbar][1] in save_Data().get_json_data(key)[sumbar-1]:
    #                     print(ProjectValue[sumbar][1])
    #                     data2.append(save_Data().get_json_data(key)[sumbar-1][ProjectValue[sumbar][1]])
    #             print(data1, data2)
    #             bar1 = Bar()
    #             bar1.set_global_opts(
    #                 title_opts=opts.TitleOpts(
    #
    #                     # 标题文本使用 \n 换行
    #                     title='iPhone客户端BUG统计图',
    #                     subtitle=columns[0] + "-" + columns[len(columns) - 1]))
    #             # is_label_show是设置上方数据是否显示
    #             bar1.add_xaxis(columns)
    #             bar1.add_yaxis(ProjectValue[sumbar][0], data1, is_selected=True)
    #             bar1.add_yaxis(ProjectValue[sumbar][1], data2, is_selected=True)
    #
    #         if sumbar is 3:
    #             data1, data2 = [], []
    #             for key in columns:
    #                 if ProjectValue[sumbar][0] in save_Data().get_json_data(key)[sumbar-1]:
    #                     data1.append(save_Data().get_json_data(key)[sumbar-1][ProjectValue[sumbar][0]])
    #             for key in columns:
    #                 if ProjectValue[sumbar][1] in save_Data().get_json_data(key)[sumbar-1]:
    #                     data2.append(save_Data().get_json_data(key)[sumbar-1][ProjectValue[sumbar][1]])
    #             print(data1, data2)
    #             bar3 = Bar()
    #             bar3.set_global_opts(
    #                 title_opts=opts.TitleOpts(
    #
    #                     # 标题文本使用 \n 换行
    #                     title='iPad客户端BUG统计图',
    #                     subtitle=columns[0] + "-" + columns[len(columns) - 1]
    #                 ))
    #             # is_label_show是设置上方数据是否显示
    #             bar3.add_xaxis(columns)
    #             bar3.add_yaxis(ProjectValue[sumbar][0], data1, is_selected=True)
    #             bar3.add_yaxis(ProjectValue[sumbar][1], data2, is_selected=True)
    #
    #         if sumbar is 4:
    #             data1, data2 = [], []
    #             for key in columns:
    #                 if ProjectValue[sumbar][0] in save_Data().get_json_data(key)[sumbar-1]:
    #                     data1.append(save_Data().get_json_data(key)[sumbar-1][ProjectValue[sumbar][0]])
    #             for key in columns:
    #                 if ProjectValue[sumbar][1] in save_Data().get_json_data(key)[sumbar-1]:
    #                     data2.append(save_Data().get_json_data(key)[sumbar-1][ProjectValue[sumbar][1]])
    #             print(data1, data2)
    #             bar4 = Bar()
    #             bar4.set_global_opts(
    #                 title_opts=opts.TitleOpts(
    #
    #                     # 标题文本使用 \n 换行
    #                     title='Windows客户端BUG统计图',
    #                     subtitle=columns[0] + "-" + columns[len(columns) - 1]))
    #             # is_label_show是设置上方数据是否显示
    #             bar4.add_xaxis(columns)
    #             bar4.add_yaxis(ProjectValue[sumbar][0], data1, is_selected=True)
    #             bar4.add_yaxis(ProjectValue[sumbar][1], data2, is_selected=True)
    #
    #     page.add(bar, bar1, bar3, bar4)
    #     # page.render(config_info.getFilePath("report",   config_info.get_Version()+"_客户端_" + columns[0] + "-" + columns[len(columns) - 1] + "_bar_report.html"))
    #     page.render(config_info.getFilePath("report",   config_info.get_Version()+"_客户端_" + charts_Data().getNowTime() + "_bar_report.html"))


if __name__ == "__main__":
    print(charts_Data().eveBugStatistics())