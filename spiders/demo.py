# -*- coding:utf-8 -*-
# author:blog.zycat.top
# datetime:2019/5/28 12:54
# software: PyCharm
import os

import requests

def run():
    headers={'Accept': 'image/png, image/svg+xml, image/*; q=0.8, */*; q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
'Cache-Control': 'max-age=0',
'Host': 'i.meizitu.net',
'Referer': 'https://www.mzitu.com',
# 'Referer': 'https://www.mzitu.com/180015/6',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    # url='https://avatar.csdn.net/3/3/F/3_danielzhou888.jpg'
    url='https://i.meizitu.net/2019/04/15b06.jpg'
    r=requests.get(url,headers=headers)
    print(r.status_code)
    file= filename = os.getcwd() + os.sep + 'bizhi.jpg'
    with open(file, 'wb') as f:
        f.write(r.content)

    print('下载完成')
if __name__ == '__main__':
    run()