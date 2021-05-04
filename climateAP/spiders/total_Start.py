# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/23 上午 10:35
# @Author : xiaoheima
# @Email : ff696977@126.com
# @File : total_Start.py
# @Software: PyCharm

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
''' 1.默认数据年限为 year_1901-year_2017 看树木的年限决定;该修改须在mydomain.py中修改 for Year in Historical[22::]:
    2.number 未来气候策略序号
    3.ENtextfile 输入gps数据:包含lat、lng、el变量（纬度、经度、海拔）
    4.输出文件保存位置为/spiders同级目录
'''


ENtextfile = 'D:/Series of python/scrapy框架/climateAP/climateAP/spiders/输入.csv'   #文件名称（绝对位置）

##########
process = CrawlerProcess(get_project_settings())
process.crawl('mydomain')
process.start()