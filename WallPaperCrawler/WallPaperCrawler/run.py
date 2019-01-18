# coding: utf-8
import os


def run_spider():
    os.chdir('../')
    print(os.getcwd())
    os.system('scrapy crawl WallPaper --nolog')


if __name__ == '__main__':
    run_spider()