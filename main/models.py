from django.db import models

class UserData(models.Model):
    goldMoney = models.IntegerField('목표 저축액', null=True, help_text="만") # 목표 금액
    currentMoney = models.IntegerField('현재 저축액', null=True, help_text="만") # 현재저축액
    salary = models.IntegerField('나의 연봉', null=True, help_text="만") # 연봉
    age = models.IntegerField('나의 나이', null=True, help_text="만") # 나이
    beforeExpense = models.IntegerField('은퇴 전 월간', null=True, help_text="만") # 은퇴 전 생활비
    afterExpense = models.IntegerField('은퇴 후 월간', null=True, help_text="만") # 은퇴 후 생활비