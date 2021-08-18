from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'), # http://localhost:8000 요청 처리
    path('restaurantDetail/delete',views.Delete_restaurant, name='resDelete'),
    path('restaurantDetail/<str:res_id>',views.restaurantDetail, name='resDetailPage'),
    #http://localhost:8000/restaurantDetail/1 요청 처리
    #http://localhost:8000/restaurantDetail/2 요청 처리
    path('restaurantDetail/updatePage/update',views.Update_restaurant,name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>',views.restaurantUpdate,name='resUpdatePage'),
    # 서버는 res_id 라는 변수를 사용할 수 있게됨 - 처리함수에서는 해당 변수를 파라미터로 받아야만 사용가능


    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'), #http://localhost:8000/restaurantCreate/ 요청 처리
    path('restaurantCreate/create', views.Create_restaurant, name='resCreate'), #
    path('categoryCreate/',views.categoryCreate, name='cateCreatePage'), #http://localhost:8000/categoryCreate/ 요청 처리
    path('categoryCreate/create',views.Create_category, name='cateCreate'), # http://localhost:8000/categoryCreate/Create/ 요청 처리
    path('categoryCreate/delete', views.Delete_category, name='cateDelete'), # categoryCreate/delete/ 요청처리
]