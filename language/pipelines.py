# -*- coding: utf-8 -*-

import hashlib
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
import redis
import requests
from pymongo import MongoClient


from .items import IndonesiaNewsContentItem, ShortWordLink, ImgLink, NewsLink
from .items import NewsLinkItem, NewsContentItem, TradeName, SongName, MovieName, KoreanNewsContentItem


class LanguagePipeline(object):
    def __init__(self):
        # 创建redis数据库连接
        pool = redis.ConnectionPool(host='47.105.132.57', port=6379, db=0, password='')
        self.r = redis.Redis(connection_pool=pool)

        # 创建mongodb库连接
        self.client = MongoClient("47.105.132.57:27017")

        # 连mysql接数据库
        self.connect = pymysql.connect(
            # host='123.56.11.156',  # 数据库地址
            # user='sjtUser',  # 数据库用户名
            # passwd='sjtUser!1234',  # 数据库密码
            # db='malaysia',  # 数据库名

            host='47.105.132.57',  # 数据库地址
            user='root',  # 数据库用户名
            passwd='Yang_123_456',  # 数据库密码
            db='spiderframe',  # 数据库名


            port=3306,  # 数据库端口
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 将数据写入数据库
        if isinstance(item, NewsLinkItem):
            md5_url = self.md5_(item['url'])
            sta = self.hash_exist(md5_url)
            if not sta:
                self.hash_(md5_url)
                self.r.lpush('news_link', item['url'])
                self.cursor.execute("""insert into news_link(category, url) value (%s, %s)""",
                                    (item['category'], item['url']))
                self.connect.commit()
            else:
                print("指纹重复")
        elif isinstance(item, NewsContentItem):
            if item['content']:
                # self.cursor.execute("""insert into vietnam_news_nhandan_content(url, content) value (%s, %s)""",
                #                     (item['url'], item['content']))
                # self.connect.commit()
                url_id = self.md5_(item['url'])
                item["id"] = url_id

                self.client.vietnam.vietnam_news_vtv_content.update({'id': item['id']}, item, True)

            else:
                # self.r.rpush(spider.name, item['url'])
                pass
        elif isinstance(item, TradeName):
            self.cursor.execute("""insert into vietnam_shopee_name(category, content) value (%s, %s)""",
                                (item['category'], item['content']))
            self.connect.commit()
        elif isinstance(item, SongName):
            self.cursor.execute("""insert into vietnam_song_name(song_name, singer_name) value (%s, %s)""",
                                (item['song_name'], item['singer_name']))
            self.connect.commit()
        elif isinstance(item, MovieName):
            self.cursor.execute("""insert into vietnam_movie_name(first_name, second_name) value (%s, %s)""",
                                (item['first_name'], item['second_name']))
            self.connect.commit()
        elif isinstance(item, KoreanNewsContentItem):
            md5_url = self.md5_(item['url'])
            sta = self.hash_exist(md5_url)
            if not sta:
                self.hash_(md5_url)
                self.cursor.execute("""insert into korean_news_text(news_link, news_text) value (%s, %s)""",
                                    (item['url'], item['content']))
                self.connect.commit()
            else:
                print("指纹重复")
        elif isinstance(item, IndonesiaNewsContentItem):
            db_name = 'indonesia_news_fingerprint'
            md5_url = self.md5_(item['url'])
            sta = self.hash_exist(db_name, md5_url)
            if not sta:
                self.hash_(db_name, md5_url)
                self.cursor.execute("""insert into indonesia_news_text(news_link, news_text) value (%s, %s)""",
                                    (item['url'], item['content']))
                self.connect.commit()
            else:
                print("指纹重复")
        elif isinstance(item, ShortWordLink):
            db_name = 'fingerprint'
            md5_url = self.md5_(item['url'])
            sta = self.hash_exist(db_name, md5_url)
            if not sta:
                self.hash_(db_name, md5_url)
                self.r.lpush('malaysia_goods_name', item['url'])
            else:
                print("指纹重复")
        elif isinstance(item, ImgLink):
            db_name = 'fingerprint'
            md5_url = self.md5_(item['url'])
            sta = self.hash_exist(db_name, md5_url)
            if not sta:
                self.hash_(db_name, md5_url)
                self.cursor.execute("""insert into Img(img_name, url) value (%s, %s)""",
                                    (md5_url, item['url']))
                self.connect.commit()

                content = requests.get(item["url"]).content

                folder = r"D:\datatang\language\language\files\car"
                if not os.path.exists(folder):
                    os.mkdir(folder)
                with open('{}\{}.jpg'.format(folder, md5_url), 'wb') as f:
                    f.write(content)
        elif isinstance(item, NewsLink):
            if not item.get("url"):
                self.r.lpush("link_error", item["ori_url"])
            else:
                db_name = 'fingerprint'
                md5_url = self.md5_(item['url'])
                sta = self.hash_exist(db_name, md5_url)
                if not sta:
                    self.hash_(db_name, md5_url)
                    self.r.rpush(spider.name, item['url'])
                else:
                    print("指纹重复")
        else:
            pass

        return item

    def md5_(self, str):
        md5 = hashlib.md5()
        data = str
        md5.update(data.encode('utf-8'))
        return md5.hexdigest()

    def hash_(self, db_name, str):
        return self.r.hset(name=db_name, key=str, value=1)

    def hash_exist(self, db_name, str):
        return self.r.hexists(name=db_name, key=str)
