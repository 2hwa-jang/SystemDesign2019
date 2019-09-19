from django.shortcuts import render

# Create your views here.
def board(request):
    return render(request,'board.html')

def detail(request):
    return render(request,'detail.html')

def guide(request):
    return render(request,'guide.html')