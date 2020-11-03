
import os
import sys
sys.path.append('./SDK') #导入腾讯AI开放平台SDK
import apiutil

import optparse
import requests
import datetime
import time
import json
#################################

import itchat
from itchat.content import *
# import tencent_Wechat
from functools import reduce

############################

def get_response(questionS): #AI回复信息

    app_id = 'XXXX' #控制台应用 APP ID
    app_key = 'XXXX' #控制台 应用APP Key

    str_question = questionS #传参
    session = 10000

    ai_obj = apiutil.AiPlat(app_id,app_key) #调用SDK AiPlat()方法
    rsp = ai_obj.getNlpTextChat(session,str_question)#调用SDK方法
    def ress():
        if rsp['ret'] == 0: #判断参数问题,并反馈信息
            ask = (rsp['data'])['answer']

            return ask
            # print(ask)

        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))

    return (ress)

#######################
# @itchat.msg_register(TEXT,isFriendChat=True)
# def text_reply(msg):
#     receive_the_messages = msg['Content']
#     # itchat.send_msg(get_response(receive_the_messages),toUserName=msg['FromUserName'])
#
#     return get_response(receive_the_messages)

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    if msg['Type'] == TEXT:
        # itchat.send_msg(get_response(msg['Content']))
        receive_the_messages = get_response(msg['Content'])

        # itchat.send_msg(receive_the_messages())
        # itchat.send_msg(get_response(msg['Content']), toUserName=msg['FromUserName'])
        # return get_response(msg['Content'])
        return receive_the_messages()
    else:
        print('Sorry! 暂时只处理文本!')


if __name__ == '__main__':

    # users = itchat.search_friends('13l')
    # userName = users[0]['UserName']
    itchat.auto_login(hotReload=True)
    itchat.run()
    # s = get_response('你好')
    # s()