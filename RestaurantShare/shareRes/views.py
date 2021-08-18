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

def restaurantDetail(request,res_id) : # 요청된 url로 게시글 id 가 전달됨(파라미터로 받아야 함)
    # 전달된 게시글 id에 해당하는 글을 DB에서 추출한 후 인스턴스변수에 저장
    restaurant = Restaurant.objects.get(id=res_id)
    # 인스턴스변수로 딕셔너리생성
    content = {'restaurant':restaurant}
    # html 파일로 전달해서 동적 렌더링을 진행
    return render(request, 'shareRes/restaurantDetail.html',content)
    #return HttpResponse('restaurantDetail')

def restaurantUpdate(request,res_id):
    #카테고리 수정 시 기존 카테고리에서 선택하게 해야 함(db 카테고리 테이블에서 모든 레코드 추출)
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'categories':categories, 'restaurant':restaurant}
    return render(request,'shareRes/restaurantUpdate.html',content)

def Update_restaurant(request):
    # 사용자가 수정해서 넘겨준 데이터 추출
    resId = request.POST['resId'] # hidden 으로 넘어 옴
    change_category_id = request.POST['resCategory']
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']

    change_category = Category.objects.get(id=change_category_id) # 사용자가 수정한 카테고리 인스턴스 추출해서 변수 저장
    before_restaurant = Restaurant.objects.get(id=resId) # 수정할 레코드 추출해서 인스턴스 변수로 저장
    # 수정 대상 인스턴스에 새로운 값 대입
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    # db에 저장
    before_restaurant.save()
    # 상세보기 페이지로 재 요청 http://127.0.0.1:8000/restaurantDetail/1
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id': resId}))

def Delete_restaurant(request):
    # 삭제할 게시글 id request 에서 추출
    res_id = request.POST['resId']
    # db에서 삭제할 게시글 인스턴스 생성
    restaurant = Restaurant.objects.get(id=res_id)
    # db에서 삭제
    restaurant.delete()
    # index.html 재요청
    return HttpResponseRedirect(reverse('index'))

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


