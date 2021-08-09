# 2020-06-04
# zhangjun
# 上传文件
from django.conf import settings
import time
import os

def fileSave(file,filepath):
    '''
    文件上传存储
    file: 文件obj
    filepath:文件路径
    :return:
    '''
    msg = {'err': None, 'Result': True, 'filename': None,'size':None}
    try:
        today = time.strftime("%Y%m%d", time.localtime())  # 今天日期
        todayDir = os.path.join('media', filepath, today)  # 今天的日期
        # print('保存文件')

        # print('file obj',file,dir(file))
        # print('todaydir',todayDir)
        if not os.path.isdir(todayDir):
            # print('mkdir',todayDir)
            os.makedirs(todayDir)  # 不存在创建
        filename = os.path.join(todayDir,file.name)
        # print('size',item.size)
        f = open(filename, 'wb')
        for line in file.chunks():
            f.write(line)
        f.close()
        msg['size'] = os.path.getsize(filename)

    except Exception as e:
        msg['err'] = e
        msg['Result'] = False
    else:
        msg['filename'] = filename


    return msg

