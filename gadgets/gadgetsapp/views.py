from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import GadgetsForm
from .models import Gadgets

# Create your views here.
def index(request):
    gadgets = Gadgets.objects.all()
    context={
        'gadgets_list': gadgets
    }
    return render(request,'index.html',context)

def detail(request,gadgets_id):
    gadgets = Gadgets.objects.get(id=gadgets_id)
    return render(request,"detail.html",{"gadgets":gadgets})

def add_gadgets(request):
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        brand=request.POST.get('brand')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        gadgets=Gadgets(name=name,price=price,brand=brand,desc=desc,img=img)
        gadgets.save()
    return render(request,'add.html')

def update(request,id):
    gadgets=Gadgets.objects.get(id=id)
    form=GadgetsForm(request.POST or None,request.FILES,instance=gadgets)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'gadgets':gadgets})

def delete(request,id):
    if request.method=='POST':
        gadgets=Gadgets.objects.get(id=id)
        gadgets.delete
        er(request,'delete.html')