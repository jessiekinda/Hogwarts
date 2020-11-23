#1获取excel数据 ---请求体+预期结果
import xlrd
from xlutils.copy import copy
import json

def get_excel_data(sheetName,caseName):
    '''
    :param sheetName: 表名
    :param caseName: 用例名
    :return: 一个列表嵌套元祖[(请求体1，期望值)]
    '''
    resList = []
    excelDir= '../data/在线考试系统接口测试用例-v1.3.xls'
    #打开excel对象
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #2对某一个表操作
    workSheet = workBook.sheet_by_name(sheetName)
    #获取值 第六列和第八列
    #print(workSheet.col_values(0))
    idx=0
    for one in workSheet.col_values(0):
        if caseName in one:
            #请求体--单元格数据---cell(行号，列号)，0从0开始
            reqBody = workSheet.cell(idx,6).value
            resqData = workSheet.cell(idx, 6).value
            #每一行数据增加返回list值
            #字符串---转化--字典， 字典 = json.loads(json数据)
            resList.append((json.loads(reqBody),json.loads(resqData)))

        idx +=1
    return resList



if __name__ == '__main__':
    res=get_excel_data('1-登录模块','login')
    for one in res:
        print(one)



