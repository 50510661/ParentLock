# zhangjun
# 2020-06-04
# UTC 上海时间转换
import re
import pytz
tz = pytz.timezone('Asia/Shanghai')
import datetime
def shi_jian_zhuan_huan(time):
    '''

    :param time: 时间字符串 2020-06-04 16:33 或 2020-06-04 16:33:34
    :return:
    '''
    abc = ''
    try:
        timeOBJ=''
        abc=''
        if re.match('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time): #年月日时分秒
            pattern="%Y-%m-%d %H:%M:%S"
            timstr=re.match('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time).string

        elif re.match('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', time): #年月日时分
            timstr=re.match('\d{4}-\d{2}-\d{2} \d{2}:\d{2}', time).string
            pattern = "%Y-%m-%d %H:%M"
            abc='年月日时分'
        elif re.match('\d{4}-\d{2}-\d{2} \d{2}', time):#年月日时
            timstr=re.match('\d{4}-\d{2}-\d{2} \d{2}', time).string
            pattern = "%Y-%m-%d %H"
            abc='年月日时'
        elif re.match('\d{4}-\d{2}-\d{2}', time):#年月日
            timstr=re.match('\d{4}-\d{2}-\d{2}', time).string
            pattern = "%Y-%m-%d"
            abc='年月日'
        elif re.match('\d{4}-\d{2}', time):#年月
            timstr = re.match('\d{4}-\d{2}', time).string
            pattern = "%Y-%m"
            print(timstr, '年月')
        elif re.match('\d{4}', time):#年
            timstr=re.match('\d{4}', time).string
            pattern = "%Y"
            abc='年'
        timeOBJ=datetime.datetime.strptime(timstr, pattern).astimezone(tz)
        return timeOBJ
    except Exception as e:
        return '时间转换出错 %s %s'%(e,abc)
#日期转换
def date_zhuan_huan(date_str):
    print(date_str)

    return datetime.datetime.strptime(date_str, "%Y-%m-%d").astimezone(tz)

