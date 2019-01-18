# -*- coding: utf-8 -*-

import urllib.request
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WallpapercrawlerPipeline(object):

    def process_item(self, item, spider):
        file_path = 'G:\Picture\WallPaper'
        img_url = item['img_url']
        file_name = img_url.split('/')[-1]
        file = file_path+'\\'+file_name
        if not os.path.exists(file):
            self.download_image(item['img_url'], file)
        else:
            print('exist. . .')

    def download_image(self, url, file):
        try:
            urllib.request.urlretrieve(url, file)
        except Exception as e:
            print('Error: '+url+' '+file)


# d = WallpapercrawlerPipeline()
# url = 'http://img1.gamersky.com/image2016/02/20160227_hc_44_4/gamersky_010origin_019_2016227193384C.jpg'
# file_name = 'gamersky_010origin_019_2016227193384C.jpg'
# file_path = 'G:\Picture\WallPaper'
# d.download_image(url, file_path+'\\'+file_name)