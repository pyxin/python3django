import random
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.utils.six import BytesIO

from .models import *
from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from django.shortcuts import redirect  # 重定向模块导入
from django.template import loader, RequestContext
from book.settings import MEDIA_ROOT


# Create your views here.
def index(request):
    return render(request, 'book_app/index.html')


# render 调用模板函数
# 解析顺序 字典 > 对象(先属性>方法  切不能传参) > list
#  不存在插''


def book(request):
    booklist = bookinfo.objects.all()
    context = {'Tem_title': '图书信息', 'Tem_booklist': booklist}
    return render(request, 'book_app/book.html', context)


def hero(request, hid):
    books=bookinfo.objects.all()
    book = bookinfo.objects.get(id=int(hid))
    # 定义一个变量存储指定id的图书实例对象     缓存
    tem_herolist = book.heroinfo_set.all()
    # tem_herolist = []
    # 定义一个list存储用户指定图书   的所有人物信息 对象
    context = {"Tem_title": "英雄信息", "tem_book": book.btitle, "tem_herolist": tem_herolist,"books":books}
    return render(request, 'book_app/hero.html', context)


def ceshi1(request):
    # 获取装载的对象模板??
    # template = loader.get_template('book_app/ceshi1.html')
    #
    # context = RequestContext(request, {"title": "图书列表"})
    # # http://192.168.80.132:8000/ceshi/?a=2daa
    # path = request.path  # 仅获取路径
    # # /ceshi/
    # get_path = request.get_full_path()  # 获取路径及参数
    # # /ceshi/?a=2daa
    # method = request.method  # 获取页面请求的方式
    # # GET
    # GE = request.GET  # GET请求方式的数据 ?sss=1
    # #  sss
    # PO = request.POST
    # return  HttpResponse(GE.get())
    # # return HttpResponse(template.render(context))
    return render(request, "book_app/ceshi1.html")


def redirec(request):
    return HttpResponsePermanentRedirect("/book/")


def get(request):
    dictt = request.GET
    a = dictt.get("a")
    b = dictt.get("b")
    c = type(dictt.get("c"))
    d = dictt.get("d", "4we")
    e = dictt.get("e")
    context = {'a': a, "b": b, "c": c, "d": d, "e": e}
    return render(request, "book_app/get.html", context)


def post(request):
    return render(request, "book_app/post.html")


def post1(request):
    # return render(request,"book_app/post1.html")
    return redirect("/")


def jubu_j(request):
    return render(request, "book_app/jubu_j.html")


def jubu(request):
    book = bookinfo.objects.all()
    print(book)
    list1 = list()

    for bookname in book:
        list1.append({'name': bookname.btitle})
    jsdict = {"booklist": list1}
    return JsonResponse(jsdict)


def cookie_set(request):
    t = HttpResponse("<h1>" + "我才" + "</h1>")
    t.set_cookie("shikey", "oooo", max_age=None, path="/")
    print(type(t))
    return t


def cookie_get(request):
    # values=request.COOKIES["shikey"]
    if request.COOKIES.get("ss"):
        # 字典通过key取值 直接[key]取 不存在会报错, 通过get("key")取不存在不会报错
        values = request.COOKIES["shikey"]
    else:
        values = "不在"
    return render(request, "book_app/cookiesget.html", {"cookieget": values})


def session_set(request):
    request.session['o1'] = "ooooooooooooooooooooooooooooooooo"
    return HttpResponse("<h1>" + "session" + "</h1>")


def session_get(request):
    w = request.session.get("o1",default=111)
    return HttpResponse("<h1>" + w + "</h1>")


def try_sum(request,sum2,sum1):
    return render(request,"book_app/try.html",context={"tem1":sum1,"tem2":sum2})

def redirect_baidu(request):
    return HttpResponsePermanentRedirect("www.baidu.com/s?wd=www")

def try_c(request):
    print(request.GET.get("wd"))
    return


def img(request):

    return render(request,"book_app/jpg.html")


def jpg_shang(request):
    return render(request,"book_app/jpg_shang.html",)


def pic_handle(request):
    if request.method == "POST":  # 判断是不是post类型
        fil = request.FILES.get("pic",None)  # 获取request中的文件对象属性
        print(fil)
        if not fil:  # 判断是否为空
            print("*"*40)
            return HttpResponse("没有文件")  # todo 这里返回一个新界面  能不能让他返回他本身的页面做成 类似局部刷新的效果
        fname = "%s/book_app/%s" % (MEDIA_ROOT, fil.name)
        with open(fname, 'wb') as pic:
            for c in fil.chunks():  # todo 一个方法 类似list  没说
                pic.write(c)
        # 添加数据到文件
        # p = PicTest()
        # p.pic = "book_app/%s" % fil.name
        # p.save()
        # # 添加数据记录 1
        PicTest.objects.create(pic="book_app/%s"%fil.name)
        # 添加数据记录2
    return HttpResponse("ok")  # todo 这里返回一个新界面  能不能让他返回他本身的页面做成 类似局部刷新的效果



def verify_code(request):
    bgcolor = (random.randrange(20,100), random.randrange(20,100),255)
    width = 100
    height = 25
    print("1")
    # 创建画面对象
    im = Image.new("RBG",(width,height), bgcolor)   # todo 找不到模块
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    for i in range(100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill= (random.randrange(0,255), random.randrange(0,255))
        draw.point(xy, fill=fill)
    print("2")
    strl = "qwertyuiopasdfghjk10923lz54xcvbnmQWER43TYUIOPASD2FGHJKLZXCVBNM"
    # 随机选出4个作为验证码
    rand_str = ""
    for i in range(4):
        rand_str +=strl[random.randrange(0,len(strl))]
    # 构造字体对象,ubuntu字体目录“/usr/share/fonts/truetype/freefont"
    font = ImageFont.truetype("FreeMono.ttf",23)
    # 构造字体颜色
    fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
    # 绘出4个字
    draw.text((5,2),rand_str[0],font=font, fill=fontcolor)
    draw.text((25,2),rand_str[1],font=font, fill=fontcolor)
    draw.text((50,2),rand_str[2],font=font, fill=fontcolor)
    draw.text((75,2),rand_str[3],font=font, fill=fontcolor)
    del draw
    # 存入session  用于验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf=BytesIO()
    # 将图片存入内存 文件类型png
    im.save(buf,"png")
    # 将内存中的图片返回给客户端,
    return HttpResponse(buf.getvalue,"image/png")



def zhuanyi(request):
    con= {"tem_context": '<H2>返回上一级</H2>'}
    return render(request,"book_app/zhuan_yi.html", con)

