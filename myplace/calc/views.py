from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calc(request):
    ctx={}
    ctx['tab']='calc'
    return render(request,'calc/calc_form.html',ctx)
