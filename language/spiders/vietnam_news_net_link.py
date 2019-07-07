# -*- coding: utf-8 -*-
import scrapy
import pprint
import json
import re
from language.items import NewsLink


class VietnamNewsNetLinkSpider(scrapy.Spider):
    name = 'vietnam_news_net_link'
    allowed_domains = ['vietnamnet.vn']
    a = ['thoi-su', 'thoi-su-chong-tham-nhung', 'thoi-su-quoc-hoi', 'thoi-su-an-toan-giao-thong', 'thoi-su-moi-truong',
         'thoi-su-clip-nong', 'thoi-su-bhxh-bhyt', 'thoi-su-quoc-phong', 'kinh-doanh', 'kinh-doanh-tai-chinh',
         'kinh-doanh-dau-tu', 'kinh-doanh-thi-truong', 'kinh-doanh-doanh-nhan', 'kinh-doanh-tu-van-tai-chinh',
         'kinh-doanh-tieu-diem-bat-dong-san',
         ]
    b = ['giai-tri', 'giai-tri-the-gioi-sao', 'giai-tri-thoi-trang', 'giai-tri-nhac', 'giai-tri-phim',
         'giai-tri-truyen-hinh', 'giai-tri-sach', 'giai-tri-di-san-my-thuat-san-khau', 'the-gioi',
         'the-gioi-binh-luan-quoc-te', 'the-gioi-chan-dung', 'the-gioi-ho-so', 'the-gioi-the-gioi-do-day',
         'the-gioi-viet-nam-va-the-gioi', 'the-gioi-quan-su',
         ]
    c = ['giao-duc', 'giao-duc-nguoi-thay', 'giao-duc-tuyen-sinh', 'giao-duc-du-hoc', 'giao-duc-guong-mat-tre',
         'giao-duc-goc-phu-huynh', 'giao-duc-hoc-tieng-anh', 'giao-duc-khoa-hoc', 'doi-song', 'doi-song-gia-dinh',
         'doi-song-song-la', 'doi-song-gioi-tre', 'doi-song-tam-su', 'doi-song-me-va-be', 'doi-song-du-lich',
         'doi-song-am-thuc', 'doi-song-meo-vat',
         ]
    d = ['phap-luat', 'phap-luat-ho-so-vu-an', 'phap-luat-ky-su-phap-dinh', 'phap-luat-tu-van-phap-luat', 'the-thao',
         'the-thao-bong-da-viet-nam', 'the-thao-bong-da-quoc-te', 'the-thao-hau-truong', 'the-thao-cac-mon-khac',
         'the-thao-xem-truc-tiep-bong-da',
         ]
    e = ['cong-nghe', 'cong-nghe-cong-dong-mang', 'cong-nghe-san-pham', 'cong-nghe-ung-dung', 'cong-nghe-tin-cong-nghe',
         'cong-nghe-vien-thong', 'cong-nghe-bao-mat', 'thong-tin-truyen-thong', 'suc-khoe', 'suc-khoe-suc-khoe-24h',
         'suc-khoe-lam-dep', 'suc-khoe-cac-loai-benh', 'suc-khoe-tu-van-suc-khoe',
         ]
    f = ['bat-dong-san', 'bat-dong-san-du-an', 'bat-dong-san-noi-that', 'bat-dong-san-kinh-nghiem-tu-van',
         'bat-dong-san-thi-truong', 'bat-dong-san-nha-dep', 'ban-doc', 'ban-doc-hoi-am', 'ban-doc-chia-se',
         'ban-doc-tho',
         'goc-nhin-thang', 'hotface', 'ban-tron-truc-tuyen', 'multimedia', 'tin-tuc-24h', 'tuanvietnam', 'oto-xe-may',
         'blog', 'thu-vien'
         ]
    s_c = ['talkshow', 'thoi-su', 'kinh-doanh', 'giai-tri', 'the-gioi', 'giao-duc', 'doi-song', 'phap-luat', 'the-thao',
         'cong-nghe', 'suc-khoe', 'bat-dong-san', 'ban-doc', 'tuanvietnam', 'oto-xe-may']

    start_urls = [
        # 'https://vietnamnet.vn/',
        # 'https://vietnamnet.vn/vn/thoi-su/chinh-tri/',
        # 'https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c=thoi-su-chinh-tri&p=1&s=15&a=5',
        'https://vietnamnet.vn/jsx/loadmore/?domain=desktop&c={}&p=1&s=15&a=5'.format(item) for item in b
    ]

    def parse(self, response):
        resp = response.text.replace("retvar =", '')
        data = json.loads(resp)
        if data:
            for news_item in data:
                news_link = news_item.get("link")
                if news_link:
                    item = NewsLink()
                    item['url'] = news_link
                    item['ori_url'] = response.url
                    yield item

            nest_page = int(re.findall('&p=(.*?)&', response.url)[0]) + 1
            nest_url = "&".join(response.url.split("&")[:2]) + '&p={}&s=15&a=5'.format(nest_page)
            yield scrapy.Request(url=nest_url, callback=self.parse, dont_filter=True)
