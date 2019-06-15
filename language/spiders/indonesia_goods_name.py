# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
import re

class IndonesiaGoodsNameSpider(RedisSpider):
    name = 'indonesia_goods_name'
    allowed_domains = ['www.tokopedia.com']
    start_urls = ['https://www.tokopedia.com/p/buku/buku-remaja-dan-anak/dunia-pengetahuan']
    redis_key = 'indonesia_goods_name'
    custom_settings = {
        # 指定redis数据库的连接参数
        'REDIS_HOST': '123.56.11.156',
        'REDIS_PORT': 6379,
        # 指定 redis链接密码，和使用哪一个数据库
        'REDIS_PARAMS': {
            'password': '',
            'db': 0
        },
    }

    def parse(self, response):
        names = response.xpath('//*[@id="search-result"]/div[2]/div[4]/div/div/div/a/div[2]/h3/text()').extract()
        self.save(names)
        print(names)

        # next_link = response.xpath('//*[@id="search-result"]/div[2]/div[5]/span[8]/span/a/@href').extract()
        # if next_link:
        #     url = 'http://www.tokopedia.com' + next_link[0]
        #     page = re.findall("page=(.*?)&", url)[0]
        #     if int(page) < 6:
        #         yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_goods_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))
