from django import forms
from .models import Bucketlist

class BucketForm(forms.ModelForm):
    class Meta:
        model = Bucketlist
        fields = ['bucket', 'goal_money', 'saving_money']

