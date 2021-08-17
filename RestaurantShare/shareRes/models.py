from django.db import models

# Create your models here.
class Category(models.Model) :
    category_name = models.CharField(max_length=100) # varChar(100) 인 컬럼 category_name이 테이블에 추가
    # 기본키가 필드 명시가 없으면 자동으로 생성


class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=4) #foreignkey 설정(카테고리를 삭제하면 기본 카테고리로 설정)
    restaurant_name = models.CharField(max_length = 100) #맛집 이름
    restaurant_link = models.CharField(max_length = 500) #맛집 URL
    restaurant_content = models.TextField() # 맛집 설명
    restaurant_keyword = models.CharField(max_length = 50) #키워드