from django.shortcuts import render

# Create your views here.
def balu(request):
    d={'a':1,'b':2,'c':1}
    return render(request,'balu.html',d)