from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    ob=Team.objects.all()
    return render(request,"index.html",{'res':obj,'res2':ob})

# def register2(request):
#     return render(request,"register2.html")

# def addition(request):
#     a=int(request.GET['n1'])
#     b=int(request.GET['n2'])
#     c=a+b
#     return render(request,"result.html",{'re':c})


# def contact(request):
#     return HttpResponse('im contact')