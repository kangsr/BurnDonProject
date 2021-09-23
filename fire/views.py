from django.shortcuts import render

# Create your views here.
def service1(request):
  return render(request, "service1_input.html")