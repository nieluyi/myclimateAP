# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from absl import  flags
import logging.config
import sys

from ..items import ClimateapItem1,ClimateapItem2,ClimateapItem3
from .utils.getData import _get_config, read_gps,equ_to_dic,getHistorical


logger = logging.getLogger('spider')
FLAGS = flags.FLAGS

time = ''
lat =''
lng =''
h=''
#D:\Series of python\scrapy框架\备份\climateAP\climateAP\climateAP1.csv
config = _get_config(logger,__file__)


class MydomainSpider(scrapy.Spider):
    name = 'mydomain'
    # allowed_domains = ['climateap.net']
    start_urls = ['https://climateap.net/']

    def __init__(self):

        self.starttime = config["start_date"]
        self.endtime = config["end_date"]
        self.history = getHistorical()
        self.future = config["future"][0]
        self.input = config["input_data"]

        self.gps  = read_gps(self.input[0])  # source file name

    def getDuration(self):
        '''读取起止日期，也可以选择未来策略'''
        starttime, endtime = self.starttime, self.endtime
        flags2 = flags1 = False
        if starttime != None and endtime != None:
            for i in range(len(self.history)):
                if (self.history[i] == starttime[0]):
                    self.start = i
                    flags1 = True
                if (self.history[i] == endtime[0]):
                    self.end = i+1
                    flags2 = True
        if flags1 and flags2:
            return self.history[self.start:self.end]
        else:
            logger.error(u'config.json 日期格式不正确，请输入正确的日期 ')
            sys.exit()

    def detail(self, response):
        html = response.text
        html = etree.HTML(html)
        Annual_variables = html.xpath("//td[@style='width:133px;']/select[@id='ListBox1']/option/text()")
        item1 = ClimateapItem1()
        List1=equ_to_dic(Annual_variables)
        lat              =html.xpath('//tr/td/input[@name="txt_lat"]/@value')[0]
        lng              =html.xpath('//tr/td/input[@name="txt_lng"]/@value')[0]
        h                =html.xpath('//tr/td/input[@name="txt_el"]/@value')[0]
        time             =html.xpath("//td/select[@id='DropD_hist']/option[@selected='selected']/text()")[0]
        item1['x_lan']   =lat
        item1['y_lai']   =lng
        item1['el']      = h
        item1['year']    =time
        item1['table']   ='Annual_variables'
        item1['MAT']     =List1['MAT ']
        item1['MWMT']    =List1['MWMT ']
        item1['MCMT']    =List1['MCMT ']
        item1['TD']      =List1['TD ']
        item1['MAP']     =List1['MAP ']
        item1['AHM']     =List1['AHM ']
        item1['DDlow0']  =List1['DD<0 ']
        item1['DDbig5']  =List1['DD>5 ']
        item1['DDlow18'] =List1['DD<18 ']
        item1['DDbig18'] =List1['DD>18 ']
        item1['NFFD']    =List1['NFFD ']
        item1['PAS']     =List1['PAS ']
        item1['EMT']     =List1['EMT ']
        item1['EXT']     =List1['EXT ']
        item1['Eref']    =List1['Eref ']
        item1['CMD']     =List1['CMD ']
        yield item1

        Seasonal_Variables = html.xpath("//td[@style='width:133px;']/select[@id='ListBox2']/option/text()")
        item2 = ClimateapItem2()
        List2 = equ_to_dic(Seasonal_Variables )

        item2['x_lan']          =  lat
        item2['y_lai']          =  lng
        item2['el']             = h
        item2['year']           =  time
        item2['table']          =  'Seasonal_Variables'
        item2['Tmax_DJF']       =  List2['Tmax_DJF ']
        item2['Tmax_MAM']       =  List2['Tmax_MAM ']
        item2['Tmax_JJA']       =  List2['Tmax_JJA ']
        item2['Tmax_SON']       =  List2['Tmax_SON ']
        item2['Tmin_DJF']       =  List2['Tmin_DJF ']
        item2['Tmin_MAM']       =  List2['Tmin_MAM ']
        item2['Tmin_JJA']       =  List2['Tmin_JJA ']
        item2['Tmin_SON']       =  List2['Tmin_SON ']
        item2['Tave_DJF']       =  List2['Tave_DJF ']
        item2['Tave_MAM']       =  List2['Tave_MAM ']
        item2['Tave_JJA']       =  List2['Tave_JJA ']
        item2['Tave_SON']       =  List2['Tave_SON ']
        item2['PPT_DJF']        =  List2['PPT_DJF ']
        item2['PPT_MAM']        =  List2['PPT_MAM ']
        item2['PPT_JJA']        =  List2['PPT_JJA ']
        item2['PPT_SON']        =  List2['PPT_SON ']
        item2['DDlow0_DJF']     =  List2['DD<0_DJF ']
        item2['DDlow0_MAM']     =  List2['DD<0_MAM ']
        item2['DDlow0_JJA']     =  List2['DD<0_JJA ']
        item2['DDlow0_SON']     =  List2['DD<0_SON ']
        item2['DDbig5_DJF']     =  List2['DD>5_DJF ']
        item2['DDbig5_MAM']     =  List2['DD>5_MAM ']
        item2['DDbig5_JJA']     =  List2['DD>5_JJA ']
        item2['DDbig5_SON']     =  List2['DD>5_SON ']
        item2['DDlow18_DJF']    =  List2['DD<18_DJF ']
        item2['DDlow18_MAM']    =  List2['DD<18_MAM ']
        item2['DDlow18_JJA']    =  List2['DD<18_JJA ']
        item2['DDlow18_SON']    =  List2['DD<18_SON ']
        item2['DDbig18_DJF']    =  List2['DD>18_DJF ']
        item2['DDbig18_MAM']    =  List2['DD>18_MAM ']
        item2['DDbig18_JJA']    =  List2['DD>18_JJA ']
        item2['DDbig18_SON']    =  List2['DD>18_SON ']
        item2['NFFD_DJF']       =  List2['NFFD_DJF ']
        item2['NFFD_MAM']       =  List2['NFFD_MAM ']
        item2['NFFD_JJA']       =  List2['NFFD_JJA ']
        item2['NFFD_SON']       =  List2['NFFD_SON ']
        item2['PAS_DJF']        =  List2['PAS_DJF ']
        item2['PAS_MAM']        =  List2['PAS_MAM ']
        item2['PAS_JJA']        =  List2['PAS_JJA ']
        item2['PAS_SON']        =  List2['PAS_SON ']
        item2['Eref_DJF']       =  List2['Eref_DJF ']
        item2['Eref_MAM']       =  List2['Eref_MAM ']
        item2['Eref_JJA']       =  List2['Eref_JJA ']
        item2['Eref_SON']       =  List2['Eref_SON ']
        item2['CMD_DJF']        =  List2['CMD_DJF ']
        item2['CMD_MAM']        =  List2['CMD_MAM ']
        item2['CMD_JJA']        =  List2['CMD_JJA ']
        item2['CMD_SON']        =  List2['CMD_SON ']
        yield item2

        item3=ClimateapItem3()
        Monthly_Variables = html.xpath("//td[@style='width:133px;']/select[@id='ListBox3']/option/text()")
        List3 = equ_to_dic(Monthly_Variables)
        item3['x_lan']                =  lat
        item3['y_lai']                =  lng
        item3['el'] = h
        item3['year']                 =  time
        item3['table']                =  'Monthly_Variables'
        item3['Tmax_01Kuo']           =  List3['Tmax(01) ']
        item3['Tmax_02Kuo']           =  List3['Tmax(02) ']
        item3['Tmax_03Kuo']           =  List3['Tmax(03) ']
        item3['Tmax_04Kuo']           =  List3['Tmax(04) ']
        item3['Tmax_05Kuo']           =  List3['Tmax(05) ']
        item3['Tmax_06Kuo']           =  List3['Tmax(06) ']
        item3['Tmax_07Kuo']           =  List3['Tmax(07) ']
        item3['Tmax_08Kuo']           =  List3['Tmax(08) ']
        item3['Tmax_09Kuo']           =  List3['Tmax(09) ']
        item3['Tmax_10Kuo']           =  List3['Tmax(10) ']
        item3['Tmax_11Kuo']           =  List3['Tmax(11) ']
        item3['Tmax_12Kuo']           =  List3['Tmax(12) ']
        item3['Tmin_01Kuo']           =  List3['Tmin(01) ']
        item3['Tmin_02Kuo']           =  List3['Tmin(02) ']
        item3['Tmin_03Kuo']           =  List3['Tmin(03) ']
        item3['Tmin_04Kuo']           =  List3['Tmin(04) ']
        item3['Tmin_05Kuo']           =  List3['Tmin(05) ']
        item3['Tmin_06Kuo']           =  List3['Tmin(06) ']
        item3['Tmin_07Kuo']           =  List3['Tmin(07) ']
        item3['Tmin_08Kuo']           =  List3['Tmin(08) ']
        item3['Tmin_09Kuo']           =  List3['Tmin(09) ']
        item3['Tmin_10Kuo']           =  List3['Tmin(10) ']
        item3['Tmin_11Kuo']           =  List3['Tmin(11) ']
        item3['Tmin_12Kuo']           =  List3['Tmin(12) ']
        item3['Tave_01Kuo']           =  List3['Tave(01) ']
        item3['Tave_02Kuo']           =  List3['Tave(02) ']
        item3['Tave_03Kuo']           =  List3['Tave(03) ']
        item3['Tave_04Kuo']           =  List3['Tave(04) ']
        item3['Tave_05Kuo']           =  List3['Tave(05) ']
        item3['Tave_06Kuo']           =  List3['Tave(06) ']
        item3['Tave_07Kuo']           =  List3['Tave(07) ']
        item3['Tave_08Kuo']           =  List3['Tave(08) ']
        item3['Tave_09Kuo']           =  List3['Tave(09) ']
        item3['Tave_10Kuo']           =  List3['Tave(10) ']
        item3['Tave_11Kuo']           =  List3['Tave(11) ']
        item3['Tave_12Kuo']           =  List3['Tave(12) ']
        item3['Prec_01Kuo']           =  List3['Prec(01) ']
        item3['Prec_02Kuo']           =  List3['Prec(02) ']
        item3['Prec_03Kuo']           =  List3['Prec(03) ']
        item3['Prec_04Kuo']           =  List3['Prec(04) ']
        item3['Prec_05Kuo']           =  List3['Prec(05) ']
        item3['Prec_06Kuo']           =  List3['Prec(06) ']
        item3['Prec_07Kuo']           =  List3['Prec(07) ']
        item3['Prec_08Kuo']           =  List3['Prec(08) ']
        item3['Prec_09Kuo']           =  List3['Prec(09) ']
        item3['Prec_10Kuo']           =  List3['Prec(10) ']
        item3['Prec_11Kuo']           =  List3['Prec(11) ']
        item3['Prec_12Kuo']           =  List3['Prec(12) ']
        item3['DDlow0_01Kuo']           =  List3['DD<0(01) ']
        item3['DDlow0_02Kuo']           =  List3['DD<0(02) ']
        item3['DDlow0_03Kuo']           =  List3['DD<0(03) ']
        item3['DDlow0_04Kuo']           =  List3['DD<0(04) ']
        item3['DDlow0_05Kuo']           =  List3['DD<0(05) ']
        item3['DDlow0_06Kuo']           =  List3['DD<0(06) ']
        item3['DDlow0_07Kuo']           =  List3['DD<0(07) ']
        item3['DDlow0_08Kuo']           =  List3['DD<0(08) ']
        item3['DDlow0_09Kuo']           =  List3['DD<0(09) ']
        item3['DDlow0_10Kuo']           =  List3['DD<0(10) ']
        item3['DDlow0_11Kuo']           =  List3['DD<0(11) ']
        item3['DDlow0_12Kuo']           =  List3['DD<0(12) ']
        item3['DDbig5_01Kuo']           =  List3['DD>5(01) ']
        item3['DDbig5_02Kuo']           =  List3['DD>5(02) ']
        item3['DDbig5_03Kuo']           =  List3['DD>5(03) ']
        item3['DDbig5_04Kuo']           =  List3['DD>5(04) ']
        item3['DDbig5_05Kuo']           =  List3['DD>5(05) ']
        item3['DDbig5_06Kuo']           =  List3['DD>5(06) ']
        item3['DDbig5_07Kuo']           =  List3['DD>5(07) ']
        item3['DDbig5_08Kuo']           =  List3['DD>5(08) ']
        item3['DDbig5_09Kuo']           =  List3['DD>5(09) ']
        item3['DDbig5_10Kuo']           =  List3['DD>5(10) ']
        item3['DDbig5_11Kuo']           =  List3['DD>5(11) ']
        item3['DDbig5_12Kuo']           =  List3['DD>5(12) ']
        item3['DDlow18_01Kuo']           =  List3['DD<18(01) ']
        item3['DDlow18_02Kuo']           =  List3['DD<18(02) ']
        item3['DDlow18_03Kuo']           =  List3['DD<18(03) ']
        item3['DDlow18_04Kuo']           =  List3['DD<18(04) ']
        item3['DDlow18_05Kuo']           =  List3['DD<18(05) ']
        item3['DDlow18_06Kuo']           =  List3['DD<18(06) ']
        item3['DDlow18_07Kuo']           =  List3['DD<18(07) ']
        item3['DDlow18_08Kuo']           =  List3['DD<18(08) ']
        item3['DDlow18_09Kuo']           =  List3['DD<18(09) ']
        item3['DDlow18_10Kuo']           =  List3['DD<18(10) ']
        item3['DDlow18_11Kuo']           =  List3['DD<18(11) ']
        item3['DDlow18_12Kuo']           =  List3['DD<18(12) ']
        item3['DDbig18_01Kuo']           =  List3['DD>18(01) ']
        item3['DDbig18_02Kuo']           =  List3['DD>18(02) ']
        item3['DDbig18_03Kuo']           =  List3['DD>18(03) ']
        item3['DDbig18_04Kuo']           =  List3['DD>18(04) ']
        item3['DDbig18_05Kuo']           =  List3['DD>18(05) ']
        item3['DDbig18_06Kuo']           =  List3['DD>18(06) ']
        item3['DDbig18_07Kuo']           =  List3['DD>18(07) ']
        item3['DDbig18_08Kuo']           =  List3['DD>18(08) ']
        item3['DDbig18_09Kuo']           =  List3['DD>18(09) ']
        item3['DDbig18_10Kuo']           =  List3['DD>18(10) ']
        item3['DDbig18_11Kuo']           =  List3['DD>18(11) ']
        item3['DDbig18_12Kuo']           =  List3['DD>18(12) ']
        item3['NFFD_01Kuo']           =  List3['NFFD(01) ']
        item3['NFFD_02Kuo']           =  List3['NFFD(02) ']
        item3['NFFD_03Kuo']           =  List3['NFFD(03) ']
        item3['NFFD_04Kuo']           =  List3['NFFD(04) ']
        item3['NFFD_05Kuo']           =  List3['NFFD(05) ']
        item3['NFFD_06Kuo']           =  List3['NFFD(06) ']
        item3['NFFD_07Kuo']           =  List3['NFFD(07) ']
        item3['NFFD_08Kuo']           =  List3['NFFD(08) ']
        item3['NFFD_09Kuo']           =  List3['NFFD(09) ']
        item3['NFFD_10Kuo']           =  List3['NFFD(10) ']
        item3['NFFD_11Kuo']           =  List3['NFFD(11) ']
        item3['NFFD_12Kuo']           =  List3['NFFD(12) ']
        item3['PAS_01Kuo']           =  List3['PAS(01) ']
        item3['PAS_02Kuo']           =  List3['PAS(02) ']
        item3['PAS_03Kuo']           =  List3['PAS(03) ']
        item3['PAS_04Kuo']           =  List3['PAS(04) ']
        item3['PAS_05Kuo']           =  List3['PAS(05) ']
        item3['PAS_06Kuo']           =  List3['PAS(06) ']
        item3['PAS_07Kuo']           =  List3['PAS(07) ']
        item3['PAS_08Kuo']           =  List3['PAS(08) ']
        item3['PAS_09Kuo']           =  List3['PAS(09) ']
        item3['PAS_10Kuo']           =  List3['PAS(10) ']
        item3['PAS_11Kuo']           =  List3['PAS(11) ']
        item3['PAS_12Kuo']           =  List3['PAS(12) ']
        item3['Eref_01Kuo']           =  List3['Eref(01) ']
        item3['Eref_02Kuo']           =  List3['Eref(02) ']
        item3['Eref_03Kuo']           =  List3['Eref(03) ']
        item3['Eref_04Kuo']           =  List3['Eref(04) ']
        item3['Eref_05Kuo']           =  List3['Eref(05) ']
        item3['Eref_06Kuo']           =  List3['Eref(06) ']
        item3['Eref_07Kuo']           =  List3['Eref(07) ']
        item3['Eref_08Kuo']           =  List3['Eref(08) ']
        item3['Eref_09Kuo']           =  List3['Eref(09) ']
        item3['Eref_10Kuo']           =  List3['Eref(10) ']
        item3['Eref_11Kuo']           =  List3['Eref(11) ']
        item3['Eref_12Kuo']           =  List3['Eref(12) ']
        item3['CMD_01Kuo']           =  List3['CMD(01) ']
        item3['CMD_02Kuo']           =  List3['CMD(02) ']
        item3['CMD_03Kuo']           =  List3['CMD(03) ']
        item3['CMD_04Kuo']           =  List3['CMD(04) ']
        item3['CMD_05Kuo']           =  List3['CMD(05) ']
        item3['CMD_06Kuo']           =  List3['CMD(06) ']
        item3['CMD_07Kuo']           =  List3['CMD(07) ']
        item3['CMD_08Kuo']           =  List3['CMD(08) ']
        item3['CMD_09Kuo']           =  List3['CMD(09) ']
        item3['CMD_10Kuo']           =  List3['CMD(10) ']
        item3['CMD_11Kuo']           =  List3['CMD(11) ']
        item3['CMD_12Kuo']           =  List3['CMD(12) ']
        yield item3

    def parse(self, response):#(self, response):
        url = 'https://climateap.net/'

        for Year in self.getDuration():
            for i in self.gps:
                global time
                time=Year

                gcm  =  self.future#self.future[int(self.future_number)]
                data = "__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=" \
                       "%2FwEPDwUJNzA3MDIxMzE1D2QWAgIDD2QWBgIJDxBkZBYBZmQCCw8QZGQWAWZkAjkPEGRkFgBkZMLh3PMaGvm9PqHNNzGmVfIlxB%2FH" \
                       "&__VIEWSTATEGENERATOR=CA0B0334" \
                       "&__EVENTVALIDATION=%2FwEdALIBIIhdu6zFzpNwKa9GTzMxTwdKP8A6iHeGLmbSkVNUG5%2FceWyrRrhfbPLdnF0N6HEQ6X4maMVkWn9uoLIWb6fmZLODNbptymJSqG8KBxavmPP5CURe%2BeVKuyZ4oAnhmBD7anHH1GRBJl5qglOmgJEeV1bOGcnULZEvJ0jQXWcosfE3Gph0Yo1nQOgwx746juel1E9Vwb18rDGnRFbgSTe4ZSsTrbmWHz5aOYycmuMropnaImlNBC%2BoeSCDjSTx2IHHvL%2Fr1%2BHflbVkkAxPDdByR1zRMV9gxRE3%2F2X7gN9PdKQVsD9WTzqC0a5E%2FxfE7w6U22JbT3NCgFkanvwIx9NIkEThqPrBEJHwaHZvXClAZUoH2tu6u5SME5jOdJgZlmOLL%2FDjJrU14qUPtVzMCCsVfXxLIvlL174YJm7oKsKxc7bKhHc%2B1haslPcgsVEc6FBHKAqLTtDhHOaNlItGNK95dbHAK4Z5SBCQWmWU3sHIZIPm2GQW0MYq3hrJxzA1BFW9nRFgxlAiNzVElTLzgXRHktwv%2BAMBiLZ97RIgqsS%2FX4v9aRb8Nbth8EThyPxFVkH97%2BGknRfFCCzefem1EXuKTby1807IP2mzmCAZUWW%2F2ttYMqXW5Z6WPqNO3HK6MuYFOz8clUZQ7I9jR41%2BopdQ5tb%2FBnWa1q%2FYIT8TNG3m6mbCGoRBmMXIZAP0K%2FKqQa7iFLTOLJidQEyx8YZHvdc6EjzJU%2FqPUW0QmdWuoFDiKSikOaWo%2BfWQ4tk1LTYgkRyHW2IPvF0Qyess4vvG%2BqCTSNGx1Encr2pRFMR8sbUcVmnznKq1lpAfTbhE4ews9hxj%2BPlwg%2Fgc7QILbQdn0yMMyLgcKWNMbrNCmMcjVKCW6srAjV43%2BjbQPrGxfdDult6DMPN36zflQRIWEIH0%2BbbsEfKLWz%2BDDTxzyY%2BHMU6%2FRxAnwbiUmZ6KbCf7Aa4bEj%2Fx87VK8ocScHVgdMxoXDah4kIZu5YlT9V0RjjVwT9e8H6Dtq35Nk9ZYmHvNl%2BlMm75Cmp6W%2Ftg4FXd0H4RlelgU0QN4n7EVPWlSPE5h51wyJEDrw%2F3SsYYTKsXS7SB1abOnIakES1vpv4yd6XWsVp7cvmTjmiK2IisEeru9iAvy8lilQZfkqJSyHzNYgEbMLRA18eWlL3XukcVwKF1r8dLd0cpJATYVMHNXZQ8tdsmBFRIVjgb6e3aVIvDR4Gj5GYsdW%2BUp5Yj%2BAvLQjkrzANW4okoX6ZpGACGLNpL0UgcBGCrVY%2BRl3Uq5aOiR4p37306gmvLnT7zaLlxlmAJGJSfmqR2ebqt648usAr0z7XjcAsW76fB0W9M96Dj1%2Ff1txO2V7UpfWT%2F0iH1X%2F%2B5gSdAJoDQF%2Fv8LucmfHct1pgNYU0SLkrkwq04a8aHEz8%2BfiM4nREHB9IQnugi1qkzb312OHej9hEqaoj6zUkIv0fcDGYdEXmfjZS7Fk1%2Fj9MW%2B%2FrS8WiOKnXCPlKiYUG6Q43BQp41M9wSpbjr3LFQH4qmb%2BjSQ25at0U0uYehF%2Bt1l3OhjtJbSVQ%2FUrBcGBgvE8LF2pFunCOg6aXyfPvn8agms5ahkPgXgbG91PLdcy7dD5jfKVtTv35RgAeq4wdqvG6bmLWGEtZ7giCT9ueH55jgl5iSMo3mX%2FflHqUfyoT5a6C4TZSYpYbs5gTav1G6bilqtth3wDISSeJjw0uDf71U1xE5v4sksQdsvj9N%2BQU0UsHj7i1RC60myyY%2F%2Bv4fI3mY743Hm%2FYI1SNE2IXMmcrPXnGpPVRE%2FxbO8M1KX8dOA4Y0jY%2BaqN%2BcuBHdj9U6cHCavouw%2FwmHQsrhYRA%2FSkunX4oveQf%2BDoxNefQBRle9%2B9%2B5Ex%2Bx6iIWQQEypnqko8NkdEg%2B2YHrCoOqk4ZtfsB6m4zp5vDCBS34hR656kmZI4PeFfn5DZAQ2WqeDvxo4ZT%2FKunw3DIpjtuYLXcucWdb009%2BcNglvkCIFSgkUmO1QDLdqAgA7XHoL1bflM5NtquytfH2Ref1K00LArIRsvQMsCFKT4tuLe2FDBacu9bOgA8gpchOxW6f9sRnkkBhiJbQRaSZQ8jZLtxcPHusW3SIAJAJAh1Elg9KFGeIN%2BKVDJeHwwHH0%2BojQH6oTVmzUXICic2g2j6QinV9JSQZWLO34POsNJI%2B1aVSKJ8RIwngsW7YodhYv7dVzQ7VqhMzcK2uLJwuKaR%2BnzKMjszEPL%2B3hT%2Bk6q77aCB41%2F6KwvfxH7XTH%2FrInQcEaxBZRcCWrhfHbnIlOoa%2Fn6xTbxDzxsWHd1K7KyjjKrcwJ%2FBtF8yn9d%2B%2FPW1%2BFJSNkIQoJKQazLo6VJ8do6V%2FcnT3sC5EKoZKAOiZZfnG1eFslvGu8IIJmpJQ0EoGKmdL2N93ZhhniX5xm%2B9b6%2B1fTDLeT6IBEtIcfS2pXKQhF7daBCaYDQVK5jGHkT8LwSyOVc16DQPb3bv6xkM%2F7CzS5mInrSdQmfD5xw3nzeMwkbz7U4fJxFg%2B%2Fq%2BlBeQ2DDrGCpOSAI3C7UOg7CEfncKB%2B5kN2%2BHDeKL3vq8gMJocJP3sAUbu17SrY2a94JK%2BVsGl2FvnkvnjgrEe%2Br8in%2F7SuGMBbjFevCJXbYbShQ8TXNs5M0XhfCSJNV7sgPSEi%2FMlsfK4uxfVr0nTnCEXjUZUAijyZjIZxrKLB5LwOcivJb152HVhI%2BFjI3eEI1140U8p6hmujMpw4qC0y6zNUq1hvO4%2Bx98CrtNPcstORv8cCmRwEfr7VSuZmj0z9BakQcFlChMPhh7n96tVtuJB9C9EoLVLWtstWj55ekyMaAHyGcAgvBURXKQdNNR8zNrgZvQnV41ZK1CvAZe0YiFBXYQ30rx1DQbGfFy0VMhM3Hlz%2FP4B7iqGm4v6RbZSTOFtYwU%2B68JmxxB%2F2zk8dOMoL14bD79YCDM%2BBGActdcuWcQd%2FmRWU3D1XPG%2BZLKFWpfqR%2BOWimZUvuWwxwj4Dv%2FUbi4PjS9YoX3w4X1YvrDNBBvC0fLKRwPKccIlJJptIPL6sFlFsGYZZJ2suGczWVgJLQzb5ZCfyRDSYtjkMn%2BzutOQ2n0C%2BG1LKDyB89456FsjyMX3pIdKUL2Qe%2BSTp8g8ss%2FkSKfQN45vg80q%2F1SN5tWNiZdJX1rpI0ijSS20GwWFcYdg97y%2Bm4MIVgIBpfWCe0l8jLFPxlNbf1c8HuIkPSTZqzFH6FCB%2BqkQR6hc%2FuAv3gFpXRrb3JHpL%2BK3a9uHaiJ9dNRSkAro3Nt7ZJYXe3Y63lWsiOLEC72ydvSOwpK7r172dzQle%2BRT3u9NNSGK18rl5ksODuoIPXwLjgb%2FxGOOXXqQ65DBiDf5163FGT0jM1B15zd3%2FtWwVJbVbsG%2BLJYCJ7l19kHLePh1Xpqr8lGzgz%2BJtyQ53ivR8G03NHgSM0m5SHRs2HotenOgNWcLT%2BDYpBcCSwxHj9qW0Ki0RpUm1shhwqMQSbQC8w%2F29av4XWTR6wnGfha7DlX0%2BvUv%2BRALZIyvoq%2BTY1ehUDR7SelOVpOsVWKvLZdll%2F0Zzfg78Z8BXhXifTCAVkevd0XbfyOK0Hd0uXlyafPgTOOAxcbEvL3%2BbUNlp8WWtLfKDneQ8RezB3RBRKc5DKZ41ZZYgDymPir0Zp4mFYzbkIiFO1BYkfsxnzcMxZ%2BpEWnATnHGCXm4xNRMd2LGtoyxQIL8yQ7aMWXJuMBsKPTdR1IYSDJx8Cyl%2FiqOcg0UHROpWJ%2FOSY2L8xqUWuN8kWgjWuiVAktcr8jjZKgUY0wJipCqrBmFAnX0Gq1uIAq6%2F7tLzqQrpjunyoLgSRPr2JvCXtjtQ40B3XBD8J36UQw2mYR29qwt"\
                       "&txt_lat={}&" \
                       "&txt_lng={}&" \
                       "&txt_el={}&" \
                       "&DropD_hist={}&" \
                       "&DropD_gcm={}&" \
                       "Button1=Calculate&txt_fOut=ClimateData.csv&" \
                       "txt_count=0&txt_opacity=25&" \
                       "txt_ovlTag=MAT_1961-1990%3A&" \
                       "txt_zoom=3&txt_mapCt_lat=10.72&" \
                       "txt_mapCt_lng=125.44&" \
                       "txt_overlay=overlays%2FAP%2Fclm%2Fmat_1961_1990.png&" \
                       "txt_mapKey=overlays%2FAP%2Fclm%2Fmat_1961_1990_lbl.png"
                data = data.format(i[0], i[1], i[2], Year, gcm)

                result=scrapy.FormRequest(url, method='POST', callback=self.detail, body = data)

                yield result







