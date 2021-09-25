from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import UserData

@csrf_exempt
def page2(req):
    form = InputForm(req.POST, req.FILES)
    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        return redirect('page5')
    return render(req, 'page2.html', {'form':form})

def page5(req):
    data = UserData.objects.last()
    gold = data.goldMoney #목표금액
    salary = data.salary #연봉
    age = data.age
    before = data.beforeExpense #은퇴전생활비
    after = data.afterExpense #은퇴후생활비

    deposit = (salary/12)-before #연간저축액
    lastYear = gold/(after*12)
    goldAge = age + gold/(deposit*12) #달성가능 나이
    return render(req, 'page5.html', {'data':data, 'deposit':deposit, 'goldAge':goldAge, 'lastYear':lastYear})

def page3(req):
    form = InputForm2(req.POST, req.FILES)
    if form.is_valid():
        _data = form.save(commit=False)
        _data.save()
        return redirect('page6')
    return render(req, 'page3.html', {'form':form})

def page6(req):
    data = UserData.objects.last()
    salary = data.salary # 연봉
    before = data.beforeExpense # 은퇴전생활비
    age = data.age
    monthDeposit = (salary/12)-before # 월저축액
    yearDeposit = monthDeposit * 12 # 연저축액
    year = 2021 # 올해

    age_arr = [] # 그래프에 표시될 나이 배열
    year_arr = [] # 그래프에 표시될 연도 선언
    yearDeposit_arr = [] # 그래프에 표시될 예상 저축액 선언

    # 위 배열을 5단위로 표시
    for i in range(10):
        yearDeposit += yearDeposit*5
        age_arr.append(age+(i*5))
        year_arr.append(year+(i*5))
        yearDeposit_arr.append(yearDeposit)

    return render(req, 'page6.html', {'data':data, 'age_arr':age_arr, 'year_arr':year_arr, 'yearDeposit_arr':yearDeposit_arr})