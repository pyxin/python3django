# coding=utf-8
# 导入注册对象Library
from django.template import Library

register = Library()

# 适用装饰器注册  因为register是导入的库函数的一个对象
@register.filter
# 自定义一个求余的函数返回
def mod(value,a):
    return value+a
# 使用自定义过滤器需要 在模板中添加 {%load 本文件名%}标签
@register.filter
def mos(value,add):
    return value+add