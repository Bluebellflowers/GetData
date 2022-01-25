import requests

star = 0
limit = 100
get_url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start={}&limit={}'.format(star,
                                                                                                                  limit)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
respose = requests.get(url=get_url, headers=headers)
name = []
for data in respose.json():
    name.append(data['title'])
print(name)
