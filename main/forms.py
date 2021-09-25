from django import forms
from django.forms import ModelForm, NumberInput
from .models import UserData

class InputForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['goldMoney', 'currentMoney', 'salary', 'age', 'beforeExpense', 'afterExpense']
        
        # widgets = {
        #     'goldMoney' : NumberInput(attrs={
        #         'class': "",
        #     })
        # }

class InputForm2(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['salary', 'age', 'currentMoney', 'beforeExpense']