import requests
from lxml import etree
from chaojiying import Chaojiying_Client
from PIL import Image
import matplotlib.pyplot as plt

# 获取登陆验证码的图片
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=https://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
session = requests.session()
html = session.get(url=login_url, headers=headers).text
tree = etree.HTML(html)
imgCodeUrl_part = tree.xpath('//*[@id="imgCode"]//@src')[0]
imgCodeUrl = 'https://so.gushiwen.cn'
imgCodeUrl += imgCodeUrl_part
imgCode = requests.get(url=imgCodeUrl, headers=headers).content
with open('img.jpg', 'wb') as f:
    f.write(imgCode)
# 展示验证码
img = Image.open('img.jpg')
plt.figure("img")
plt.imshow(img)
plt.show()

# 通过第三方API识别验证码
chaojiying = Chaojiying_Client('bluebell', 'ZH20010201', '928116')  # 用户中心>>软件ID 生成一个替换 96001
im = open('img.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg
yanzhengma = chaojiying.PostPic(im, 1902)['pic_str']
print('验证码识别结果为：{}'.format(yanzhengma))

# 通过session进行模拟登陆记录下session状态
login_url_index = 'https://so.gushiwen.cn/user/login.aspx?from=https://so.gushiwen.cn/user/collect.aspx'
request_header = {
    '__VIEWSTATE': 'gVYirCbslOQTQwrL8aiJT4pI+guQrbFS/skwSKxRWeeNIGK7m1YTXAa/rnTfvBdfK0qQh+2PK46duYQ8rTxGSjYO'
                   '/R69aqD6aFYrxWez5wlQwppnaEWcJy4Wn/4=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '1205946274@qq.com',
    'pwd': 'ZH20010201',
    'code': yanzhengma,
    'denglu': '登录'
}

response = session.post(url=login_url_index, headers=headers)
print('服务器状态为：{}'.format(response.status_code))

# 获取登陆之后的界面
url = 'https://so.gushiwen.cn/user/collect.aspx'
print(session.get(url=url, headers=headers).text)
