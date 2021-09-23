from django.shortcuts import render, redirect, get_object_or_404
from .models import Bucketlist
from .forms import BucketForm
from django.db.models import Sum

# Create your views here.
def new(request):
    if request.method == 'POST': #글을 작성한 후 저장 버튼을 눌렀을 때
        post_form = BucketForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.save()
            return redirect('list')
    else:   #글을 쓰려고 들어갔을 때
        post_form = BucketForm()   #글을 입력받기 위한 빈 form을 불러옴
        return render(request, 'new.html', {'post_form':post_form})

def list(request):
    buckets = Bucketlist.objects
    goal_money_sum = Bucketlist.objects.aggregate(Sum('goal_money'))
    saving_money_sum = Bucketlist.objects.aggregate(Sum('saving_money'))
    earn_money = Bucketlist.objects.aggregate(earn_total = Sum('goal_money')-Sum('saving_money'))
    return render(request, 'list.html', {'buckets':buckets, 'goal_money_sum':goal_money_sum, 'saving_money_sum':saving_money_sum, 'earn_money':earn_money})

def edit(request, id):
    post = get_object_or_404(Bucketlist, pk = id)
    if request.method == 'GET': #수정하려고 들어갔을 때
        post_form = BucketForm(instance = post)
        #현재 post가 포함된 form을 불러옴
        return render(request, 'edit.html', {'edit_post':post_form})
    else:
        post_form = BucketForm(request.POST, request.FILES, instance = post)
        #현재 post에 가져온 정보를 form에 담음
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
        return redirect('list')

    
def delete(request, id):
    delete_bucket = Bucketlist.objects.get(id = id)
    delete_bucket.delete()
    return redirect('list')
