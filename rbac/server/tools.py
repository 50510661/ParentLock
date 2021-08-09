from django.conf import settings
import time
import os
import requests
import pytz
tz = pytz.timezone('Asia/Shanghai')
import datetime
class tools():
    '''
    #项download_file
    '''
    def __init__(self):
        self.ret = {'state': True, 'message': None}
    # 下载文件或图片
    def download_file(self,url, filepath,filename):
        '''
        :param url: http://XXX
        :param filepath: /home/xxx/xx/xx/media
        :return:
        '''
        try:
            # print('下载文件开始。。。',filepath,url)
            if not os.path.isdir(filepath):
                # print('mkdir',filepath)
                os.makedirs(filepath)  # 不存在创建
            file_data = requests.get(url, allow_redirects=True).content
            with open(os.path.join(filepath,filename), 'wb') as handler:
                handler.write(file_data)
            self.ret['message']=filepath
        except Exception as e:
            self.ret['state']=False
            self.ret['message']='下载 %s 出错【%s】'%(url,e)
        finally:return self.ret
    def time_stamp_to_time(self,tst):
        # 时间戳转时间
        local_format = "%Y-%m-%d %H:%M:%S"
        if len('%s'%tst) == 13:
            t1=time.localtime(int(tst/1000))
        elif len('%s'%tst) == 10:
            t1 = time.localtime(tst)
        time_str = time.strftime(local_format, t1)
        return time_str
