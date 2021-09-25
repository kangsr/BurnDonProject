from typing_extensions import final
from django import forms
from django.forms import fields
from .models import UserData

class InputForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['goldMoney', 'currentMoney', 'salary', 'age', 'beforeExpense', 'afterExpense']

class InputForm2(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['salary', 'age', 'currentMoney', 'beforeExpense']