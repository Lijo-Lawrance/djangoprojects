from django.shortcuts import render
from eshop.models import Product
# Create your views here.
from django.db.models import Q


def searchresult(requset):
    products=None
    query=None
    if 'q' in requset.GET:
        query=requset.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(requset,'search.html',{'query':query,'products':products})