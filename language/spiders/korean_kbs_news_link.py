# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime, timedelta
from ..items import KoreanNewsContentItem


class KoreanKbsNewsLinkSpider(scrapy.Spider):
    name = 'korean_kbs_news_link'
    allowed_domains = ['http://news.kbs.co.kr']
    # 第一类新闻
    urls = ['https://pbbsapi.kbs.co.kr/board/v1/list?bbs_id=T2003-0100-04-261151&page=8&page_size={}&notice_yn=N&kbs_board_auth=0'.format(i) for i in range(1, 370)]
    # start_urls = ['https://pbbsapi.kbs.co.kr/board/v1/list?bbs_id=T2003-0100-04-261151&page=8&page_size=10&notice_yn=N&kbs_board_auth=0']

    # 第二类新闻
    # start_urls = ['http://news.kbs.co.kr/news/list.do?mcd=0795#1']
    # 第三类新闻和第四和第二类新闻结构相同，mcd分别1033,0795 第二类是0933
    # 第五类新闻（体育新闻）以时间为参数, 和第二，三和四类似，但是参数不同
    start_urls = ['http://news.kbs.co.kr/sports/subMain.do']

    # 第六类新闻用了日期和列表

    def parse(self, response):
        # 第一类新闻
        # data = json.loads(response.body)
        # pages = data.get("data")
        # for page in pages:
        #     page_id = page.get("id")
        #     page_url = 'http://news.kbs.co.kr/news/view.do?ncd={}'.format(page_id)
        #     yield scrapy.Request(url=page_url, callback=self.parse_item, dont_filter=True)

        # 第二， 三和四类新闻，第二类新闻采用的是post接口
        # url = 'http://news.kbs.co.kr/news/getMenuNewsList.do'
        # for i in range(1, 146):
        #     payload = {
        #         "CURRENT_PAGE_NO": '{}'.format(i),
        #         "ROW_PER_PAGE": '12',
        #         "SEARCH_MENU_CODE": '0795'
        #     }
        #     yield scrapy.FormRequest(
        #         url=url,
        #         formdata=payload,
        #         callback=self.parse_page,
        #         dont_filter=True
        #     )

        # 第五类新闻
        for i in range(360):
            to_day = datetime.now()
            news_day = to_day - timedelta(days=i)
            payload = {
                "CURRENT_PAGE_NO": '1',
                "ROW_PER_PAGE": '12',
                "SEARCH_DATE": news_day.strftime("%Y%m%d"),
                "SEARCH_SECTION": '0002',
                "LAST_DATE": ''
            }
            url = 'http://news.kbs.co.kr/news/getContentsNewsList.do'
            req = scrapy.FormRequest(
                url=url,
                formdata=payload,
                callback=self.parse_page,
                dont_filter=True
            )
            req.meta['date_time'] = news_day.strftime("%Y%m%d")
            yield req

    def parse_page(self, response):
        page_content = json.loads(response.body.decode('utf8'))
        page_list = page_content.get("page_list")
        for page in page_list:
            news_code = page.get("NEWS_CODE")
            page_url = 'http://news.kbs.co.kr/news/view.do?ncd={}'.format(news_code)
            yield scrapy.Request(url=page_url, callback=self.parse_item, dont_filter=True)

        current_page = page_content.get("page_currentPageNo")
        page_total_size = page_content.get("page_totalSize")
        page_total = int(page_total_size) // 12 + 1
        if int(current_page) < page_total:
            print("-"*300)
            payload = {
                "CURRENT_PAGE_NO": '{}'.format(str(int(current_page)+1)),
                "ROW_PER_PAGE": '12',
                "SEARCH_DATE": response.meta["date_time"],
                "SEARCH_SECTION": '0002',
                "LAST_DATE": ''
            }
            url = 'http://news.kbs.co.kr/news/getContentsNewsList.do'
            req = scrapy.FormRequest(
                url=url,
                formdata=payload,
                callback=self.parse_page,
                dont_filter=True
            )
            req.meta['date_time'] = response.meta["date_time"]
            yield req

    def parse_item(self, response):
        page_content = response.xpath('//*[@id="cont_newstext"]//text()').extract()
        news_text = ' '.join(page_content)
        url = response.url
        item = KoreanNewsContentItem()
        item['url'] = url
        item['content'] = news_text
        yield item
