# -*- coding: utf-8 -*-
import scrapy


class MalaysiaBookingStoresSpider(scrapy.Spider):
    name = 'malaysia_booking_stores'
    allowed_domains = ['www.booking.com/searchresults.id.html?aid=304142']
    start_urls = [
        # 'https://www.booking.com/searchresults.ms.html?aid=304142&label=gen173nr-1FCAMooQE4xQJIG1gEaDGIAQGYARu4AQbIAQzYAQHoAQH4AQKIAgGoAgO4Av3fk-cFwAIB&sid=04f62ed8683bc53f81231999e0f1bf72&tmpl=searchresults&checkin_month=10&checkin_monthday=16&checkin_year=2019&checkout_month=10&checkout_monthday=17&checkout_year=2019&city=-2403010&class_interval=1&dest_id=-2403010&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&src=city&src_elem=sb&srpvid=a54930c4c0f101c8&ss=Kuala%20Lumpur&ss_all=0&ssb=empty&sshis=0&ssne=Kuala%20Lumpur&ssne_untouched=Kuala%20Lumpur&rows=25'
        # "https://www.booking.com/searchresults.ms.html?label=gen173nr-1DCAYooQFCBWpvaG9ySBtYBGhiiAEBmAEbuAEYyAEM2AED6AEB-AECiAIBqAIEuALf7ZPnBcACAQ&lang=ms&sid=04f62ed8683bc53f81231999e0f1bf72&sb=1&src=region&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fregion%2Fmy%2Fjohor.ms.html%3Flabel%3Dgen173nr-1DCAYooQFCBWpvaG9ySBtYBGhiiAEBmAEbuAEYyAEM2AED6AEB-AECiAIBqAIEuALf7ZPnBcACAQ%3Bsid%3D04f62ed8683bc53f81231999e0f1bf72%3Binac%3D0%26%3B&ss=Johor&is_ski_area=0&ssne=Johor&ssne_untouched=Johor&region=991&checkin_year=2019&checkin_month=10&checkin_monthday=10&checkout_year=2019&checkout_month=10&checkout_monthday=11&no_rooms=1&group_adults=2&group_children=0&b_h4u_keep_filters=&from_sf=1"
        "https://www.booking.com/searchresults.ms.html?label=gen173nr-1DCAMooQE4xQJIG1gEaGKIAQGYARu4ARjIAQzYAQPoAQH4AQKIAgGoAgS4As7wk-cFwAIB&lang=ms&sid=04f62ed8683bc53f81231999e0f1bf72&sb=1&src=city&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcity%2Fmy%2Fkuala-lumpur.ms.html%3Flabel%3Dgen173nr-1DCAMooQE4xQJIG1gEaGKIAQGYARu4ARjIAQzYAQPoAQH4AQKIAgGoAgS4As7wk-cFwAIB%3Bsid%3D04f62ed8683bc53f81231999e0f1bf72%3Binac%3D0%26%3B&ss=Kuala+Lumpur&is_ski_area=0&ssne=Kuala+Lumpur&ssne_untouched=Kuala+Lumpur&city=-2403010&checkin_year=2019&checkin_month=11&checkin_monthday=13&checkout_year=2019&checkout_month=11&checkout_monthday=14&no_rooms=1&group_adults=2&group_children=0&b_h4u_keep_filters=&from_sf=1",
        "https://www.booking.com/searchresults.ms.html?label=gen173nr-1DCAYooQFCBWpvaG9ySBtYBGh1iAEBmAEbuAEYyAEM2AED6AEB-AECiAIBqAIEuAKR8ZPnBcACAQ&lang=ms&sid=04f62ed8683bc53f81231999e0f1bf72&sb=1&src=region&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fregion%2Fmy%2Fjohor.ms.html%3Flabel%3Dgen173nr-1DCAYooQFCBWpvaG9ySBtYBGh1iAEBmAEbuAEYyAEM2AED6AEB-AECiAIBqAIEuAKR8ZPnBcACAQ%3Bsid%3D04f62ed8683bc53f81231999e0f1bf72%3Binac%3D0%26%3B&ss=Johor&is_ski_area=0&ssne=Johor&ssne_untouched=Johor&region=991&checkin_year=2019&checkin_month=12&checkin_monthday=16&checkout_year=2019&checkout_month=12&checkout_monthday=17&no_rooms=1&group_adults=2&group_children=0&b_h4u_keep_filters=&from_sf=1"
    ]

    def parse(self, response):
        content = response.xpath('//span[@class="sr-hotel__name\n"]//text()').extract()
        names = [name.strip() for name in content]
        print(names)
        with open('C:\\Users\\Administrator\\Desktop\\booking_name.txt', 'a', encoding='utf8')as f:
            f.write('\n'.join(names))

        nest_page = response.xpath('//*[@id="search_results_table"]/div[4]/nav/ul/li[last()]/a/@href').extract()
        if nest_page:
            next_url = 'https://www.booking.com' + nest_page[0]
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
