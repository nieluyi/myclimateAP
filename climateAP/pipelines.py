# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import ClimateapItem1,ClimateapItem2,ClimateapItem3
from .spiders.writer.fileshead import gethead1,gethead2,gethead3
import csv
import os
import sys
import logging

class ClimateapPipeline:
    def __init__(self):
        self.headers1 = gethead1()
        self.headers2 = gethead2()
        self.headers3 = gethead3()

    def open_spider(self, spider):

        # csv文件的位置,无需事先创建
        store_file1 = os.path.dirname(__file__) + '\climateAP1.csv'
        store_file2 = os.path.dirname(__file__) + '\climateAP2.csv'
        store_file3 = os.path.dirname(__file__) + '\climateAP3.csv'
        self.file1 = open(store_file1, 'a+', encoding="gb2312",newline = '')  # 打开(创建)文件
        self.file2 = open(store_file2, 'a+', encoding="gb2312", newline='')
        self.file3 = open(store_file3, 'a+', encoding="gb2312", newline='')
        # self.file.write(codecs.BOM_UTF8)
        self.writer1 = csv.writer(self.file1, dialect="excel")        # csv写法
        self.writer2 = csv.writer(self.file2, dialect="excel")
        self.writer3 = csv.writer(self.file3, dialect="excel")

        self.writer1.writerow(self.headers1)
        self.writer2.writerow(self.headers2)
        self.writer3.writerow(self.headers3)

    def process_item(self,item,spider):
        # 判断字段值不为空再写入文件
        # print("正在写入......")
        if isinstance(item,ClimateapItem1):
            # 主要是解决存入csv文件时出现的每一个字以‘，’隔离
            self.writer1.writerow([
                                   item['x_lan'],
                                   item['y_lai'],
                                   item['el'],
                                   item['year'],
                                   item['table'],
                                   item['MAT'] ,
                                   item['MWMT'],
                                   item['MCMT'],
                                   item['TD']  ,
                                   item['MAP'] ,
                                   item['AHM'] ,
                                   item['DDlow0'],
                                   item['DDbig5'],
                                   item['DDlow18'],
                                   item['DDbig18'],
                                   item['NFFD'],
                                   item['PAS'] ,
                                   item['EMT'] ,
                                   item['EXT'] ,
                                   item['Eref'],
                                   item['CMD']
                                   ])
            return item
        elif isinstance(item,ClimateapItem2):
            self.writer2.writerow([
                item['x_lan'],
                item['y_lai'],
                item['el'],
                item['year'],
                item['table'],
                item['Tmax_DJF'],
                item['Tmax_MAM'],
                item['Tmax_JJA'],
                item['Tmax_SON'],
                item['Tmin_DJF'],
                item['Tmin_MAM'],
                item['Tmin_JJA'],
                item['Tmin_SON'],
                item['Tave_DJF'],
                item['Tave_MAM'],
                item['Tave_JJA'],
                item['Tave_SON'],
                item['PPT_DJF'],
                item['PPT_MAM'],
                item['PPT_JJA'],
                item['PPT_SON'],
                item['DDlow0_DJF'],
                item['DDlow0_MAM'],
                item['DDlow0_JJA'],
                item['DDlow0_SON'],
                item['DDbig5_DJF'],
                item['DDbig5_MAM'],
                item['DDbig5_JJA'],
                item['DDbig5_SON'],
                item['DDlow18_DJF'],
                item['DDlow18_MAM'],
                item['DDlow18_JJA'],
                item['DDlow18_SON'],
                item['DDbig18_DJF'],
                item['DDbig18_MAM'],
                item['DDbig18_JJA'],
                item['DDbig18_SON'],
                item['NFFD_DJF'],
                item['NFFD_MAM'],
                item['NFFD_JJA'],
                item['NFFD_SON'],
                item['PAS_DJF'],
                item['PAS_MAM'],
                item['PAS_JJA'],
                item['PAS_SON'],
                item['Eref_DJF'],
                item['Eref_MAM'],
                item['Eref_JJA'],
                item['Eref_SON'],
                item['CMD_DJF'],
                item['CMD_MAM'],
                item['CMD_JJA'],
                item['CMD_SON'],
            ])
            return item
        elif isinstance(item,ClimateapItem3):
            self.writer3.writerow([
                item['x_lan'],
                item['y_lai'],
                item['el'],
                item['year'],
                item['table'],
                item['Tmax_01Kuo'],
                item['Tmax_02Kuo'],
                item['Tmax_03Kuo'],
                item['Tmax_04Kuo'],
                item['Tmax_05Kuo'],
                item['Tmax_06Kuo'],
                item['Tmax_07Kuo'],
                item['Tmax_08Kuo'],
                item['Tmax_09Kuo'],
                item['Tmax_10Kuo'],
                item['Tmax_11Kuo'],
                item['Tmax_12Kuo'],
                item['Tmin_01Kuo'],
                item['Tmin_02Kuo'],
                item['Tmin_03Kuo'],
                item['Tmin_04Kuo'],
                item['Tmin_05Kuo'],
                item['Tmin_06Kuo'],
                item['Tmin_07Kuo'],
                item['Tmin_08Kuo'],
                item['Tmin_09Kuo'],
                item['Tmin_10Kuo'],
                item['Tmin_11Kuo'],
                item['Tmin_12Kuo'],
                item['Tave_01Kuo'],
                item['Tave_02Kuo'],
                item['Tave_03Kuo'],
                item['Tave_04Kuo'],
                item['Tave_05Kuo'],
                item['Tave_06Kuo'],
                item['Tave_07Kuo'],
                item['Tave_08Kuo'],
                item['Tave_09Kuo'],
                item['Tave_10Kuo'],
                item['Tave_11Kuo'],
                item['Tave_12Kuo'],
                item['Prec_01Kuo'],
                item['Prec_02Kuo'],
                item['Prec_03Kuo'],
                item['Prec_04Kuo'],
                item['Prec_05Kuo'],
                item['Prec_06Kuo'],
                item['Prec_07Kuo'],
                item['Prec_08Kuo'],
                item['Prec_09Kuo'],
                item['Prec_10Kuo'],
                item['Prec_11Kuo'],
                item['Prec_12Kuo'],
                item['DDlow0_01Kuo'],
                item['DDlow0_02Kuo'],
                item['DDlow0_03Kuo'],
                item['DDlow0_04Kuo'],
                item['DDlow0_05Kuo'],
                item['DDlow0_06Kuo'],
                item['DDlow0_07Kuo'],
                item['DDlow0_08Kuo'],
                item['DDlow0_09Kuo'],
                item['DDlow0_10Kuo'],
                item['DDlow0_11Kuo'],
                item['DDlow0_12Kuo'],
                item['DDbig5_01Kuo'],
                item['DDbig5_02Kuo'],
                item['DDbig5_03Kuo'],
                item['DDbig5_04Kuo'],
                item['DDbig5_05Kuo'],
                item['DDbig5_06Kuo'],
                item['DDbig5_07Kuo'],
                item['DDbig5_08Kuo'],
                item['DDbig5_09Kuo'],
                item['DDbig5_10Kuo'],
                item['DDbig5_11Kuo'],
                item['DDbig5_12Kuo'],
                item['DDlow18_01Kuo'],
                item['DDlow18_02Kuo'],
                item['DDlow18_03Kuo'],
                item['DDlow18_04Kuo'],
                item['DDlow18_05Kuo'],
                item['DDlow18_06Kuo'],
                item['DDlow18_07Kuo'],
                item['DDlow18_08Kuo'],
                item['DDlow18_09Kuo'],
                item['DDlow18_10Kuo'],
                item['DDlow18_11Kuo'],
                item['DDlow18_12Kuo'],
                item['DDbig18_01Kuo'],
                item['DDbig18_02Kuo'],
                item['DDbig18_03Kuo'],
                item['DDbig18_04Kuo'],
                item['DDbig18_05Kuo'],
                item['DDbig18_06Kuo'],
                item['DDbig18_07Kuo'],
                item['DDbig18_08Kuo'],
                item['DDbig18_09Kuo'],
                item['DDbig18_10Kuo'],
                item['DDbig18_11Kuo'],
                item['DDbig18_12Kuo'],
                item['NFFD_01Kuo'],
                item['NFFD_02Kuo'],
                item['NFFD_03Kuo'],
                item['NFFD_04Kuo'],
                item['NFFD_05Kuo'],
                item['NFFD_06Kuo'],
                item['NFFD_07Kuo'],
                item['NFFD_08Kuo'],
                item['NFFD_09Kuo'],
                item['NFFD_10Kuo'],
                item['NFFD_11Kuo'],
                item['NFFD_12Kuo'],
                item['PAS_01Kuo'],
                item['PAS_02Kuo'],
                item['PAS_03Kuo'],
                item['PAS_04Kuo'],
                item['PAS_05Kuo'],
                item['PAS_06Kuo'],
                item['PAS_07Kuo'],
                item['PAS_08Kuo'],
                item['PAS_09Kuo'],
                item['PAS_10Kuo'],
                item['PAS_11Kuo'],
                item['PAS_12Kuo'],
                item['Eref_01Kuo'],
                item['Eref_02Kuo'],
                item['Eref_03Kuo'],
                item['Eref_04Kuo'],
                item['Eref_05Kuo'],
                item['Eref_06Kuo'],
                item['Eref_07Kuo'],
                item['Eref_08Kuo'],
                item['Eref_09Kuo'],
                item['Eref_10Kuo'],
                item['Eref_11Kuo'],
                item['Eref_12Kuo'],
                item['CMD_01Kuo'],
                item['CMD_02Kuo'],
                item['CMD_03Kuo'],
                item['CMD_04Kuo'],
                item['CMD_05Kuo'],
                item['CMD_06Kuo'],
                item['CMD_07Kuo'],
                item['CMD_08Kuo'],
                item['CMD_09Kuo'],
                item['CMD_10Kuo'],
                item['CMD_11Kuo'],
                item['CMD_12Kuo'],
            ])
            return item


    def close_spider(self,spider):
        self.file1.close()
        self.file2.close()
        self.file3.close()

from .spiders.utils.getData import _get_config2

logger = logging.getLogger('spider.mysql_writer')

class  WebcrawlerScrapyPipeline:
    ''' 定义需要格式化的内容（或是需要保存到数据库的字段'''
    def __init__(self):

        self.config = _get_config2(logger, __file__)
        self.mysql_config = self.config['mysql_config']#获取config中的数据库配置信息
        # 创建数据库
        create_database = """CREATE DATABASE IF NOT EXISTS climateAP DEFAULT
                                  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"""

        self._mysql_create_database(create_database)


    def _mysql_create(self, connection, sql):
        """创建MySQL数据库或表"""
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
        finally:
            connection.close()

    def _mysql_create_database(self, sql):
        """创建MySQL数据库"""
        try:
            import pymysql
        except ImportError:
            logger.warning(
                u'系统中可能没有安装pymysql库，请先运行 pip install pymysql ，再运行程序')
            sys.exit()
        try:
            connection = pymysql.connect(**self.mysql_config)
            self._mysql_create(connection, sql)
        except pymysql.OperationalError:
            logger.warning(u'系统中可能没有安装或正确配置MySQL数据库，请先根据系统环境安装或配置MySQL，再运行程序')
            sys.exit()

    def _mysql_create_table(self, sql):
        """创建MySQL表"""
        import pymysql
        connection = pymysql.connect(**self.mysql_config)
        self._mysql_create(connection, sql)

    def _mysql_insert(self, table, data_list):
        """向MySQL表插入或更新数据"""
        import pymysql
        if len(data_list) > 0:
            keys = ', '.join([
                '`{key}`'.format(key=key)
                for key in data_list.keys()
            ])
            values = ', '.join([
                '"{value}"'.format(value=value)
                for value in data_list.values()
            ])
            connection = pymysql.connect(**self.mysql_config)
            cursor = connection.cursor()
            sql = """INSERT INTO {table}({keys}) VALUES ({values}) ON
             DUPLICATE KEY UPDATE `x_lan`=`x_lan`,`year`=`year`""".format(table=table,
                                                                          keys=keys,
                                                                          values=values)


            try:
                cursor.execute(sql)
                connection.commit()
            except Exception as e:
                connection.rollback()
                logger.exception(e)
            finally:
                connection.close()

    def write_climateAP(self, climateAPs,table_name):
        columns = ', '.join([
                '`{key}` varchar(20)'.format(key=key)
                for key in climateAPs.keys()
            ])
        try:
            create_table = '''
                    CREATE TABLE IF NOT EXISTS {table_name}(
                                             {columns},
                                             PRIMARY KEY (`x_lan`,`year`)
                                    ) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4'''.format(table_name=table_name,columns=columns)
            self._mysql_create_table(create_table)
            # 在'climateAP'表中插入或更新数据
            self._mysql_insert(table_name, climateAPs)
            logger.info(u'%d条数据写入MySQL数据库完毕', len(climateAPs))
        except Exception as e:
            logger.exception(e)


    #pipeline默认调用
    def process_item(self, item, spider):
        #连接数据库
        #创建数据表
        #写入文件
        #返回写入是否成功

        if isinstance(item, ClimateapItem1):
            self.write_climateAP(item,"climateap1")
        elif isinstance(item, ClimateapItem2):
            self.write_climateAP(item, "climateap2")
        elif isinstance(item, ClimateapItem3):
            self.write_climateAP(item, "climateap3")
        return item


