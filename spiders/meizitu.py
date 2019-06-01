# -*- coding: utf-8 -*-
import os

import scrapy

from spirderxxoo.items import MeizituItem


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    start_urls = ['https://www.mzitu.com/xinggan/page/{}/'.format(str(i)) for i in range(2,10)]
    # start_urls = ['https://www.mzitu.com/xinggan/']

    # allowed_domains = ['www.mzitu.com']

    def detail_page(self, response):
        url = response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/@href').extract()[0][:-1]
        nums = response.xpath('/html/body/div[2]/div[1]/div[4]/a[5]/span/text()').extract()[0]
        item = response.meta['item']
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
        }
        for i in range(1, int(nums) + 1):
            img_url = url + str(i)
            yield scrapy.Request(url=img_url, callback=self.get_url, meta={'url': url, 'nums': nums, 'item': item})

    @classmethod
    def get_url(self, response):
        item = response.meta['item']
        img_url = response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract()[0]
        item['url'] = img_url
        item['name'] = img_url.split('/')[-1]
        yield item

    def parse(self, response):
        imgurls = response.xpath('//*[@id="pins"]/li/a/@href').extract()
        folder = response.xpath('//*[@id="pins"]/li/a/img/@alt').extract()

        for url, name in zip(imgurls, folder):
            item = MeizituItem()
            item['folder'] = name
            yield scrapy.Request(url=url, callback=self.detail_page, meta={'item': item})


if __name__ == '__main__':
    from scrapy import cmdline, Request

    args = "scrapy crawl meizitu".split()
    cmdline.execute(args)
