from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import InputForm
from .models import UserData

@csrf_exempt
def new(req):
    form = InputForm(req.POST, req.FILES)
    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        return redirect('page5')
    return render(req, 'new.html', {'form':form})

def page5(req):
    data = UserData.objects.values()
    gold = data[0]['goldMoney'] #목표금액
    salary = data[0]['salary'] #연봉
    after = data[0]['afterExpense'] #은퇴후생활비
    before = data[0]['beforeExpense'] #은퇴전생활비
    age = data[0]['age']
    deposit = (salary/12)-before #연간저축액
    lastYear = gold/(after*12)
    goldAge = age + gold/(deposit*12) #달성가능 나이
    return render(req, 'page5.html', {'data':data, 'deposit':deposit, 'goldAge':goldAge, 'lastYear':lastYear})

def new2(req):
    form = InputForm(req.POST, req.FILES)
    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        return redirect('core2')
    return render(req, 'inputpage2.html', {'form':form})

def page6(req):
    data = UserData.objects.values()
    salary = data[0]['salary'] # 연봉
    before = data[0]['beforeExpense'] # 은퇴전생활비
    age = data[0]['age']
    monthDeposit = (salary/12)-before # 월저축액
    yearDeposit = monthDeposit * 12 # 연저축액
    year = 2021 # 올해

    age_arr = [] # 그래프에 표시될 나이 배열
    year_arr = [] # 그래프에 표시될 연도 선언
    yearDeposit_arr = [] # 그래프에 표시될 예상 저축액 선언

    # 위 배열을 5단위로 표시
    for i in range(10):
        age_arr[i].append(age+(i*5))
        year_arr[i].append(year+(i*5))
        yearDeposit_arr[i].append(yearDeposit(i*5))

    return render(req, 'core2.html', {'data':data, 'age_arr':age_arr, 'year_arr':year_arr, 'yearDeposit_arr':yearDeposit_arr})