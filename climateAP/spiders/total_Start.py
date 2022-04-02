# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/11/23 上午 10:35
# @Author : xiaoheima
# @Email : ff696977@126.com
# @File : total_Start.py
# @Software: PyCharm

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

##########
process = CrawlerProcess(get_project_settings())
process.crawl('mydomain')
process.start()