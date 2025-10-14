from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_view(request):
    return HttpResponse("姓名：代卫婷<br>学号：20231201001", content_type="text/html")
