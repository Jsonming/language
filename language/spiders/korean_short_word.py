# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_redis.spiders import RedisSpider


class KoreanShortWordSpider(RedisSpider):
    name = 'korean_short_word'
    allowed_domains = ['http://kr.tingroom.com']
    # start_urls = [
    #     'http://kr.tingroom.com/hych/ytybhydc/49943.html',
    #     "http://kr.tingroom.com/hych/hyshch/48660.html",
    #     "http://kr.tingroom.com/hych/hyjsjch/6965.html",
    #     "http://kr.tingroom.com/hych/swhych/47458.html",
    #     "http://kr.tingroom.com/hych/syhych/50080.html",
    #     "http://kr.tingroom.com/hych/TOPIKch/50658.html",
    #     "http://kr.tingroom.com/hych/fkhych/51058.html",
    # "http://kr.tingroom.com/hych/zhuanyech/49647.html",
    # "http://kr.tingroom.com/hych/huoyonghanyuxuehanyu/48673.html",
    # "http://kr.tingroom.com/hych/hanyuguanyongyu/25864.html",
    # "http://kr.tingroom.com/hych/hanguogequjiexi/27507.html"
    # ]

    redis_key = 'korean_short_word'
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
        # print(response.body)
        match = re.compile("[\uac00-\ud7ff]+|[\uAC00-\uD7A3]+")
        article = response.xpath('//div[@id="article"]//text()').extract()
        text = []
        for line in article:
            line = match.findall(line)
            if line:
                line = ' '.join(line)
                if len(line.replace(" ", '')) < 6:
                    text.append(line)
                    print(line)

        with open(r"C:\Users\Administrator\Desktop\korean_short_word.txt", 'a', encoding='utf8') as f:
            f.write('\n'.join(text))
