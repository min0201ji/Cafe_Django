from django.urls import path
from . import views

urlpatterns = [
    path('send/',views.sendEmail), #http://localhost:8000/sendEmail/send/ 요청시 views.sendEmail 함수 요청


]