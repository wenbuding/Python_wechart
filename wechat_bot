import itchat
import json
from turtle import clear
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
def get_response(questionS): #AI回复信息
    SecretId = 'XXXXXXX'
    SecretKey = 'XXXXXXX'
    try:
        cred = credential.Credential(SecretId, SecretKey)
        #cred = credential.Credential("SecretId", "SecretKey")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.ChatBotRequest()
        params = {
            "Query": questionS
        }
        req.from_json_string(json.dumps(params))
        
        resp = client.ChatBot(req)
        print(resp.to_json_string())
        j = json.loads(resp.to_json_string())
        return [j['Reply']]
    except TencentCloudSDKException as err:
        print(err)

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['Type'] == 'Text':
        # print(msg.NickName,msg.Text)
        answer = ''.join(get_response(msg['Content']))
    return answer
   
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
