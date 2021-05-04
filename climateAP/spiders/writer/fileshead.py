# -*- coding: utf-8 -*-

# Define your item pipelines name here
def gethead1():
    return ['x_lan','y_lai','year','table','MAT','MWMT','MCMT','TD','MAP','AHM','DD<0',
         'DD>5', 'DD<18','DD>18','NFFD','PAS','EMT','EXT','Eref','CMD']


def gethead2():
    return['x_lan','y_lai','year','table','Tmax_DJF','Tmax_MAM','Tmax_JJA','Tmax_SON','Tmin_DJF',
    'Tmin_MAM','Tmin_JJA','Tmin_SON','Tave_DJF','Tave_MAM','Tave_JJA','Tave_SON','PPT_DJF',
    'PPT_MAM','PPT_JJA','PPT_SON','DD<0_DJF','DD<0_MAM','DD<0_JJA','DD<0_SON','DD>5_DJF',
    'DD>5_MAM','DD>5_JJA','DD>5_SON','DD<18_DJF','DD<18_MAM','DD<18_JJA','DD<18_SON','DD>18_DJF',
    'DD>18_MAM','DD>18_JJA','DD>18_SON','NFFD_DJF','NFFD_MAM','NFFD_JJA','NFFD_SON','PAS_DJF','PAS_MAM',
    'PAS_JJA','PAS_SON','Eref_DJF','Eref_MAM','Eref_JJA','Eref_SON','CMD_DJF','CMD_MAM','CMD_JJA','CMD_SON']

def gethead3():
    return['x_lan','y_lai','year','table','Tmax_01','Tmax_02','Tmax_03','Tmax_04','Tmax_05','Tmax_06',
    'Tmax_07','Tmax_08','Tmax_09','Tmax_10','Tmax_11','Tmax_12','Tmin_01','Tmin_02','Tmin_03',
    'Tmin_04','Tmin_05','Tmin_06','Tmin_07','Tmin_08','Tmin_09','Tmin_10','Tmin_11','Tmin_12',
    'Tave_01','Tave_02','Tave_03','Tave_04','Tave_05','Tave_06','Tave_07','Tave_08','Tave_09',
    'Tave_10','Tave_11','Tave_12','Prec_01','Prec_02','Prec_03','Prec_04','Prec_05','Prec_06',
    'Prec_07','Prec_08','Prec_09','Prec_10','Prec_11','Prec_12','DD<0_01','DD<0_02','DD<0_03',
    'DD<0_04','DD<0_05','DD<0_06','DD<0_07','DD<0_08','DD<0_09','DD<0_10','DD<0_11',
    'DD<0_12','DD>5_01','DD>5_02','DD>5_03','DD>5_04','DD>5_05','DD>5_06','DD>5_07',
    'DD>5_08','DD>5_09','DD>5_10','DD>5_11','DD>5_12','DD<18_01','DD<18_02','DD<18_03',
    'DD<18_04','DD<18_05','DD<18_06','DD<18_07','DD<18_08','DD<18_09','DD<18_10','DD<18_11',
    'DD<18_12','DD>18_01','DD>18_02','DD>18_03','DD>18_04','DD>18_05','DD>18_06','DD>18_07',
    'DD>18_08','DD>18_09','DD>18_10','DD>18_11','DD>18_12','NFFD_01','NFFD_02','NFFD_03','NFFD_04',
    'NFFD_05','NFFD_06','NFFD_07','NFFD_08','NFFD_09','NFFD_10','NFFD_11','NFFD_12','PAS_01','PAS_02',
    'PAS_03','PAS_04','PAS_05','PAS_06','PAS_07','PAS_08','PAS_09','PAS_10','PAS_11','PAS_12',
    'Eref_01','Eref_02','Eref_03','Eref_04','Eref_05','Eref_06','Eref_07','Eref_08','Eref_09',
    'Eref_10','Eref_11','Eref_12','CMD_01','CMD_02','CMD_03','CMD_04','CMD_05','CMD_06','CMD_07',
    'CMD_08','CMD_09','CMD_10','CMD_11','CMD_12']