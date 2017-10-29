from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', index),  # 生产推荐  链接关键字正则/

    # 反向解析测试  url
    url(r'^bookss/$', book,name="na"),

    # 参数测试  url
    # url(r"^try/(\d+)/(\d+)/", try_sum),
    # url(r"^try/(?P<sum1>\d+)/(?P<sum2>\d+)/",try_sum,name="n"),

    # 重定向与页面跳转   坑 测试url
    url(r"^try1/s", try_c),  # 页面跳转url
    # 经测试 在a标签中写入百度网址
    url(r"^www",redirect_baidu),  # 重定向

    url(r"^jpg/$",img),  # 静态图片


    url(r"^jpg_shang/$",jpg_shang),  # 上传文件1
    url(r"^pic_handle/$",pic_handle),  # 上传文件2


    url(r"^verify_code/$", verify_code),  # 测试验证码  没过去



    url(r"^zhuan_yi/$", zhuanyi),



    url(r'hero(\d+)/$', hero),
    url(r"^ceshi/", ceshi1),
    url(r"^get/", get),
    url(r"^post/$", post),
    url(r"^post1/$", post1),
    url(r"^redirect/$", redirec),
    url(r"^jubu_j/$", jubu_j),
    url(r"^jubu/$", jubu),
    url(r"^cookieset/$", cookie_set),
    url(r"^cookieget/$", cookie_get),
    url(r"^session_set/$", session_set),
    url(r"^session_get/$", session_get),

]