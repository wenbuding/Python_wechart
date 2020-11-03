#coding=utf-8
import itchat
from tencent_WeChat import get_response
from iciba import every_day

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    receive_the_messages = get_response(msg['Content'])

    # 用于判断 关键字
    weather = msg['Content']  # 接受 天气关键词
    citys = msg['Content']  # 接受 天气 城市关键词
    iciba = msg['Content']  # 接受 每日一句关键词
    names = msg['Content']  # 接受 你是谁等 关键字
    name = msg['Content']  # 回答自己名字
    # city = citys
    if weather == '天气':
        return '您想查询哪个城市?'
    # elif citys == city:
    #     return receive_the_messages()
    elif iciba == '每日一句':
        iciba = every_day()
        return iciba
    elif names == '你叫什么' or names == '你叫什么？' or names == '你叫什么?' or names == '你是谁':
        names = '你好呀!我叫小埔!'
        return names
    elif name == '小埔' or name == '小哥哥':
        name = '你好呀! 小姐姐 在的'
        return name
    else:
        return receive_the_messages()

itchat.auto_login(hotReload=True)
itchat.run()
