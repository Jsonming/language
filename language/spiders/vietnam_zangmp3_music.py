# -*- coding: utf-8 -*-
import scrapy
import json
import execjs
import time
from lxml import etree
from ..items import SongName

class VietnamZangmp3MusicSpider(scrapy.Spider):
    name = 'vietnam_zangmp3_music'
    allowed_domains = ['https://zingmp3.vn']
    start_urls = [
        # 'https://zingmp3.vn/api/top100?ctime=1555498717&sig=92720941d3dd02c54ea574b24f920586456535ab30d5bfae92686ce8b634c4b7c99a01a6a542e7ef82e34cf38411f9644672b0efd0e5a9cabae197a45046d6ad&api_key=38e8643fb0dc04e8d65b99994d3dafff',
        'https://zingmp3.vn/api/topic/get-group?ctime=1555570646&sig=553528840fb41a2a3ff4efc015ecaba8eb13ae85c98b7fd44c89425fb52e73fd56a48cd97f1df85cd821b050c5d98c3f8953a8cd43e5231cddb8db16d752d284&api_key=38e8643fb0dc04e8d65b99994d3dafff'
    ]

    def parse(self, response):
        page_url = "https://zingmp3.vn"
        req_url = response.url
        req_url_type = req_url.split("?")[0].split("/")[-1]
        if 'top100' in req_url_type:
            data = json.loads(response.body).get("data")
            for genre in data:
                items = genre.get("items")
                for item in items:
                    short_link = item.get("link")
                    link = page_url + short_link
                    yield scrapy.Request(url=link, callback=self.parse_items, dont_filter=True)
        elif 'get-group' in req_url_type:
            data = json.loads(response.body).get("data")
            for genre in data:
                childs = genre.get("childs")
                for child in childs:
                    short_link = child.get("link")
                    link_id = short_link.split('.')[0].split('/')[-1]
                    link = "https://zingmp3.vn/api/playlist/get-playlist-detail?id={}&ctime={}&sig=fa0092f4752f5d631383ce528b9ee85b4b37981c9e1deccdf9ff2be21fc426b1ee8ff6ba7254c9190c4d687f0a3d991e21f5cf92596e35ba6872f65b122343cc&api_key=38e8643fb0dc04e8d65b99994d3dafff".format(link_id, str(int(time.time())))
                    yield scrapy.Request(url=link, callback=self.parse_items, dont_filter=True)
        else:
            pass

    def parse_items(self, response):
        req_url = response.url
        if '100' in req_url:
            root = etree.HTML(response.body)
            data_json_string = root.xpath('//script[@type="application/ld+json"]/text()')[0]
            data = execjs.eval(data_json_string)
            itemListElement = data.get("track").get("itemListElement")
            if itemListElement:
                for element in itemListElement:
                    if element:
                        item = element.get("item")
                        if item:
                            song_name = item.get("name")
                            artist = item.get("byArtist")
                            if artist:
                                singer_name = ','.join([art.get("name") for art in artist if art])
                                item = SongName()
                                item["singer_name"] = singer_name
                                item["song_name"] = song_name
                                yield item
        elif 'detail' in req_url:
            print(response.body)
