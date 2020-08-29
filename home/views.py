from django.shortcuts import render

def index(request):
    return render(request, 'home_page.html')

def service(request):
    return render(request, "home/service.html")

def vip(request):
    return render(request, "home/vip.html")

def tables(request):
    return render(request, "home/tables.html")
