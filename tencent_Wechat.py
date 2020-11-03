#coding=utf-8
# import optparse
# import time
# import apiutil1  # 这里我上端代码独立生成一个文件“apiutil.py"，所以要导入一下
# import json
#
# app_key = 'KoXxoQpG1WzrDVJJ'
# app_id = '2159423472'
# questionS = '在吗999？'
#
# def anso(questionS):
#     str_question = questionS
#     session = 10000
#     ai_obj = apiutil1.AiPlat(app_id, app_key)
#
#     rsp = ai_obj.getNlpTextChat(session, str_question)
#     if rsp['ret'] == 0:
#         print('............................................................')
#         ask = (rsp['data'])['answer']
#         print(ask)
#     else:
#         print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
#
#
# if __name__ == '__main__':
#     anso(questionS)
#


import apiutil1
import json

def get_response(questionS): #AI回复信息
    app_id = 'XXXXX'
    app_key = 'XXXXX'

    str_question = questionS #传参
    session = 10000

    ai_obj = apiutil1.AiPlat(app_id,app_key) #调用SDK AiPlat()方法
    rsp = ai_obj.getNlpTextChat(session,str_question)#调用SDK方法

    def rsps(): #需要被调用反馈信息的函数
        if rsp['ret'] == 0: #判断参数问题,并反馈信息
            ask = (rsp['data'])['answer']
            print("ask========")

            return ask
        else:
            print(json.dumps(rsp, ensure_ascii=False, sort_keys=False, indent=4))
            print('else========')

    return (rsps)





