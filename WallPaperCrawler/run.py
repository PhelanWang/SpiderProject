# coding: utf-8
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings
from WallPaperCrawler.spiders.WallPaper import WallpaperSpider


def run_spider():
    process = CrawlerProcess(settings)
    process.crawl(WallpaperSpider())
    process.start()


if __name__ == '__main__':
    run_spider()