from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def mypage(request):
    return render(request,'mypage.html')

def signin(request):
    return render(request,'signin.html')