
import requests
def test_wenxinweb_demo():

    corpid ="ww8c60b4408fc42f94"
    corpsecret="lqJWRtCsSpItRv9sL5fm-YSeZPJgLcK5Lj6n1U-0QDE"
    r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8c60b4408fc42f94&corpsecret=lqJWRtCsSpItRv9sL5fm-YSeZPJgLcK5Lj6n1U-0QDE")
    # print(r.text)
    print(r.json()["access_token"])
    