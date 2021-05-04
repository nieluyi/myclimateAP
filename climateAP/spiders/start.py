# -*- coding: utf-8 -*-
# @Time : 2020/9/9 下午 03:02
# @Author : xiaoheima
# @Email : ff696977@126.com
# @File : start.py
# @Software: PyCharm
#
# import urllib.robotparser
# import scrapy.spiderloader
# import scrapy.statscollectors
# import scrapy.logformatter
# import scrapy.dupefilters
# import scrapy.squeues
# import scrapy.extensions.spiderstate
# import scrapy.extensions.corestats
# import scrapy.extensions.telnet
# import scrapy.extensions.logstats
# import scrapy.extensions.memusage
# import scrapy.extensions.memdebug
# import scrapy.extensions.feedexport
# import scrapy.extensions.closespider
# import scrapy.extensions.debug
# import scrapy.extensions.httpcache
# import scrapy.extensions.statsmailer
# import scrapy.extensions.throttle
# import scrapy.core.scheduler
# import scrapy.core.engine
# import scrapy.core.scraper
# import scrapy.core.spidermw
# import scrapy.core.downloader
# import scrapy.downloadermiddlewares.stats
# import scrapy.downloadermiddlewares.httpcache
# import scrapy.downloadermiddlewares.cookies
# import scrapy.downloadermiddlewares.useragent
# import scrapy.downloadermiddlewares.httpproxy
# import scrapy.downloadermiddlewares.ajaxcrawl
# # import scrapy.downloadermiddlewares.chunked
# import scrapy.downloadermiddlewares.decompression
# import scrapy.downloadermiddlewares.defaultheaders
# import scrapy.downloadermiddlewares.downloadtimeout
# import scrapy.downloadermiddlewares.httpauth
# import scrapy.downloadermiddlewares.httpcompression
# import scrapy.downloadermiddlewares.redirect
# import scrapy.downloadermiddlewares.retry
# import scrapy.downloadermiddlewares.robotstxt
# import scrapy.spidermiddlewares.depth
# import scrapy.spidermiddlewares.httperror
# import scrapy.spidermiddlewares.offsite
# import scrapy.spidermiddlewares.referer
# import scrapy.spidermiddlewares.urllength
# import scrapy.pipelines
# import scrapy.core.downloader.handlers.http
# import scrapy.core.downloader.contextfactory
# from tkinter.filedialog import askdirectory
# from tkinter.messagebox import *
# import csv
# import os
# import pandas as pd
# import numpy as np
# import scrapy
# from lxml import etree
# import tkinter
# import tornado
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# #################图像界面
# #定义读取本地路径函数
# import tkinter
# from tkinter.filedialog import askdirectory
# from tkinter.messagebox import *
# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams,LTTextBox
# #生成界面
# root=tkinter.Tk()
# root.geometry('500x250')
# root.title('climateAP爬虫')
# #生成文本框
# pathroad1=tkinter.StringVar()#设置pathroad为输入文本
# b1entry=tkinter.Entry(root,width=500,textvariable=pathroad1)#为输入文本的功能设计文本框
# b1entry.place(x=100,y=60,width=300,height=30)
#
# pathroad2=tkinter.IntVar()#设置pathroad为输入数字
# b2entry=tkinter.Entry(root,width=500,textvariable=pathroad2)#为输入文本的功能设计文本框
# b2entry.place(x=100,y=90,width=30,height=30)
#
# def selectPath1():
#     path_ = askdirectory()
#     pathroad1.set(path_)
#
#
# ##生成按钮
# b1=tkinter.Button(root,text='输入gps数据',command = selectPath1)#生成文本提示词
# b1.place(x=15,y=60,width=80,height=30)
#
# b2=tkinter.Button(root,text='未来气候序号')#生成文本提示词
# b2.place(x=15,y=90,width=80,height=30)
#
# def get_data():
#     # !/usr/bin/env python3
#     ENtextfile = b1entry.get()
#     number =b2entry.get()
#     process = CrawlerProcess(get_project_settings())
#     process.crawl('mydomain',input=ENtextfile, future_number=number)
#     process.start()
#     showinfo('提示', '获取完成')
#
# work=tkinter.Button(root,text='开始获取数据',command = get_data)#生成翻译键
# # work.pack(side=tkinter.LEFT)#将b1添加至主窗口
# work.place(x=200,y=120,width=90,height=30)
#
# root.mainloop()
#
#



