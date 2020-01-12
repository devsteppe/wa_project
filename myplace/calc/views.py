from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calc(request):
    from .calc_obj import obj as CALC
    ctx = {}
    ctx['operation']=CALC.keys()
    ctx['tab'] = 'calc'
    template_name='calc/calc_form.html'
    if request.method=='GET':

        return render(request,template_name,ctx)

    elif request.method=='POST':
        try:
            first_number=float(request.POST.get('first'))
            operation=request.POST.get('operation')
            second_number=float(request.POST.get('second'))
            res=CALC[operation](first_number,second_number)
            ctx['result']=res
        except Exception as e:
            print(e)
            ctx['errors']=e
            return render(request,template_name,ctx)
        return render(request,template_name,ctx)
