from django.contrib import admin
from .models import *


# Register your models here.

# admin.site.register(bookinfo)
# admin.site.register(heroinfo)


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ["btitle", "bpub_date", "bread", "bcomment", "id", "isDelete"]
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    fields = ["btitle", "bread", "bcomment", "bpub_date", "isDelete"]  # todo 不能添加日期???
    # fieldsets = (
    #     ('基本', {'fields': ['btitle', 'isDelete']}),  # todo 主键id 不能写这里 报错 id 不在book类中  是根据类中属性定的貌似
    #     ('高级', {'fields': [ 'bread', 'bcomment']}),  # todo 不知道为什么 不能写日期  难道是类型限制???
    # )
    # list_filter = ["bcomment1", "bread1"]  # todo 过滤器不能显示中文.............
    # list_display = ["btitle", "bpub_date1", "bread1", "bcomment1", "id", "isDelete1"]


class HeroInfoAdmin(admin.ModelAdmin):
    # list_display = ["btitle", "bpub_date", "bread", "bcomment", "id", "isDelete"]
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    # list_filter = ["bcomment","bread"]
    list_display = ['hname1', 'hgender1', 'gongfu', 'hbook1']
    fields = ["hbook", "hname"]  # todo 不能使用改后的名字比如hname1


admin.site.register(heroinfo, HeroInfoAdmin)
admin.site.register(bookinfo, BookInfoAdmin)
admin.site.register(PicTest, )  # todo 貌似对命名 有要求  本来是1 (1).jpg  传过变成了1_1.jpg

