# -*- coding:utf-8 -*-
# author:blog.zycat.top
# datetime:2019/6/7 17:23
# software: PyCharm
import os

import requests
from lxml import etree
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_index_m3u8(url):
    base = url.split('index.m3u8')[0]
    r = requests.get(url=url)
    print(bytes.decode(r.content))
    content = bytes.decode(r.content)
    l = content.split('\n')
    urls = [k for k in l if k.endswith('.ts')]
    return base, urls


def down_video(base_path, base, urls):
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for url in urls:
        r = requests.get(base + url, stream=True, verify=False)
        path = base_path + url
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(url + '下载完成')


def merge_video(base_path):
    shell_str='copy /b '+base_path+'\*.ts '+ base_path+'\\'+'new.mp4'
    print(shell_str)
    r=os.system(shell_str)
    if r==0:
        del_str = 'del/f/s/q ' + base_path + "\*.ts"
        os.system(del_str)

if __name__ == '__main__':
    # 视频根目录
    base_path = 'F:\spider_down\\video'
    # index地址
    url = 'https://www.sdfdfgfdtrd.space/cheng/gc975/500kb/hls/index.m3u8'
    # base, urls = get_index_m3u8(url)
    # down_video(base_path, base, urls)
    # 合并
    # merge_video(base_path)