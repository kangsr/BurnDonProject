from django.db import models


# Create your models here.
class Bucketlist(models.Model):
    bucket = models.CharField('제목', max_length=200)
    goal_money = models.IntegerField('목표금액', default=0, help_text="만원단위로 입력하세요.")
    saving_money = models.IntegerField('모은금액', default=0, help_text="만원단위로 입력하세요.")

