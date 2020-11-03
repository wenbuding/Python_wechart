#
#   聚合数据 API获取 天气情况函数 weather.py
#
import requests

def get_weather_forcast(citys): #聚合数据 API获取 天气情况函数

    apikey = '81e6caaf8a8da9cd43aa27d13fe803a1'
    url = 'http://v.juhe.cn/weather/index?format=2&cityname='+citys+'&key=' + apikey
    weather_forcast = requests.get(url).json()

    return weather_forcast #返回抓取数据

def weathers(cits):
    # 调用 天气函数
    weather_forcast = get_weather_forcast(cits)
    # print(weather_forcast)
    # 获取今日天气所有情况
    toDay_weather = weather_forcast['result']['today']
    # 获取天气的城市
    city = toDay_weather['city']
    # 今日时间
    date_y = toDay_weather['date_y']
    # 获取今日天气
    weather = toDay_weather['weather']
    # 获取今日气温
    temperature = toDay_weather['temperature']
    # 今日风向
    wind = toDay_weather['wind']
    # 今日穿衣指数
    dressing_index = toDay_weather['dressing_index']
    # 今日穿衣建议
    dressing_advice = toDay_weather['dressing_advice']

    # 打印排版
    meassage = '''城市: {} \n时间: {} \n天气: {} \n气温: {} \n风向: {} \n穿衣指数: {} \n穿衣建议: {}
                '''.format(city, date_y, weather, temperature, wind, dressing_index, dressing_advice)
    print(meassage)

if __name__ == '__main__' :
    weathers('北京')
    # # 调用 天气函数
    # weather_forcast = get_weather_forcast('北京')
    # # 获取今日天气所有情况
    # toDay_weather = weather_forcast['result']['today']
    # # 获取天气的城市
    # city = toDay_weather['city']
    # # 今日时间
    # date_y = toDay_weather['date_y']
    # # 获取今日天气
    # weather = toDay_weather['weather']
    # # 获取今日气温
    # temperature = toDay_weather['temperature']
    # # 今日风向
    # wind = toDay_weather['wind']
    # # 今日穿衣指数
    # dressing_index = toDay_weather['dressing_index']
    # #今日穿衣建议
    # dressing_advice = toDay_weather['dressing_advice']
    #
    #
    # #打印排版
    # meassage =  '''
    #             城市: {}
    #             时间: {}
    #             天气: {}
    #             气温: {}
    #             风向: {}
    #             穿衣指数: {}
    #             穿衣建议: {}
    #             '''.format(city,date_y,weather,temperature,wind,dressing_index,dressing_advice)
    # print(meassage)
