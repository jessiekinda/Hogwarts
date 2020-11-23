#增加留言
import requests
from configs.config import HOST
from lib.apiLib.login import Login
#封装类
class Msg:
    def add_msg(self,inToken,inDtada):
        '''
        :param inToken: 登录接口获取token
        :param inDtada:留言新增的body
        :return:
        '''
        url=f'{HOST}/api/message'
        #请求头--需要带token---格式是字典

        header = {'X-AUTH-TOKEN':inToken,'Content-Type': 'application/json'}
        payload = inDtada
        resp = requests.post(url,json=payload,headers=header)
        return resp.json()

if __name__ == '__main__':
    #登录--获取token
    token=Login().login({'username': 20154084, 'password': '123456'},getToken=True)
    info ={"title": "留言标题", "content": "留言内容"}
    res = Msg().add_msg(token,info)
    print(res)#这个留言的id作为后续的删除以及恢复操作


#新增留言




