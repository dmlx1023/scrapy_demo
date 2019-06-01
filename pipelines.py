# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class SpirderxxooPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagesrenamePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        str = request.url
        fileName = str.split('/')[-3:len(str)]
        dir = 'F:\spider_down\image'
        folder = request.meta['item']['folder']
        pathprefx = dir + os.sep + folder
        path = pathprefx + os.sep + ''.join(fileName)
        return path

    def get_media_requests(self, item, info):
        headers = {'Accept': 'image/png, image/svg+xml, image/*; q=0.8, */*; q=0.5',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                   'Cache-Control': 'max-age=0',
                   'Host': 'i.meizitu.net',
                   'Referer': 'https://www.mzitu.com',
                   # 'Referer': 'https://www.mzitu.com/180015/6',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

        yield scrapy.Request(item['url'], headers=headers, meta={'item': item})

    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, download_func, settings)
