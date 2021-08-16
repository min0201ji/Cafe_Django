from django.db import models

# Create your models here.
class Category(models.Model) :
    category_name = models.CharField(max_length=100) # varChar(100) 인 컬럼 category_name이 테이블에 추가
    # 기본키가 필드 명시가 없으면 자동으로 생성