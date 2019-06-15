# -*- coding: utf-8 -*-
import scrapy
from ..items import NewsLinkItem


class UtusanNewsLinkSpider(scrapy.Spider):
    name = 'utusan_news_link'
    allowed_domains = ['www.utusan.com.my']
    start_urls = ['http://www.utusan.com.my/berita/terkini',
                  'http://www.utusan.com.my/berita/jenayah'
                  "http://www.utusan.com.my/berita/utama",
                  "http://www.utusan.com.my/berita/nasional",
                  "http://www.utusan.com.my/berita/wilayah",
                  "http://www.utusan.com.my/berita/luar-negara",
                  "http://www.utusan.com.my/berita/politik",
                  "http://www.utusan.com.my/berita/parlimen",
                  "http://www.utusan.com.my/berita/jenayah",
                  "http://www.utusan.com.my/berita/nahas-bencana",
                  "http://www.utusan.com.my/berita/mahkamah",
                  "http://www.utusan.com.my/rencana/utama",
                  "http://www.utusan.com.my/rencana/bisik-bisik",
                  "http://www.utusan.com.my/rencana/selak",
                  "http://www.utusan.com.my/rencana/cuit",
                  "http://www.utusan.com.my/rencana/forum",
                  "http://www.utusan.com.my/rencana/agama",
                  "http://www.utusan.com.my/rencana/blog",
                  "http://www.utusan.com.my/rencana/sukan",
                  "http://www.utusan.com.my/hiburan/berita",
                  "http://www.utusan.com.my/hiburan/selebriti",
                  "http://www.utusan.com.my/hiburan/muzik",
                  "http://www.utusan.com.my/hiburan/filem-drama",
                  "http://www.utusan.com.my/hiburan/rancangan_tv",
                  "http://www.utusan.com.my/hiburan/seni-budaya",
                  "http://www.utusan.com.my/bisnes/ekonomi",
                  "http://www.utusan.com.my/bisnes/korporat",
                  "http://www.utusan.com.my/bisnes/siaran-akhbar",
                  "http://www.utusan.com.my/bisnes/usahawan",
                  "http://www.utusan.com.my/bisnes/automotif",
                  "http://www.utusan.com.my/bisnes/hartanah",
                  "http://www.utusan.com.my/bisnes/teknologi",
                  "http://www.utusan.com.my/bisnes/saham-wang",
                  "http://www.utusan.com.my/sukan/bola-sepak",
                  "http://www.utusan.com.my/sukan/badminton",
                  "http://www.utusan.com.my/sukan/lumba-kereta",
                  "http://www.utusan.com.my/sukan/lumba-motosikal",
                  "http://www.utusan.com.my/sukan/berbasikal",
                  "http://www.utusan.com.my/sukan/golf",
                  "http://www.utusan.com.my/sukan/hoki",
                  "http://www.utusan.com.my/sukan/lain-lain",
                  "http://www.utusan.com.my/sukan/rencana-sukan",
                  "http://www.utusan.com.my/mega/rona",
                  "http://www.utusan.com.my/mega/permotoran",
                  "http://www.utusan.com.my/mega/pelancongan",
                  "http://www.utusan.com.my/mega/rekreasi",
                  "http://www.utusan.com.my/mega/kesihatan",
                  ]

    def parse(self, response):
        req_url = response.url
        category = req_url.split('/')[-2]
        teasers = response.xpath('//li[@class="element_item item_teaser"]')
        for teaser in teasers:
            short_url = teaser.xpath('.//a/@href').extract()[0]
            url = 'http://www.utusan.com.my' + short_url
            item = NewsLinkItem()
            item['category'] = category
            item['url'] = url
            yield item
