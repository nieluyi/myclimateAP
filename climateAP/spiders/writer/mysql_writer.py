import copy
import logging
import sys

from .writer import Writer

logger = logging.getLogger('spider.mysql_writer')


class MySqlWriter(Writer):
    def __init__(self, mysql_config):
        self.mysql_config = mysql_config

        # 创建'weibo'数据库
        create_database = """CREATE DATABASE IF NOT EXISTS climateAP DEFAULT
                            CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"""
        self._mysql_create_database(create_database)
        self.mysql_config['db'] = 'climateAP'

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
            # We use this to filter out unset values.
            data_list = [{k: v
                          for k, v in data.items() if v is not None}
                         for data in data_list]

            keys = ', '.join(data_list[0].keys())
            values = ', '.join(['%s'] * len(data_list[0]))
            connection = pymysql.connect(**self.mysql_config)
            cursor = connection.cursor()
            sql = """INSERT INTO {table}({keys}) VALUES ({values}) ON
                        DUPLICATE KEY UPDATE""".format(table=table,
                                                       keys=keys,
                                                       values=values)
            update = ','.join([
                ' {key} = values({key})'.format(key=key)
                for key in data_list[0]
            ])
            sql += update
            try:
                cursor.executemany(
                    sql, [tuple(data.values()) for data in data_list])
                connection.commit()
            except Exception as e:
                connection.rollback()
                logger.exception(e)
            finally:
                connection.close()

    def write_weibo(self, weibos):
        """将爬取的微博信息写入MySQL数据库"""
        # 创建'weibo'表
        try:
            create_table ="""
                CREATE TABLE IF NOT EXISTS weibo (
                x_lan varchar(30) NOT NULL,
                y_lai varchar(30),
                year varchar(30),
                table varchar(30),
                MAT varchar(30),
                MWMT varchar(30),
                MCMT varchar(30),
                TD varchar(30),
                MAP varchar(30),
                AHM varchar(30),
                DDlow0 varchar(30),
                DDbig5 varchar(30),
                DDlow18 varchar(30),
                DDbig18 varchar(30),
                NFFD varchar(30),
                PAS varchar(30),
                EMT varchar(30),
                EXT  varchar(30),
                Eref varchar(30),
                CMD varchar(30)
                PRIMARY KEY(x_lan)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
            self._mysql_create_table(create_table)
            # 在'weibo'表中插入或更新微博数据
            weibo_list = []
            info_list = copy.deepcopy(weibos)
            for weibo in info_list:
                weibo_list.append(weibo.__dict__)
            self._mysql_insert('weibo', weibo_list)
            logger.info(u'%d条写入MySQL数据库完毕', len(weibos))
        except Exception as e:
            logger.exception(e)
