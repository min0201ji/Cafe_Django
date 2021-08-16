from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request) :
    return render(request,'shareRes/index.html') # 클라이언트 요청에 대해 html 코드 랜더링(반환포함)
    #return HttpResponse('index') # 요청에의하 응답 확인

def restaurantCreate(request) :
    return render(request, 'shareRes/restaurantCreate.html')
    #return HttpResponse('restaurantCreate')

def restaurantDetail(request) :
    return render(request, 'shareRes/restaurantDetail.html')
    #return HttpResponse('restaurantDetail')

def categoryCreate(request) :
    return render(request, 'shareRes/categoryCreate.html')
    #return HttpResponse('categoryCreate')