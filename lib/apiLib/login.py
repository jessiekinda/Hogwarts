#完成登录代码的编写----依据接口文档
#获取token值，一般是在前后端分离的时候用到
#接口的url  ----参数化
from configs.config import HOST
import requests
import pprint
import hashlib

'''
封装思想
1.登录接口比较特殊
用途：获取登录token---给后续接口做关联
    接口本身也需要做自动化测试
'''

def get_md5(psw):
    md5 = hashlib.md5()
    md5.update(psw.encode('utf-8'))
    return md5.hexdigest()#加密后的结果，十六进制的格式

class Login:#登录类
    def login(self,inData,getToken=False):#实力方法
        url = f'{HOST}/api/loginS'
        # 请求体 body
        payload = inData
        payload['password']=get_md5(payload['password'])#字典---修改值的条件
        #字典修改值操作，字典名[键名]=新的值
        resp = requests.post(url, json=payload)
        if getToken:
            return resp.json()['token']
        else:
            return resp.json()

if __name__ == '__main__':
    testData = {'username': 20154084, 'password': '123456'}
    #实例化对象
    res = Login().login(testData,getToken=True)
    print(res)




