from django.db import models

class UserData(models.Model):
    goldMoney = models.IntegerField(null=True) # 목표 금액
    currentMoney = models.IntegerField(null=True) # 현재저축액
    salary = models.IntegerField(null=True) # 연봉
    age = models.IntegerField(null=True) # 나이
    beforeExpense = models.IntegerField(null=True) # 은퇴 전 생활비
    afterExpense = models.IntegerField(null=True) # 은퇴 후 생활비