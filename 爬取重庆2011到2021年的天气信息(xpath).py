import requests
from lxml import etree
from bs4 import BeautifulSoup
from time import sleep
import random
import matplotlib.pyplot as plt

# 拼接日期列表
years = [i for i in range(2011, 2022)]
mouth_size = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# for i in range(1,mouth_number+1):
#     if i==4:

#     if mouth_size[i]:

# 时间序列数据应为三维张量，即年(22),日(365)，气温(1)


init_url = 'https://lishi.tianqi.com/chongqing/{}.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}

# 储存所有年份的
weather = {}
"""
    weather的数据结构是一个嵌套的字典
"""
f = open('爬取天气结果.txt', 'w', encoding='utf-8')
for year in years:
    # 储存每一年的
    each_year = {}
    # 写入
    f.write(str(year) + '\n')
    for month in months:
        url = init_url.format(str(year) + month)
        html = requests.get(url=url, headers=headers).content
        tree = etree.HTML(html)
        data_max_t = tree.xpath('//div[@class="tian_three"]//li/div[2]/text()')
        data_min_t = tree.xpath('//div[@class="tian_three"]//li/div[3]/text()')
        # 储存每个月的最高最低温度
        monthly_data = {}
        # 利用正则表达式提取字符串中的数字
        import re

        for index, _ in enumerate(data_max_t):
            data_max_t[index] = int(re.findall('\d+', _)[0])
        for index, _ in enumerate(data_min_t):
            data_min_t[index] = int(re.findall('\d+', _)[0])
        # print(data_max_t,'\n',data_min_t)
        # 写入
        f.write(str(month) + '月   ' + '最高气温：' + str(data_max_t) + ',' + '最低气温：' + str(data_min_t) + '\n')
        monthly_data['max'] = data_max_t
        monthly_data['min'] = data_min_t
        # print(monthly_data)
        each_year[str(month)] = monthly_data
        print('成功爬取{}月！'.format(month))
        sleep(random.random() * 2)
    f.write('\n')
    weather[str(year)] = each_year
    print('爬取第{}年天气数据成功！！！'.format(year))
f.close()
print('爬取成功！！')


def get_all_t(weather, which):
    temperature = []
    for year in weather.keys():
        for month in weather[year].keys():
            temperature.extend(weather[year][month][which])
    return temperature


print('开始绘制温度变化曲线图：###########################################')
max_t = get_all_t(weather, 'max')
min_t = get_all_t(weather, 'min')

x = [i for i in range(len(max_t))]
plt.figure()
plt.plot(x, max_t, label='max temperature')  # Plot some data on the (implicit) axes.
plt.plot(x, min_t, label='min temperature')  # etc.
plt.xlabel('number/day')
plt.ylabel('temperature/℃')
plt.title("The weather change curve of Chongqing in recent 20 years")
plt.legend();
plt.show()
print('绘制成功！')
