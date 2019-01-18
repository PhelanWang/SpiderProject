# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib.parse import urljoin


class WallpaperSpider(scrapy.Spider):
    name = 'WallPaper'
    allowed_domains = ['gamersky.com']
    start_urls = ['https://www.gamersky.com/ent/wp/']

    def parse(self, response):
        page_list = response.xpath('//ul[@class="pictxt contentpaging"]/li')
        for page in page_list:
            page_url = page.xpath('div[@class="img"]/a/@href').extract()
            if page_url:
                yield Request(url=urljoin(self.start_urls[0], page_url[0]), callback=self.parse_page)

        next_url = response.xpath('//span[@class="pagecss"]/a[@class="p1 nexe"]/@href').extract()
        if next_url:
            yield Request(urljoin(self.start_urls[0], next_url[0]))

    def parse_page(self, response):
        img_list = response.xpath('//p[@align="center"]/a/@href').extract()
        for img_url in img_list:
            yield {'img_url': img_url.split('?')[1]}

        next_list = set(response.xpath('//div[@class="page_css"]/a/@href').extract())
        for page_url in next_list:
            yield Request(page_url)
