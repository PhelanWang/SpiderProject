# coding: UTF-8
from PIL import Image
import sys
import os

image_dir = 'G:\\Picture\\WallPaper'

image_list = os.listdir(image_dir)

for image in image_list:
    image_path = image_dir + '\\' + image
    image_size = Image.open(image_path).size
    if (image_size[0] < 1366) or (image_size[1] < 768):
        print(image_size, end=', ')
        os.remove(image_path)