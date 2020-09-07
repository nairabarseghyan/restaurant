from django.shortcuts import render
from .models import Food


def index(request):
    return render(request, 'home_page.html')

def service(request):
    return render(request, "home/service.html")

def vip(request):
    return render(request, "home/vip.html")

def tables(request):
    return render(request, "home/tables.html")

def slug(request, slug):
    foods = Food.objects.all().order_by('-id')[int(slug) * 15 - 15:int(slug) * 15]
    return render(request,
                    "slug.html",
                  {'foods': foods,
                   'id': [i+1 for i in range(((len(Food.objects.all()))//15)+1)]})
