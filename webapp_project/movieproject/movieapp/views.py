from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Movie
from. forms import MovieForm
# Create your views here.



def index(request):
    movie=Movie.objects.all()
    context={'mv':movie}
    return render(request,'index.html',context)

def detail(request,movie_id):
    mov=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'mv':mov})

def add_movie(requset):
    if requset.method=="POST":
        name=requset.POST.get('name',)
        desc = requset.POST.get('desc', )
        year = requset.POST.get('yr', )
        img = requset.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(requset,'add.html')

def update(request,id):
    mov=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'fm':form,'mv':mov})

def delete(requset,id):
    if requset.method=="POST":
        mov=Movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(requset,'delete.html')
