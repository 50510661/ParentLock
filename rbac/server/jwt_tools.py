import jwt
import datetime
from jwt import exceptions
JWT_SALT='334532ADFewdwqer53@#￥2%3243453@1DDAF5432345u'
def get_token(payload, timeout=20):
    """
    :param payload:  例如：{'user_id':1,'username':'wupeiqi'}用户信息
    :param timeout: token的过期时间，默认20分钟
    :return: 获取token
    """
    headers = {'typ': 'jwt','alg': 'HS256'}
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=timeout)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).encode('utf-8')
    # result 为token
    return result
def parse_payload(token):
    """
    对token进行和发行校验并获取payload
    :param token:
    :return:验证token
    """
    result = {'status': False, 'data': None, 'error': None}
    try:
        verified_payload = jwt.decode(token, JWT_SALT, algorithms=['HS256'])
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result
