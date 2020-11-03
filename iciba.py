#
#    金山词霸每日一句 iciba.py
#

import re
import time
import datetime

import requests

def get_sentence(api): #获取金山词霸每日一句函数
    sentence = requests.get(api)
    return  sentence.json()

def every_day():
    icibaApi = 'http://open.iciba.com/dsapi'  # 每日一句接口地址
    sentence = get_sentence(icibaApi)
    # print(sentence) #测试返回值
    content = sentence['content'] #每日一句 原文
    note = sentence['note'] #每日一句 翻译短语
    dates = sentence['dateline']# 短语时间
    # print("'%s'\n\t%s ———— %s" % (content,note,dates)) #测试输出正常

    weeks = datetime.datetime.now()
    wk = weeks.weekday()

    week = wk+1
    # if week=='1':
    #     week = '星期一'
    # elif week=='2':
    #     week = '星期二'
    # elif week=='3':
    #     week = '星期三'
    # elif week=='4':
    #     week = '星期四'
    # elif week=='5':
    #     week = '星期五'
    # elif week=='6':
    #     week = '星期六'
    # elif week=='7':
    #     week = '星期日'
    # else:
    #     week ='没找到该星期'

    meassage = '''
    -------每日一句------------
    ' {} '\n\t
    ' {} '\n\t
    日期: {}  星期 {}
    ---------------------------
    '''.format(content, note, dates,week)
    # print(meassage)

    return meassage

# if __name__ == '__main__' :
#     every_day()
#     icibaApi = 'http://open.iciba.com/dsapi' #每日一句接口地址
#     sentence = get_sentence(icibaApi)
#     # print(sentence) #测试返回值
#     content = sentence['content'] #每日一句 英文短语
#     note = sentence['note'] #每日一句 翻译短语
#     dates = sentence['dateline']# 短语时间
#     print("'%s'\n\t%s ———— %s" % (content,note,dates)) #测试输出正常