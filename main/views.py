from django.shortcuts import render
from .models import Quote, GalleryItem
def home(request):
    return render(request,"home.html",{"quotes":Quote.objects.all()[:3],"gallery":GalleryItem.objects.all()[:6]})
def character(request): return render(request,"character.html")
def abilities(request): return render(request,"abilities.html")
def quotes(request): return render(request,"quotes.html",{"quotes":Quote.objects.all()})
def gallery(request): return render(request,"gallery.html",{"gallery":GalleryItem.objects.all()})
