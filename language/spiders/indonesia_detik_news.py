# -*- coding: utf-8 -*-
import scrapy
import datetime
from ..items import IndonesiaNewsContentItem


class IndonesiaDetikNewsSpider(scrapy.Spider):
    name = 'indonesia_detik_news'
    allowed_domains = ['https://news.detik.com']
    now_time = datetime.datetime.now()
    urls = []

    for i in range(1*365):
        news_time = now_time - datetime.timedelta(days=i)
        urls.append("https://sport.detik.com/sepakbola/indeks?date={}/{}/{}".format(news_time.strftime('%m'), news_time.day,
                                                                         news_time.year))
    start_urls = urls
    # start_urls = ['https://news.detik.com/indeks/all?date=04/22/2019']
    # 第二类新闻，类型同第一种，以日期为参数
    # start_urls = ['https://finance.detik.com/indeks?date=04/10/2019']
    # 第四类新闻
    # start_urls = ['https://inet.detik.com/main/indeks?date=04/26/2019']
    # 第五类型GET
    # start_urls = ['https://sport.detik.com/indeks?date=04/09/2019']
    # 第六类型GET
    # start_urls = ['https://oto.detik.com/indeks?date=04/09/2019']
    # 第八类型GET
    # start_urls = ['https://sport.detik.com/sepakbola/indeks?date=04%2F16%2F2019']
    # 第九类型GET
    # start_urls = ['https://food.detik.com/detikfood/indeks?date=04%2F09%2F2019']
    # start_urls = ['https://health.detik.com/detikhealth/indeks?date=04%2F09%2F2019']
    # start_urls = ['https://wolipop.detik.com/indeks?date=04%2F10%2F2019']

    # 第三类新闻，post 请求，
    # def start_requests(self):
    #     url = 'https://hot.detik.com/indeks?_ga=2.240846528.2143120600.1556156724-1537197453.1555930518'
    #     now_time = datetime.datetime.now()
    #     for i in range(3):
    #         news_time = now_time - datetime.timedelta(days=i)
    #         formdata = {"datepick": "{}/{}/{}".format(news_time.strftime('%m'), news_time.day, news_time.year)}
    #         yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.parse)

    def parse(self, response):
        # links = response.xpath('//*[@id="indeks-container"]/li/article/div/a/@href').extract()
        links = response.xpath('//div[@class="desc_idx ml10"]//a/@href').extract()
        for url in links:
            yield scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        news_content = response.xpath('//*[@id="detikdetailtext"]//text()').extract()
        news_text = ''.join(news_content)
        url = response.url
        item = IndonesiaNewsContentItem()
        item["url"] = url
        item["content"] = news_text
        yield item
