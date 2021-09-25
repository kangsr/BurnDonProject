from django import forms
from .models import UserData

class InputForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['goldMoney', 'currentMoney', 'salary', 'age', 'beforeExpense', 'afterExpense']

class InputForm2(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['salary', 'age', 'currentMoney', 'beforeExpense']