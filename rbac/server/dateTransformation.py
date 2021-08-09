# coding=utf-8
#__author__=50510661@qq.com
def dateTransformation(obj):
    '''
    时间转换
    :param obj:
    :return:
    '''
    # print('obj',obj,type(obj))
    yy=obj.split('-')[0].strip()
    # print('yy',yy)
    MM=obj.split('-')[1].strip()
    # print('MM',MM)
    DD=obj.split('-')[2].strip()
    # print('DD',DD)
    if MM == '一月':MM='01'
    elif MM == '二月':MM='02'
    elif MM == '三月':MM='03'
    elif MM == '四月':MM='04'
    elif MM == '五月':MM='05'
    elif MM == '六月':MM='06'
    elif MM == '七月':MM='07'
    elif MM == '八月':MM='08'
    elif MM == '九月':MM='09'
    elif MM == '十月':MM='10'
    elif MM == '十一月':MM='11'
    elif MM == '十二月':MM='12'
    yy='%s-%s-%s'%(yy,MM,DD)
    # print('format--',yy)
    return yy