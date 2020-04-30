# -*-coding:utf-8-*
# @Time : 2020/4/28 13:34
# @Author : Baojie
# @Site : 
# @File : processing_data.py
# @Software: PyCharm
import os
import csv
from config import config_info


class processingData:
    # 初始化信息
    def __init__(self):
        self.Path = config_info.getFilePath("csv_data")  # 需要处理的文件的路径地址
        self.Version = config_info.get_Version()
        self.Project = config_info.get_Project()
        self.data = self.readCsv()

    # 获取路径下最新的文件
    def getFilePath(self):
        lists = os.listdir(self.Path)
        lists.sort(key=lambda fn: os.path.getmtime(os.path.join(self.Path, fn)))

        # 找到最新的文件
        filePath = os.path.join(self.Path, lists[-1])
        return filePath

    # 判断最新的文件是否是Csv格式
    def isCsv(self):
        if '.csv' in str(self.getFilePath()):
            print("File is Csv:", self.getFilePath())
            return True
        else:
            print("File is Not Csv:", self.getFilePath())
            return False

    # 读取CSV文件
    def readCsv(self):
        data = []
        if self.isCsv() is True:
            try:
                print("------文件格式正确，开始读取文件------")
                for i in csv.reader(open(self.getFilePath(), 'r')):
                    # print(i)
                    data.append(i)
            except EOFError:
                print("读取文件错误")
        else:
            print("File Format Is NOt Right")
        return data

    # 获取字段对应的行数值：可以自行添加
    def getRowNo(self):
        global projectID, Severity, bugStatus, toAssigned, Resolver, resolverMethod, createTime
        for i in range(len(self.data[0])):
            if self.data[0][i] == "所属项目":
                projectID = i
            elif self.data[0][i] == "严重程度":
                Severity = i
            elif self.data[0][i] == "Bug状态":
                bugStatus = i
            elif self.data[0][i] == "指派给":
                toAssigned = i
            elif self.data[0][i] == "解决者":
                Resolver = i
            elif self.data[0][i] == "解决方案":
                resolverMethod = i
            elif self.data[0][i] == "创建日期":
                createTime = i
        return projectID, Severity, bugStatus, toAssigned, Resolver, resolverMethod, createTime

    # 根据配置文件获取项目名称和开发人员名称
    def getProjectInfo(self):
        projectKeyList, projectValueList = [], []
        for key, value in self.Project.items():
            projectKeyList.append(key)
            projectValueList.append(value)
        return projectKeyList, projectValueList

    # 获取对应项目的数据信息
    def getVersionData(self):
        # 获取项目的版本信息
        projectKeyList = self.getProjectInfo()[0]

        # 1. 根据项目名称和版本好筛选出对应bug信息    2.取出无效的bug
        projectDataList = []
        reason = ["设计如此", "重复Bug", "外部原因"]
        for projectKey in projectKeyList:
            for projectData in self.data:
                # 通过判断版本号来进行删选
                if (projectKey+config_info.get_Version()) in projectData[self.getRowNo()[0]]:
                    # 剔除reason = ["设计如此", "重复Bug", "外部原因"]的bug记录
                    if projectData[self.getRowNo()[5]] not in reason:
                        projectDataList.append(projectData)
        return projectDataList

    # 获取客户端总数
    def clientBugCount(self, client=None):
        List = []
        VersionData = self.getVersionData()
        for data in VersionData:
            if client in data[self.getRowNo()[0]]:
                List.append(data)
        return List

    # BUG创建时间列表：通过读取getVersionData数据逐行进行判断和添加
    def createTimeList(self):
        createTimeList = []
        versionData = self.getVersionData()
        for eveDate in versionData:
            # 判断各端BUG列表是否为空
            if eveDate is []:
                print("获取的数据为空")
            else:
                # 判断时间是否在createTimeList，是：不操作    否：执行添加
                if eveDate[self.getRowNo()[6]] not in createTimeList:
                    createTimeList.append(eveDate[self.getRowNo()[6]])
        createTimeList.sort()  # 升序排列
        return createTimeList

    # 存储格式：dict
    def saveDataDict(self):
        projectKeyList = config_info.get_Project().keys()
        dataDict = {}
        for createTime in self.createTimeList():
            dataDict[createTime] = {}
            for projectKey in projectKeyList:
                dataDict[createTime][projectKey] = {}
                for projectValue in config_info.get_Project()[projectKey]:
                    dataDict[createTime][projectKey][projectValue] = 0
        return dataDict

    #  每天的生成的bug数量，按照每个段进行分类
    def eveDataList(self):
        projectKeyList = self.getProjectInfo()[0]
        eveData = {}
        versionData = self.getVersionData()
        for createTime in self.createTimeList():
            eveData[createTime] = {}
            for projectKey in projectKeyList:
                eveData[createTime][projectKey] = []
                for eveDate in versionData:
                    if eveDate[self.getRowNo()[6]] == createTime:
                        if (projectKey + config_info.get_Version()) in eveDate[self.getRowNo()[0]]:
                            eveData[createTime][projectKey].append(eveDate)
        return eveData

    # 计算每个端的bug数量
    def countClientBug(self):
        """
        # eveData[createTime] : 每天的bug统计
        # eveData[createTime][projectKey] : 各个端的bug
        :return:
        """
        eveData = self.eveDataList()
        saveDataDict = self.saveDataDict()
        for createTime in self.createTimeList():
            for projectKey in config_info.get_Project().keys():
                if not eveData[createTime][projectKey]:
                    for projectValue in config_info.get_Project()[projectKey]:
                        saveDataDict[createTime][projectKey][projectValue] = 0
                else:
                    eveClientBugList = eveData[createTime][projectKey]
                    # print(eveClientBugList)
                    for eveClientBug in eveClientBugList:
                        if eveClientBug[self.getRowNo()[2]] == "激活":
                            if eveClientBug[self.getRowNo()[3]] not in saveDataDict[createTime][projectKey].keys():
                                saveDataDict[createTime][projectKey][eveClientBug[self.getRowNo()[3]]] = 1
                            else:
                                num = saveDataDict[createTime][projectKey][eveClientBug[self.getRowNo()[3]]]
                                saveDataDict[createTime][projectKey][eveClientBug[self.getRowNo()[3]]] = num + 1
                        elif eveClientBug[self.getRowNo()[2]] == "已解决" or eveClientBug[self.getRowNo()[2]] == "已关闭":
                            # print(createTime, projectKey, eveClientBug[self.getRowNo()[4]])
                            if eveClientBug[self.getRowNo()[4]] not in saveDataDict[createTime][projectKey].keys():
                                saveDataDict[createTime][projectKey][eveClientBug[self.getRowNo()[4]]] = 1
                            else:
                                num = saveDataDict[createTime][projectKey][eveClientBug[self.getRowNo()[4]]]
                                saveDataDict[createTime][projectKey][eveClientBug[self.getRowNo()[4]]] = num + 1
        return saveDataDict

    # 统计所有的bug状态下数据统计
    def BugSum(self):
        openListName, resolveListName, closeListName = [], [], []
        versionData = self.getVersionData()
        # 激活状态下：openList

        print("------------激活状态下Bug统计-------------")
        for openData in versionData:
            if openData[self.getRowNo()[2]] == "激活":
                openListName.append(openData[self.getRowNo()[3]])
        # print(openListName)
        opensSet = set(openListName)
        for item in opensSet:
            print(" %s :拥有bug %d" % (item, openListName.count(item)))

        # 解决状态下数据统计
        print("------------解决状态下Bug统计-------------")
        for resolveDate in versionData:
            if resolveDate[self.getRowNo()[2]] == "已解决":
                resolveListName.append(resolveDate[self.getRowNo()[4]])
        # print(resolveListName)
        opensSet = set(resolveListName)
        for item in opensSet:
            print(" %s :拥有bug %d" % (item, resolveListName.count(item)))

        # 关闭状态下数据统计
        print("------------关闭状态下Bug统计-------------")
        for closeDate in versionData:
            # 需要判断解决方案
            if closeDate[self.getRowNo()[2]] == "已关闭":
                closeListName.append(closeDate[self.getRowNo()[4]])
        # print(closeListName)
        opensSet = set(closeListName)
        for item in opensSet:
            print(" %s :拥有bug %d" % (item, closeListName.count(item)))
        count = "共计BUG: "+"激活-"+str(len(openListName))+".已解决-"+ str(len(resolveListName))+".已关闭-"+str(len(closeListName))
        return count


if __name__ == "__main__":
    # for data in processingData().getVersionData():
    #         print(data)
    # print(len(processingData().getVersionData()))
    # print(len(processingData().clientBugCount(client="AC_AndroidPad")))
    # processingData().createTimeList()
    # print(processingData().eveDataList())
    # processingData().BugSum()
    # processingData().saveDataDict()
    print(processingData().countClientBug())