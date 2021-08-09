# 将项目相关数据写入数据库
# 张军
# 13535539134
# 2020-07-07
from Project.models import Project #项目
from Customer.models import CustomerInof #客户表
from Project_Funding.models import Capital #奖金表
from Project_Funding.models import lin_gong_gong_zi #明细
from django.db.models import Q,F
from Document_management.models import Document #文档表
from OA.excel import excel #处理excel表格
oafrom_excel = excel()  # 临工工资处理
class Project_inif_save(object):
    '''
    存储项目信息
    '''
    def __init__(self):
        self.Project=None #项目
        self.msg = {'code': 0, 'info': None,'content':None,
                    'tab_head':None,
                    'tab_tail':None,
                    'explain':None,
                    'filenameObj':None,
                    'xiangmu':None}
    def lin_gong_gong_zi(self,request,gongzhixing):
        '''
        临工工资
        :return:
        '''
        try:

            title=gongzhixing.get('tab_head').get('title')
            project=Project.objects.get(pk=gongzhixing.get('xiangmu_id'))
            filenameObj=Document.objects.filter(file=gongzhixing.get('filename')).first()#文件obj
            print('filenameObj',filenameObj)
            heji_ying_fu=gongzhixing.get('heji_ying_fu') #合计应付
            self.msg['tab_head']={'title':title,'heji_ying_fu':heji_ying_fu}
            self.msg['xiangmu']=project
            self.msg['filenameObj']=filenameObj
            if Capital.objects.filter(filename=filenameObj).first() == None:
                print('工资表不存在')
                capitalObj=Capital.objects.create(
                    title=title,
                    project=project,
                    capital_tyep='0',#人工工资
                    money=heji_ying_fu, #合计应付
                    state='2',#草稿
                    simple='人工工资',
                    user=request.user,
                    filename=filenameObj,#文件
                )
            capitalObj=Capital.objects.filter(filename=filenameObj).first()
            print('工资表',capitalObj)
            gonzi_list = oafrom_excel.lin_gong_gong_zi(gongzhixing.get('filename'), project)  # 返回工资处理结果
            print(len(gonzi_list.get('ret')))
            print('-'*100)
            for gongren in gonzi_list.get('ret'):
                # print(gongren)
                userID=gongren.get('userID') #身份证
                haoma=gongren.get('haoma') #手机号码
                print(gongren.get('name'),userID,haoma)
                customerobj=CustomerInof.objects.filter(shen_fen_zhen=userID).first() #身份证唯一工人客户OBJ
                print('工人obj',customerobj)
                if customerobj == None:#不存在就创建
                    print('创建客户')
                    customerobj=CustomerInof.objects.create(
                        name=gongren.get('name'),
                        PhoneNumber=haoma,
                        user=project.user,
                        shen_fen_zhen=userID,
                        CUSTOMER_TYPE='2',
                        yin_hang_zhang_hao=gongren.get('zhang_hao'),
                        yin_hang=gongren.get('kai_hu_hang'),
                    ).save
                    print('创建客户完成',customerobj)
                customerobj=CustomerInof.objects.filter(shen_fen_zhen=userID).first() #工人OBJ

                lin_obj = lin_gong_gong_zi.objects.filter(capital=capitalObj, customer=customerobj).first()

                if lin_obj == None: #如果这个工人没有创建这个表就添加这个表单
                    print('临时工不存在就添加临时工工资')
                    linggongObj=lin_gong_gong_zi(
                        capital=capitalObj,
                        customer=customerobj,
                        tian=gongren.get('tian'),#工作天数
                        gong_zi=gongren.get('gong_zi'),#工资/天(元)
                        jia_ban=gongren.get('jia_ban_shi_jian'),#加班
                        jia_ban_gong_zi=gongren.get('jia_ban_yuan'),#元/小时（元)
                        ying_fu=gongren.get('yingfu'),#应付
                        shi_fu=gongren.get('shi_fu'),#实付
                        kou_kuan=gongren.get('kou_kuan'),#扣款
                    ).save()

                    self.msg['info'] = '临时工工资存储完毕'
                else:
                    self.msg['info'] = '临时工工资已经存在不需要重复添加'
                self.msg['content'] = capitalObj  # 所有人员

            # print(linggongObj)


        except Exception as e:
            self.msg['code']=1
            self.msg['info'] = '临时工工资存储过程出错 [%s]'%e
        return self.msg
