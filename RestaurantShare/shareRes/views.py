from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request) :
    # 기존에 입력되어 있는(혹은 새로 입력한) 카테고리 내용을 DB에서 select함
    categories = Category.objects.all() # select 진행 후 결과 반환
    restaurants = Restaurant.objects.all()

    # rendering에 사용할 dict로 구성
    content = {'categories':categories, 'restaurants':restaurants}

    # 구성된 dict를 rendering에 사용하도록 전달
    return render(request,'shareRes/index.html', content) # 클라이언트 요청에 대해 html 코드 랜더링(반환포함)
    #return HttpResponse('index') # 요청에의하 응답 확인

def restaurantCreate(request) :
    # restaurantCreate.html 파일을 rendering 할 때 카테고리 선택을 위한 데이터는 동적으로 추가되도록 코딩
    # Category 테이블에서 레코드 모두 추출
    categories = Category.objects.all()

    # 딕셔너리 구성
    content = {'categories':categories}

    # 랜더링 사용할 수 있도록 html파일에 전달
    return render(request, 'shareRes/restaurantCreate.html',content)
    #return HttpResponse('restaurantCreate')

def Create_restaurant(request):
    # 외래키로 연결된 카테고리컬럼은 저장을 일반 값이 아닌 해당카테고리 레코드의 인스턴스를 넘겨줘야 함
    # 카테고리 id 추출
    category_id = request.POST['resCategory']
    # 카테고리 테이블의 레코드 인스턴스 반환
    category = Category.objects.get(id=category_id) # 현 코드에서 생성되는 인스턴스를 db로 전달해야 함

    # 나머지 입력 데이터 추출
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']

    # 맛집 입력 모델 테이블인 Restaurant의 인스턴스를 생성
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link,
                         restaurant_content=content, restaurant_keyword=keyword)
    new_res.save() # DB저장

    # 저장된 결과를 출력하기 위해 index.html 파일 요청
    return HttpResponseRedirect(reverse('index')) # index 함수에서 Restaurant 추가 내용이 표출되도록 수정
    #return HttpResponse('맛집 DB 저장합니다!')

def restaurantDetail(request) :
    return render(request, 'shareRes/restaurantDetail.html')
    #return HttpResponse('restaurantDetail')

def categoryCreate(request) :
    categories = Category.objects.all() # categories 변수에는 Category 테이블의 모든 레코드를 반환 받아서 저장
    # Category 테이블 컬럼: id, category_name
    content = {'categories' : categories}
    return render(request, 'shareRes/categoryCreate.html', content)
    #return HttpResponse('categoryCreate')

def Create_category(request) :
    # 사용자가 입력한 카테고리 Data를 추출해서 DB에 저장
    # 1. 사용자가 입력한 카테고리 Data를 추출(post방식으로 서버에 전송됨)
    category_name = request.POST['categoryName']

    # 2. 추출 Data DB에 저장
    new_category = Category(category_name=category_name) # 모델에 data를 적용한 인스턴스 생성(insert 구문 생성)
    new_category.save() # insert 구문 db에 반영

    # DB 저장 완료 후 index.html 파일을 재 요청
    return HttpResponseRedirect(reverse('index')) #index url(기본페이지요청)
    #return HttpResponse('여기서 카테고리 저장을 구현합니다!')

def Delete_category(request): # 카테고리 삭제
    category_id = request.POST('categoryId') #hidden태그로 인해 전송됨
    # 레코드 삭제
    # 해당 레코드 가져오기
    delete_category = Category.object.get(id=category_id)
    delete_category.delete() #db 내부에서 해당 레코드 삭제
    return HttpResponseRedirect(reverse('cateCreatePage'))


