#
#    金山词霸每日一句 iciba.py
#


import requests

def get_sentence(api): #获取金山词霸每日一句函数
    sentence = requests.get(api)
    return  sentence.json()


if __name__ == '__main__' :

    icibaApi = 'http://open.iciba.com/dsapi' #每日一句接口地址
    sentence = get_sentence(icibaApi)
    # print(sentence) #测试返回值
    content = sentence['content'] #每日一句 英文短语
    note = sentence['note'] #每日一句 翻译短语
    dates = sentence['dateline']# 短语时间
    print("'%s'\n\t%s ———— %s" % (content,note,dates)) #测试输出正常