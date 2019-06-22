# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LanguageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsLinkItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()


class NewsContentItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()


class KoreanNewsContentItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()


class IndonesiaNewsContentItem(scrapy.Item):
    url = scrapy.Field()
    content = scrapy.Field()


class TradeName(scrapy.Item):
    category = scrapy.Field()
    content = scrapy.Field()


class SongName(scrapy.Item):
    singer_name = scrapy.Field()
    song_name = scrapy.Field()


class MovieName(scrapy.Item):
    first_name = scrapy.Field()
    second_name = scrapy.Field()


class ShortWordLink(scrapy.Item):
    url = scrapy.Field()


class ImgLink(scrapy.Item):
    url = scrapy.Field()


class NewsLink(scrapy.Item):
    url = scrapy.Field()
    ori_url = scrapy.Field()
