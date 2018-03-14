from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Album, Song
from django.template import loader
# Create your views here.



def index(request):
    all_album = Album.objects.all()
    template = loader.get_template('blog/index.html')

    context = {
        'all_album' : all_album,
    }
    return render(request,'blog/index.html',context)


def detail(request, album_id):
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'blog/detail.html',{'album':album})


def favorite(request, album_id):
    return HttpResponse("return")




