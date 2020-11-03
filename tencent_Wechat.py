#
#   腾讯AI 平台机器自动回复信息 tencent_Wechat.py
#
import os
import sys
sys.path.append('./SDK') #导入腾讯AI开放平台SDK
import apiutils
import apiutil

import optparse
import requests
import datetime
import time
import json

def get_response(questionS): #AI回复信息
#    app_id = 'XXXXXX' #控制台应用 APP ID
#    app_key = 'XXXXXX' #控制台 应用APP Key

    app_id = 'XXXXX'
    app_key = 'XXXXX'

    str_question = questionS #传参
    session = 10000

    ai_obj = apiutil.AiPlat(app_id,app_key) #调用SDK AiPlat()方法
    rsp = ai_obj.getNlpTextChat(session,str_question)#调用SDK方法

    def rsps(): #需要被调用反馈信息的函数
        if rsp['ret'] == 0: #判断参数问题,并反馈信息
            ask = (rsp['data'])['answer']

            return ask
        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))

    return (rsps)




