# -*- coding:utf-8 -*-
# author:blog.zycat.top
# datetime:2019/5/27 20:40
# software: PyCharm
import os

import scrapy


class spider(scrapy.Spider):
    name = "spider_name"

    def start_requests(self):
        # urls = ['http://lab.scrapyd.cn/page/{}/'.format(str(i)) for i in range(1, 3)]
        # for url in urls:
        yield scrapy.Request(url='www.baidu.com', callback=self.parse)

    def parse(self, response):
        l = response.xpath('//*[@id="main-table"]/tbody/*/td[3]/a/text()')
        filename = os.getcwd() + os.sep + 'a.txt'
        with open(filename, 'wb') as f:
            f.write(l)
        self.log('保存文件: %s' % filename)


if __name__ == '__main__':
    from scrapy import cmdline

    args = "scrapy crawl spider_name".split()
    cmdline.execute(args)
