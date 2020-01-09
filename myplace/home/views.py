from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Place
# Create your views here.

def home_page(request):
    ctx={}
    all_places=Place.objects.all()
    for place in all_places:
        print(place.place_name)
    ctx['places']=all_places
    return  render(request,'home/home_page.html',ctx)