import pytest
from tools.ExcelData import get_excel_data
from lib.apiLib.login import Login
#1.获取excel数据
#mresList= get_excel_data('1-登录模块','login')
#2 数据传入接口代码---请求体

testData = {'username': 20154084, 'password': '123456'}
#1 登录的测试类
'''
从excel货物请求体/响应的预期结果
'''
class TestLogin:
    @pytest.mark.parametrize('inBody,expData',get_excel_data('1-登录模块','login'))
    def test_login(self,inBody,expData):
        #2调用登录的接口代码
        res = Login().login(inBody,getToken=False)#获取响应数据----字典
        # 3 写入测试结果 pass/fail 预期结果与实际结果对比
        assert res['message'] ==expData['message']

if __name__ == '__main__':
    pytest.main(['test_login.py','-s'])

'''
-s:控制台显示打印信息
-F：断言失败
.  成功
E  异常
'''