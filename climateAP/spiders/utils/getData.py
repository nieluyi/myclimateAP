# -*- coding: utf-8 -*-
import pandas as pd
import json
import os
import sys
import shutil



def _get_config(logger,__file__):

    """获取config.json数据"""
    src = os.path.split(
        os.path.realpath(__file__))[0] + os.sep + 'config/config.json'
    config_path = os.getcwd() + os.sep + 'config/config.json'
    if src:
        config_path = src
    elif not os.path.isfile(config_path):
        shutil.copy(src, config_path)
        logger.info(u'请先配置当前目录(%s)下的config.json文件，' %
                    os.getcwd())
        sys.exit()
    try:
        with open(config_path,encoding='utf-8') as f:
            config = json.loads(f.read())
            return config
    except ValueError:
        logger.error(u'config.json 格式不正确，请访问 ')
        sys.exit()


def _get_config2(logger,__file__):

    """获取config.json数据"""
    src = os.path.split(
        os.path.realpath(__file__))[0] + os.sep + 'spiders/config/config.json'
    config_path = os.getcwd() + os.sep + 'spiders/config/config.json'
    if src:
        config_path = src
    elif not os.path.isfile(config_path):
        shutil.copy(src, config_path)
        logger.info(u'请先配置当前目录(%s)下的config.json文件，' %
                    os.getcwd())
        sys.exit()
    try:
        with open(config_path,encoding='utf-8') as f:
            config = json.loads(f.read())
            return config
    except ValueError:
        logger.error(u'config.json 格式不正确，请访问 ')
        sys.exit()


def read_gps(input_data):
    '''获取csv中gps数据'''
    data = pd.read_csv(input_data, encoding="utf-8")
    data2 = pd.concat([data.lat, data.lng,data.el], axis=1, ignore_index=True)
    res = []
    for i in data2.index:
        res.append(data2.loc[i].tolist())
    return res

def equ_to_dic(List):
    for i in range(0, len(List)):
        List[i] = List[i].split('=', 1)
    return dict(List)



def getHistorical():
    return [
    'Normal_1961_1990', 'Select a period', 'Normal_1901_1930', 'Normal_1911_1940',
    'Normal_1921_1950', 'Normal_1931_1960', 'Normal_1941_1970', 'Normal_1951_1980',
    'Normal_1961_1990', 'Normal_1971_2000', 'Normal_1981_2010', 'Decade_1901_1910',
    'Decade_1911_1920', 'Decade_1921_1930', 'Decade_1931_1940', 'Decade_1941_1950',
    'Decade_1951_1960', 'Decade_1961_1970', 'Decade_1971_1980', 'Decade_1981_1990',
    'Decade_1991_2000', 'Decade_2001_2010',
    'year_1901', 'year_1902', 'year_1903', 'year_1904', 'year_1905', 'year_1906', 'year_1907', 'year_1908',
    'year_1909', 'year_1910', 'year_1911', 'year_1912', 'year_1913', 'year_1914', 'year_1915', 'year_1916',
    'year_1917', 'year_1918', 'year_1919', 'year_1920', 'year_1921', 'year_1922', 'year_1923', 'year_1924',
    'year_1925', 'year_1926', 'year_1927', 'year_1928', 'year_1929', 'year_1930', 'year_1931', 'year_1932',
    'year_1933', 'year_1934', 'year_1935', 'year_1936', 'year_1937', 'year_1938', 'year_1939', 'year_1940',
    'year_1941', 'year_1942', 'year_1943', 'year_1944', 'year_1945', 'year_1946', 'year_1947', 'year_1948',
    'year_1949', 'year_1950', 'year_1951', 'year_1952', 'year_1953', 'year_1954', 'year_1955', 'year_1956',
    'year_1957', 'year_1958', 'year_1959', 'year_1960', 'year_1961', 'year_1962', 'year_1963', 'year_1964',
    'year_1965', 'year_1966', 'year_1967', 'year_1968', 'year_1969', 'year_1970', 'year_1971', 'year_1972',
    'year_1973', 'year_1974', 'year_1975', 'year_1976', 'year_1977', 'year_1978', 'year_1979', 'year_1980',
    'year_1981', 'year_1982', 'year_1983', 'year_1984', 'year_1985', 'year_1986', 'year_1987', 'year_1988',
    'year_1989', 'year_1990', 'year_1991', 'year_1992', 'year_1993', 'year_1994', 'year_1995', 'year_1996',
    'year_1997', 'year_1998', 'year_1999', 'year_2000', 'year_2001', 'year_2002', 'year_2003', 'year_2004',
    'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009', 'year_2010', 'year_2011', 'year_2012',
    'year_2013', 'year_2014', 'year_2015', 'year_2016', 'year_2017']  #22开始到最后
def getfuture():
     return [
    'Select+a+GCM+and+a+period',
    'CanESM2_RCP45_r1i1p1_2025',
    'CanESM2_RCP45_r1i1p1_2055',
    'CanESM2_RCP45_r1i1p1_2085',
    'CanESM2_RCP85_r1i1p1_2025',
    'CanESM2_RCP85_r1i1p1_2055',
    'CanESM2_RCP85_r1i1p1_2085',
    'CNRM-CM5_RCP45_r1i1p1_2025',
    'CNRM-CM5_RCP45_r1i1p1_2055',
    'CNRM-CM5_RCP45_r1i1p1_2085',
    'CNRM-CM5_RCP85_r1i1p1_2025',
    'CNRM-CM5_RCP85_r1i1p1_2055',
    'CNRM-CM5_RCP85_r1i1p1_2085',
    'HadGEM2-ES_RCP45_r1i1p1_2025',
    'HadGEM2-ES_RCP45_r1i1p1_2055',
    'HadGEM2-ES_RCP45_r1i1p1_2085',
    'HadGEM2-ES_RCP85_r1i1p1_2025',
    'HadGEM2-ES_RCP85_r1i1p1_2055',
    'HadGEM2-ES_RCP85_r1i1p1_2085',
]