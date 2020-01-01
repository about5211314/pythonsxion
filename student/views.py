from django.shortcuts import render

# Create your views here.

#导入HttpResponse，用来向网页返回内容的，像print一样，不过HttpResponse是把内容显示到网页上。
from django.http import HttpResponse
# Create your views here.

def index(request):#定义一个函数，第一个参数必须是request
    return HttpResponse("Hello sl测试git和钉钉提醒, world. Hello，python.")#返回HttpResonse对象，最终将这行字符显示在页面上

