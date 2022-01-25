from time import sleep

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
allpage_url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
re = requests.get(url=allpage_url, headers=headers).content
bs = BeautifulSoup(re, 'lxml')
# allpage=bs.find('div',class_='book-mulu').findAll('a')
# with open('sanguoyanyi_title.txt','w',encoding='utf-8') as f:
#     for _ in allpage:
#         f.write(_.string)
# print('ok!!!!')
# 获取每一回的标题和该回具体内容的跳转url
title = []
title_list = bs.select('.book-mulu a')
for _ in title_list:
    title.append(_.text)
# 获取每一回的具体内容
f = open('三国演义爬取结果.txt', 'w', encoding='utf-8')
for page in range(1, 121):
    url = 'https://www.shicimingju.com/book/sanguoyanyi/{}.html'.format(page)
    re1 = requests.get(url=url, headers=headers).content
    bs1 = BeautifulSoup(re1, 'lxml')
    text = bs1.find('div', class_='chapter_content')
    f.write(text.text + '\n')
    # sleep(2)
    print('爬取第{}回成功！！'.format(page))
f.close()
