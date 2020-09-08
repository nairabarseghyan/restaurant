from django.shortcuts import render
from .models import Food
from .models import Coffee
from .models import Drink
from .models import Dessert



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

def coffee(request, slug):
    coffee = Coffee.objects.all().order_by('-id')[int(slug) * 15 - 15:int(slug) * 15]
    return render(request,
                    "coffee.html",
                  {'coffees': coffee,
                   'cof_id': [i+1 for i in range(((len(Coffee.objects.all()))//15)+1)]})

def drink(request, slug):
    drink = Drink.objects.all().order_by('-id')[int(slug) * 15 - 15:int(slug) * 15]
    return render(request,
                    "drink.html",
                  {'drinks': drink,
                   'drink_id': [i+1 for i in range(((len(Drink.objects.all()))//15)+1)]})

def dessert(request, slug):
    dessert = Dessert.objects.all().order_by('-id')[int(slug) * 15 - 15:int(slug) * 15]
    return render(request,
                    "dessert.html",
                  {'desserts': dessert,
                   'dessert_id': [i+1 for i in range(((len(Dessert.objects.all()))//15)+1)]})