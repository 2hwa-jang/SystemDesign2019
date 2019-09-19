from django.shortcuts import render

# Create your views here.
def bookstore(request):
    return render(request,'bookstore.html')

def realmap(request):
    return render(request,'realmap.html')