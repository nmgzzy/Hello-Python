# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:54:09 2018

@author: Joey Zhao
"""

from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '14353301'
API_KEY = 'j8vzfr6gYKiyQYFzemeprjG6'
SECRET_KEY = 'xGK4yYBUPpu5P00nCBTD391Zog63vrUb'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用通用物体识别 """
client.advancedGeneral(image)

""" 如果有可选参数 """
#options = {}
#options["baike_num"] = 5

""" 带参数调用通用物体识别 """
#client.advancedGeneral(image, options)
