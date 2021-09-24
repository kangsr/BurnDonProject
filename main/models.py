from django.db import models

class UserData(models.Model):
    goldMoney = models.IntegerField() # 목표 금액
    currentMoney = models.IntegerField() # 현재저축액
    salary = models.IntegerField() # 연봉
    age = models.IntegerField() # 나이
    beforeExpense = models.IntegerField() # 은퇴 전 생활비
    afterExpense = models.IntegerField() # 은퇴 후 생활비