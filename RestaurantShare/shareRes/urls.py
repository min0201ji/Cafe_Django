from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'), # http://localhost:8000 요청 처리
    path('restaurantDetail/',views.restaurantDetail, name='resDetailPage'),#http://localhost:8000/restaurantDetail/ 요청 처리
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'), #http://localhost:8000/restaurantCreate/ 요청 처리
    path('restaurantCreate/create', views.Create_restaurant, name='resCreate'), #
    path('categoryCreate/',views.categoryCreate, name='cateCreatePage'), #http://localhost:8000/categoryCreate/ 요청 처리
    path('categoryCreate/create',views.Create_category, name='cateCreate'), # http://localhost:8000/categoryCreate/Create/ 요청 처리
    path('categoryCreate/delete', views.Delete_category, name='cateDelete'), # categoryCreate/delete/ 요청처리
]