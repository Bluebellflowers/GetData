import requests

# 注意是使用的post请求来交换数据的
post_url = 'https://fanyi.baidu.com/sug'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
data = {'kw': 'dog'}
respose = requests.post(url=post_url, data=data, headers=headers)
print(respose.json())
