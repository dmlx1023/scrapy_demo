# -*- coding: utf-8 -*-
import scrapy

from spirderxxoo.items import MeizituItem


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://i.meizitu.net/2019/04/15b06.jpg']
    headers = {'Accept': 'image/png, image/svg+xml, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
               'Cache-Control': 'max-age=0',
               'Host': 'i.meizitu.net',
               'Referer': 'https://www.mzitu.com',
               # 'Referer': 'https://www.mzitu.com/180015/6',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}

    def start_requests(self):
        yield scrapy.Request(url='https://i.meizitu.net/2019/04/15b06.jpg',headers=self.headers,callback=self.parse)

    def parse(self, response):
        item=MeizituItem()
        item['url']='https://i.meizitu.net/2019/04/15b06.jpg'
        yield item

if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl video".split()
    cmdline.execute(args)