from django.shortcuts import render, redirect
from app1.models import *
from django.core.files.storage import FileSystemStorage


def kino(request):
    list_kino = Kino.objects.all()
    context= {'list_kino': list_kino}

    if request.method == "POST":
 
        create_film(request)
    return render(request, 'app1/kino.html',context=context)

def film(request):
    list_kino = Kino.objects.filter(type='Фільм')
    context= {'list_kino': list_kino}

    if request.method == "POST":
        create_film(request)
    return render(request, 'app1/kino.html',context=context)

def serial(request):
    list_kino = Kino.objects.filter(type='Серіал')
    context= {'list_kino': list_kino}

    if request.method == "POST":
        create_film(request)
    return render(request, 'app1/kino.html',context=context)

def multserial(request):
    list_kino = Kino.objects.filter(type='Мультсеріал')
    context= {'list_kino': list_kino}

    if request.method == "POST":
        create_film(request)
       
    return render(request, 'app1/kino.html',context=context)

def multfilm(request):
    list_kino = Kino.objects.filter(type='Мультфільм')
    context= {'list_kino': list_kino}

    if request.method == "POST":
        create_film(request)
    return render(request, 'app1/kino.html',context=context)


def create_film(request):
    
    name = request.POST.get('name')
    graduationYear = request.POST.get('graduationYear')
    genre = request.POST.get('genre')
    linkToView = request.POST.get('linkToView')
    type = request.POST.get('type')
    image = request.POST.get('image')
   
    if name and graduationYear and genre and linkToView and type and request.FILES['image']:
        image_file = request.FILES['image']
        file = FileSystemStorage().save('app1/image/' + image_file.name, image_file)
        file_url = FileSystemStorage().url(file)
        Kino.objects.create(name = name, graduationYear = graduationYear, genre = genre, linkToView = linkToView, type = type, image = file_url)

def start(request):
    return redirect('kino/')
    
# Create your views here.
