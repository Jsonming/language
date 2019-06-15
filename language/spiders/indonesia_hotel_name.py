# -*- coding: utf-8 -*-
import scrapy


class IndonesiaHotelNameSpider(scrapy.Spider):
    name = 'indonesia_hotel_name'
    allowed_domains = ['www.traveloka.com/hotel']
    start_urls = ['https://www.traveloka.com/hotel/indonesia?id=2760098057401446760&adloc=id-id&kw=2760098057401446760_hotel%20indonesia&gmt=e&gn=g&gd=c&gdm=&gcid=326489323410&gdp=&gdt=&gap=1t1&pc=1&cp=2760098057401446760_HLO100003-COM-D-s_2760098057401446760_100003-H&aid=65738320072&wid=aud-308616686859:kwd-186689356&fid=&gid=9056704&kid=_k_Cj0KCQjw5J_mBRDVARIsAGqGLZD0veehJfszPKcY9eR4Y0T7xhIQALcVA1QdiDoXeUFCGtweMdvyWKgaAqFeEALw_wcB_k_&gclid=Cj0KCQjw5J_mBRDVARIsAGqGLZD0veehJfszPKcY9eR4Y0T7xhIQALcVA1QdiDoXeUFCGtweMdvyWKgaAqFeEALw_wcBhttps://www.traveloka.com/hotel/indonesia?id=2760098057401446760&adloc=id-id&kw=2760098057401446760_hotel%20indonesia&gmt=e&gn=g&gd=c&gdm=&gcid=326489323410&gdp=&gdt=&gap=1t1&pc=1&cp=2760098057401446760_HLO100003-COM-D-s_2760098057401446760_100003-H&aid=65738320072&wid=aud-308616686859:kwd-186689356&fid=&gid=9056704&kid=_k_Cj0KCQjw5J_mBRDVARIsAGqGLZD0veehJfszPKcY9eR4Y0T7xhIQALcVA1QdiDoXeUFCGtweMdvyWKgaAqFeEALw_wcB_k_&gclid=Cj0KCQjw5J_mBRDVARIsAGqGLZD0veehJfszPKcY9eR4Y0T7xhIQALcVA1QdiDoXeUFCGtweMdvyWKgaAqFeEALw_wcB']

    def parse(self, response):
        names = response.xpath('//*[@id="popularHotelList"]/div/div[2]/div/div[1]/h3/a/text()').extract()
        self.save(names)
        print(names)

        links = response.xpath('//*[@id="container"]/div[3]/div[4]/div[1]/div[3]/p/a/@href').extract()
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse, dont_filter=True)

    def save(self, result):
        with open(r'C:\Users\Administrator\Desktop\indonesia_temp\indonesia_hotel_name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

