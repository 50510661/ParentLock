# 分页
# 2020/05/30
# 50510661@qq.com

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def fenye(pags,currentPage,pags_number=10):
    '''
    需要分页数据
    :param pags: 需要分页数据
    :param currentPage: 当前页
    :return:
    '''

    currentPage = int(currentPage)
    paginator = Paginator(pags, pags_number)  # 实例化对象,每页显示10条信息
    # page = paginator.page(currentPage)
    if currentPage - 5 < 1:  # 如果-5小于1就说明到头了
        if paginator.num_pages - 9 < 1:
            pageRange = range(1, paginator.num_pages)
        else:pageRange = range(1, 9)
    elif currentPage + 5 > paginator.num_pages:  # 如果大于总数就是到头了
        pageRange = range(currentPage - 5, paginator.num_pages + 1)
    else:
        pageRange = range(currentPage - 5, currentPage + 5)

    try:
        pages = paginator.page(currentPage)  # 生成本页面信息
    except PageNotAnInteger:  # 页码不是整数，就显示第一页面
        pages = paginator.page(1)
    except EmptyPage:
        # 页码不超出范围
        pages = paginator.page(paginator.num_pages)  # 页码不超出范围就显示最后一页
    # 分页结束

    msg={'pages':pages,'currentPage':currentPage,'pageRange':pageRange,'paginator':paginator}
    return msg
